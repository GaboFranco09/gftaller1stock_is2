const express = require('express');
const dotenv  = require('dotenv');

dotenv.config();

const app  = express();
const PORT = process.env.EXPRESS_PORT || 5002;

app.use(express.json());

// Rutas
const ventasRoutes = require('./routes/ventas');
app.use('/ventas', ventasRoutes);

// Ruta de salud
app.get('/health', (req, res) => {
    res.json({ status: 'ok', servicio: 'ms-ventas' });
});

app.listen(PORT, () => {
    console.log(`MS Ventas corriendo en puerto ${PORT}`);
});