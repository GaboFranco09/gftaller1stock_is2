const mongoose = require('mongoose');

const ventaSchema = new mongoose.Schema({
    usuario_id:   { type: String, required: true },
    producto_id:  { type: String, required: true },
    cantidad:     { type: Number, required: true },
    precio_total: { type: Number, required: true },
    fecha:        { type: String, default: () => new Date().toISOString().split('T')[0] }
});

module.exports = mongoose.model('Venta', ventaSchema);