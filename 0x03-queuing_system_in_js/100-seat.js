import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';
import express from 'express';

const client = redis.createClient();
client.on('error', (err) => console.error('Redis error:', err));

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const reserveSeat = (number) => {
  return setAsync('available_seats', number);
}

const getCurrentAvailableSeats = async () => {
  const seats = await getAsync('available_seats');
  return parseInt(seats, 10) || 0;
}

let reservationEnabled = true;
reserveSeat(50);

const queue = kue.createQueue();

const app = express();
const port = 1245;

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (!err) {
      return res.json({ status: 'Reservation in process' });
    } else {
      return res.json({ status: 'Reservation failed' });
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();

    if (currentSeats > 0) {
      await reserveSeat(currentSeats - 1);
      if (currentSeats - 1 === 0) {
        reservationEnabled = false;
      }
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
