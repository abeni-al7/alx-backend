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

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  } else {
    console.log(message);
  }
});
