import kue from 'kue';

// Créer une file d'attente Kue
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }

// Écouter les nouveaux travaux dans la file d'attente "push_notification_code"
queue.process('push_notification_code', (job, done) => {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message);
	done();
  });
