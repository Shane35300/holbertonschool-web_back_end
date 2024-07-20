import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';
import redis from 'redis';

describe('createPushNotificationsJobs', function () {
	let queue;
	let redisClient;

	beforeEach(function () {
		// Créer une queue Kue en mode test
		queue = kue.createQueue();
		queue.testMode.enter();

		// Initialiser le client Redis
		redisClient = redis.createClient();
	});

	afterEach(function (done) {
		// Quitter le mode test
		queue.testMode.exit();

		// Vider la base de données Redis
		redisClient.flushdb(done);
	});

	it('should display an error message if jobs is not an array', function () {
		expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
	});

	it('should create jobs in the queue', function (done) {
		const list = [
			{ phoneNumber: '4153518780', message: 'Test message 1' },
			{ phoneNumber: '4153518781', message: 'Test message 2' }
		];

		createPushNotificationsJobs(list, queue);

		// Vérifier les jobs dans la queue
		setTimeout(() => {
			const jobs = queue.testMode.jobs;

			expect(jobs.length).to.equal(2);

			expect(jobs[0].type).to.equal('push_notification_code_3');
			expect(jobs[1].type).to.equal('push_notification_code_3');

			done();
		}, 100); // Attendre un peu pour que les jobs soient ajoutés
	});

	it('should throw an error if the jobs parameter is not an array', function () {
		expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
	});
});
