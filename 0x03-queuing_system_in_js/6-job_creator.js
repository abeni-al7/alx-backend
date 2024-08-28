import kue from 'kue';

const queue = kue.createQueue();
const jobData = {
  phoneNumber: "+251999999999",
  message: "Do the job",
}

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.log(err);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
})
.on('failed', (err) => {
  console.log('Notification job failed');
});
