export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }
  jobs.forEach(obj => {
    const job = queue.create('push_notification_code_3', obj)
    .save((err) => {
      if (err) {
        console.log(err);
      } else if (job !== undefined) {
        console.log(`Notification job created: ${job.id}`);
      } else {
        console.log('Job created');
      }
    });

    if (job) {
      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      })
      .on('progress', (progress, data) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
    }

    
  });
}