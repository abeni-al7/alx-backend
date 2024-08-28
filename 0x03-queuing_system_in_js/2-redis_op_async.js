import redis from 'redis';
import util from 'util';

const client = redis.createClient();

const setAsync = util.promisify(client.set).bind(client);
const getAsync = util.promisify(client.get).bind(client);

const task = () => {
  client.on('connect', () => {
    console.log('Redis client connected to the server');
  });

  client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });
}

task();

const setNewSchool = async (schoolName, value) => {
  try {
    const reply = await setAsync(schoolName, value);
    redis.print(reply);
  } catch (err) {
    redis.print(err);
  }
}

const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
