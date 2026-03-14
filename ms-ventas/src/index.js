const express  = require('express');
const dotenv   = require('dotenv');
const mongoose = require('mongoose');

dotenv.config();

const app  = express();
const PORT = process.env.EXPRESS_PORT || 5002;

app.use(express.json());

// Conexión a MongoDB
mongoose.connect(process.env.MONGODB_URI)
    .then(() => console.log('MongoDB conectado'))
    .catch(err => console.error('Error conectando MongoDB:', err));

// Rutas
const ventasRoutes = require('./routes/ventas');
app.use('/ventas', ventasRoutes);

app.get('/health', (req, res) => {
    res.json({ status: 'ok', servicio: 'ms-ventas' });
});

app.listen(PORT, () => {
    console.log(`MS Ventas corriendo en puerto ${PORT}`);
});