import redis from 'redis';


const publisher = redis.createClient();
const channelName = 'holberton school channel';

function publishMessage(message, time) {
	setTimeout(() => {
		publisher.publish(channelName, message, (err, reply) => {
			if (err) {
				console.error(err);
			} else {
				console.log(`About to send ${message}`);
			}
		});
	}, time);
}
// Événement déclenché lorsque le client se connecte avec succès au serveur Redis
publisher.on('connect', () => {
	console.log('Redis client connected to the server');
});

// Événement déclenché lorsque le client ne parvient pas à se connecter au serveur Redis
publisher.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
