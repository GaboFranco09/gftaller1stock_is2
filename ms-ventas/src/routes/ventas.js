const express = require('express');
const router  = express.Router();

// Base de datos en memoria — temporal hasta conectar MongoDB
let ventas     = [];
let contadorId = 1;


router.get('/', (req, res) => {
    res.json(ventas);
});


router.get('/:id', (req, res) => {
    const venta = ventas.find(v => v.id === parseInt(req.params.id));
    if (!venta) {
        return res.status(404).json({ error: 'Venta no encontrada' });
    }
    res.json(venta);
});

// ventas por usuario
router.get('/usuario/:usuario_id', (req, res) => {
    const ventasUsuario = ventas.filter(v => v.usuario_id === req.params.usuario_id);
    res.json(ventasUsuario);
});

// ventas por fecha
router.get('/fecha/:fecha', (req, res) => {
    const ventasFecha = ventas.filter(v => v.fecha === req.params.fecha);
    res.json(ventasFecha);
});

//registrar una venta
router.post('/', (req, res) => {
    const { usuario_id, producto_id, cantidad, precio_total } = req.body;

    if (!usuario_id || !producto_id || !cantidad || !precio_total) {
        return res.status(400).json({ error: 'Faltan campos requeridos' });
    }

    const venta = {
        id:          contadorId++,
        usuario_id:  usuario_id,
        producto_id: producto_id,
        cantidad:    cantidad,
        precio_total: precio_total,
        fecha:       new Date().toISOString().split('T')[0]
    };

    ventas.push(venta);
    res.status(201).json(venta);
});

module.exports = router;