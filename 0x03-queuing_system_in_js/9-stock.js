import express from 'express';
import redis from 'redis';
import util from 'util';

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

const getItemById = (id) => {
  return listProducts.find(product => product.itemId === id);
}

const client = redis.createClient();

const getAsync = util.promisify(client.get).bind(client);
const setAsync = util.promisify(client.set).bind(client);

const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
}

const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : null;
}

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = currentStock !== null ? currentStock : product.initialAvailableQuantity;

  res.json({
    itemId: product.itemId,
    itemName: product.itemName,
    price: product.price,
    initialAvailableQuantity: product.initialAvailableQuantity,
    currentQuantity: currentQuantity,
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = currentStock !== null ? currentStock : product.initialAvailableQuantity;

  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: product.itemId });
  }

  await reserveStockById(itemId, currentQuantity - 1);
  res.json({ status: 'Reservation confirmed', itemId: product.itemId });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
