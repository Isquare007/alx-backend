const { expect } = require('chai');
const kue = require('kue');
const { createPushNotificationsJobs } = require('./8-job');

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    const invalidJobs = 'not an array';
    expect(() => createPushNotificationsJobs(invalidJobs, queue)).to.throw(
      'Jobs is not an array'
    );
  });

  it('should create jobs in the queue and log the corresponding messages', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
      {
        phoneNumber: '4153518743',
        message: 'This is the code 4321 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(jobs.length);

    const expectedLogMessages = [
      'Notification job created:',
      'Notification job created:',
      'Notification job created:',
    ];

    queue.testMode.jobs.forEach((job, index) => {
      expect(job.type).to.equal('push_notification_code_3');
      expect(job.data).to.deep.equal(jobs[index]);
      expect(console.log.calledWith(expectedLogMessages[index])).to.be.true;
    });
  });
});
