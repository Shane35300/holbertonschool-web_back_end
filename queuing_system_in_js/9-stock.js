// Liste des produits
const listProducts = [
	{ id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
	{ id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
	{ id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
	{ id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Fonction pour obtenir un produit par ID
function getItemById(id) {
	return listProducts.find(product => product.id === id);
}

import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// Initialisation du serveur Express
const app = express();
const port = 1245;

// Connexion à Redis
const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

// Fonction pour réserver du stock
async function reserveStockById(itemId, stock) {
	await setAsync(`item.${itemId}`, stock);
}

// Fonction pour obtenir le stock réservé actuel
async function getCurrentReservedStockById(itemId) {
	const reservedStock = await getAsync(`item.${itemId}`);
	return reservedStock ? parseInt(reservedStock, 10) : 0;
}

// Route GET /list_products
app.get('/list_products', (req, res) => {
	const formattedProducts = listProducts.map(product => ({
		itemId: product.id,
		itemName: product.name,
		price: product.price,
		initialAvailableQuantity: product.stock
	}));
	res.json(formattedProducts);
});

// Route GET /list_products/:itemId
app.get('/list_products/:itemId', async (req, res) => {
	const itemId = parseInt(req.params.itemId, 10);
	const product = getItemById(itemId);

	if (!product) {
		return res.json({ status: 'Product not found' });
	}

	const reservedStock = await getCurrentReservedStockById(itemId);
	const availableStock = product.stock - reservedStock;

	res.json({
		itemId: product.id,
		itemName: product.name,
		price: product.price,
		initialAvailableQuantity: product.stock,
		currentQuantity: availableStock
	});
});

// Route GET /reserve_product/:itemId
app.get('/reserve_product/:itemId', async (req, res) => {
	const itemId = parseInt(req.params.itemId, 10);
	const product = getItemById(itemId);

	if (!product) {
		return res.json({ status: 'Product not found' });
	}

	const reservedStock = await getCurrentReservedStockById(itemId);
	const availableStock = product.stock - reservedStock;

	if (availableStock <= 0) {
		return res.json({
			status: 'Not enough stock available',
			itemId
		});
	}

	await reserveStockById(itemId, reservedStock + 1);
	res.json({
		status: 'Reservation confirmed',
		itemId
	});
});

// Démarrer le serveur
app.listen(port, () => {
	console.log(`Server listening on port ${port}`);
});
