import redis from 'redis';


const client = redis.createClient();

// Événement déclenché lorsque le client se connecte avec succès au serveur Redis
client.on('connect', () => {
	console.log('Redis client connected to the server');

	client.hset('HolbertonSchools', 'Portland', 50, (err, reply) => {
		if (err) throw err;
		redis.print(err, reply);

		client.hset('HolbertonSchools', 'Seattle', 80, (err, reply) => {
			if (err) throw err;
			redis.print(err, reply);

			client.hset('HolbertonSchools', 'New York', 20, (err, reply) => {
				if (err) throw err;
				redis.print(err, reply);

				client.hset('HolbertonSchools', 'Bogota', 20, (err, reply) => {
					if (err) throw err;
					redis.print(err, reply);

					client.hset('HolbertonSchools', 'Cali', 40, (err, reply) => {
						if (err) throw err;
						redis.print(err, reply);

						client.hset('HolbertonSchools', 'Paris', 2, (err, reply) => {
							if (err) throw err;
							redis.print(err, reply);

							client.hgetall('HolbertonSchools', (err, reply) => {
								if (err) throw err;
								console.log(reply);
							});
						});
					});
				});
			});
		});
	});
});

// Événement déclenché lorsque le client ne parvient pas à se connecter au serveur Redis
client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});
