const kue = require('kue');
import createPushNotificationsJobs from './8-job.js';

const assert = require('assert')

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

  it('should validate the jobs inside the queue', () => new Promise((done) => {
    const lists = [{ phoneNumber: '790003-3-33', message: 'This is your code 1803' }, { phoneNumber: '7980-30039-00', message: 'This is your code 9039' }];
    createPushNotificationsJobs(lists, queue);

    const { jobs } = queue.testMode;

    assert.equal(jobs.length, lists.length);
    done();
  }));

  it('should display an error message if jobs is not an array', () => new Promise((done) => {
    const lists = {
      phoneNumber: '790003-3-33', message: 'This is your code 1803', phoneNumber: '7980-3003900', message: 'This is your code 9039',
    };
    try {
      createPushNotificationsJobs(lists, queue);
    } catch (error) {
      assert.equal(error.message, 'Jobs is not an array');
      assert(error instanceof Error);
      done();
    }
  }));
});
