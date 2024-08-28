import redis from 'redis';

const client = redis.createClient();

const task = () => {
  client.on('connect', () => {
    console.log('Redis client connected to the server');
  });

  client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });
}

task();

const hash = [
  { 'Portland': 50 },
  { 'Seattle': 80 },
  { 'New York': 20 },
  { 'Bogota': 20 },
  { 'Cali': 40 },
  { 'Paris': 2 },
];

hash.forEach((obj) => {
  const key = Object.keys(obj)[0];
  const value = obj[key];
  client.hset('HolbertonSchools', key, value, (err, reply) => {
    redis.print(err, reply);
  });
});

client.hgetall('HolbertonSchools', (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log(reply);
  }
});
