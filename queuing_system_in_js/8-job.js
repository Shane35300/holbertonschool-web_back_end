import kue from 'kue';

/**
 * Crée des jobs de notifications push dans la queue.
 * @param {Array} jobs - Un tableau d'objets contenant les données des jobs.
 * @param {Object} queue - Une instance de la queue Kue.
 * @throws {Error} - Si le paramètre jobs n'est pas un tableau.
 */
function createPushNotificationsJobs(jobs, queue) {
  // Vérifier si jobs est un tableau
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Créer des jobs pour chaque élément du tableau
  jobs.forEach(jobData => {
    const job = queue.create('push_notification_code_3', jobData);

    // Ajouter un écouteur pour le log de la création du job
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });

    // Ajouter un écouteur pour le log de l'achèvement du job
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Ajouter un écouteur pour le log de l'échec du job
    job.on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    // Ajouter un écouteur pour le log de la progression du job
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Enregistrer le job dans la queue
    job.save();
  });
}

export default createPushNotificationsJobs;
