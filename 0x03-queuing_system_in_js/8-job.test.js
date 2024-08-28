import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not array', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234' },
      { phoneNumber: '4153518781', message: 'This is the code 1235' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
