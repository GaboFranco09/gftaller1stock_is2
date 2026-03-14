const express = require('express');
const router  = express.Router();
const Venta   = require('../models/Venta');

router.get('/', async (req, res) => {
    try {
        const ventas = await Venta.find();
        res.json(ventas);
    } catch (err) {
        res.status(500).json({ error: 'Error al obtener ventas' });
    }
});

router.get('/:id', async (req, res) => {
    try {
        const venta = await Venta.findById(req.params.id);
        if (!venta) {
            return res.status(404).json({ error: 'Venta no encontrada' });
        }
        res.json(venta);
    } catch (err) {
        res.status(500).json({ error: 'Error al obtener venta' });
    }
});

router.get('/usuario/:usuario_id', async (req, res) => {
    try {
        const ventas = await Venta.find({ usuario_id: req.params.usuario_id });
        res.json(ventas);
    } catch (err) {
        res.status(500).json({ error: 'Error al obtener ventas' });
    }
});

router.get('/fecha/:fecha', async (req, res) => {
    try {
        const ventas = await Venta.find({ fecha: req.params.fecha });
        res.json(ventas);
    } catch (err) {
        res.status(500).json({ error: 'Error al obtener ventas' });
    }
});

// POST /ventas — registrar una venta
router.post('/', async (req, res) => {
    try {
        const { usuario_id, producto_id, cantidad, precio_total } = req.body;

        if (!usuario_id || !producto_id || !cantidad || !precio_total) {
            return res.status(400).json({ error: 'Faltan campos requeridos' });
        }

        const venta = new Venta({ usuario_id, producto_id, cantidad, precio_total });
        await venta.save();

        res.status(201).json(venta);
    } catch (err) {
        res.status(500).json({ error: 'Error al registrar venta' });
    }
});

module.exports = router;