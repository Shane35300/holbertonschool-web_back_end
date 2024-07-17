import redis from 'redis';

// Crée un client Redis
const client = redis.createClient();


// Fonction pour définir une nouvelle valeur pour une clé donnée
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Fonction pour afficher la valeur d'une clé
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log(reply);
    }
  });
}

// Événement déclenché lorsque le client se connecte avec succès au serveur Redis
client.on('connect', () => {
  console.log('Redis client connected to the server');
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
});

// Événement déclenché lorsque le client ne parvient pas à se connecter au serveur Redis
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
