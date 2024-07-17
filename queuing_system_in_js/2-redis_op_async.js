import redis from 'redis';
import { promisify } from 'util';


// Crée un client Redis
const client = redis.createClient();

// Convertir les fonctions Redis basées sur des callbacks en fonctions renvoyant des promesses
const getAsync = promisify(client.get).bind(client);


// Fonction pour définir une nouvelle valeur pour une clé donnée
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Fonction asynchrone pour afficher la valeur d'une clé
async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.error(err);
  }
}

// Événement déclenché lorsque le client se connecte avec succès au serveur Redis
client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
});

// Événement déclenché lorsque le client ne parvient pas à se connecter au serveur Redis
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
