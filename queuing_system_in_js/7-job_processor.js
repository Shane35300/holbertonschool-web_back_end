import kue from 'kue';

// Tableau des numéros de téléphone blacklistés
const blacklistedNumbers = ['4153518780', '4153518781'];

// Fonction pour envoyer la notification
function sendNotification(phoneNumber, message, job, done) {
	// Suivre la progression du travail à 0%
	job.progress(0, 100);

	// Vérifier si le numéro de téléphone est blacklisté
	if (blacklistedNumbers.includes(phoneNumber)) {
		done(new Error(`Phone number ${phoneNumber} is blacklisted`));
		return;
	}

	// Simuler un délai pour la progression à 50%
	job.progress(50, 100);

	// Loguer l'envoi de la notification
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

	// Terminer le travail avec succès
	done();
}

// Créer une file d'attente Kue
const queue = kue.createQueue();

// Définir le traitement des travaux de la file d'attente push_notification_code_2
queue.process('push_notification_code_2', 2, (job, done) => {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message, job, done);
});

