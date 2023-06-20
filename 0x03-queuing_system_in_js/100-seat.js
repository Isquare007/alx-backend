const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');
const express = require('express');
const port = 1245;

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const queue = kue.createQueue();
const app = express();

async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  const currentQuantity = parseInt(seats) || 0;
  return currentQuantity;
}

reserveSeat(50);
let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ "numberOfAvailableSeats": seats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ "status": "Reservation are blocked" });
  }
  const job = queue.create('reserve_seat');
  job.save((err) => {
    if (err) {
      console.log(`Seat reservation job ${job.id} failed: ${err}`);
      res.json({ "status": "Reservation failed" });
    } else {
      console.log(`Seat reservation job ${job.id} completed`);
      res.json({ "status": "Reservation in process" });
    }
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeats();
    if (currentAvailableSeats === 0) {
      reservationEnabled = false;
    } else if (currentAvailableSeats >= 0) {
      await reserveSeat(currentAvailableSeats - 1);
      if (currentAvailableSeats - 1 === 0) reservationEnabled = false;
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
})

app.listen(port, () => {
  console.log(`app listening on port ${port}`);
})