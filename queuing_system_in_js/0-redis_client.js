import redis from 'redis';

// Crée un client Redis
const client = redis.createClient();

// Événement déclenché lorsque le client se connecte avec succès au serveur Redis
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Événement déclenché lorsque le client ne parvient pas à se connecter au serveur Redis
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
