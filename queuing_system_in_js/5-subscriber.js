import redis from 'redis';


const subscriber = redis.createClient();
const channelName = 'holberton school channel';

// Événement déclenché lorsque le client se connecte avec succès au serveur Redis
subscriber.on('connect', () => {
	console.log('Redis client connected to the server');
	subscriber.subscribe(channelName);
});

// Événement déclenché lorsque le client ne parvient pas à se connecter au serveur Redis
subscriber.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

subscriber.on('message', (channel, msg) => {
	if (channel === channelName) {
		console.log(msg);
	}
	if (msg === 'KILL_SERVER') {
		subscriber.unsubscribe(channelName, () => {
			subscriber.quit();
		});
	}
})
