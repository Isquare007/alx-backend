function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData);

    job
      .on('enqueue', () => {
        console.log(`Notification job created: ${job.id}`);
      })
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed', (errorMessage) => {
        console.log(`Notification job ${job.id} failed: ${errorMessage}`);
      })
      .on('progress', (progress, total) => {
        const percentage = (progress / total) * 100;
        console.log(`Notification job ${job.id} ${percentage}% complete`);
      });

    job.save();
  });
}

module.exports = createPushNotificationsJobs;
