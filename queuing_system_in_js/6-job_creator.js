import kue from 'kue';

// Créer une file d'attente Kue
const queue = kue.createQueue();

// Créer un objet contenant les données du travail
const jobData = {
	phoneNumber: '4153518780',
	message: 'This is the code to verify your account',
};

// Créer un travail dans la file d'attente nommée "push_notification_code"
const job = queue.create('push_notification_code', jobData)
	.save((err) => {
		if (!err) {
			console.log(`Notification job created: ${job.id}`);
		}
	});

// Gérer les événements de succès et d'échec du travail
job.on('complete', () => {
	console.log('Notification job completed');
}).on('failed', () => {
	console.log('Notification job failed');
});
