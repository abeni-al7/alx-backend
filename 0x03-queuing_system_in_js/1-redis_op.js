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

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, reply) => {
    redis.print(err, reply);
  });
}

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    if (err) console.error(err);
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
