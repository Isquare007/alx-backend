const kue = require('kue');

const jobData = {
  phoneNumber: 'string',
  message: 'string',
};

const queue = kue.createQueue();

const job = queue.create('push_notification_code', jobData);

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});
job.on('complete', () => {
  console.log('Notification job completed');
});
job.on('failed', () => {
  console.log('Notification job failed');
});

job.save((err) => {
  if (err) {
    console.error('Failed to create notification job:', err);
    return;
  }
});
