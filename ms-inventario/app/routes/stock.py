from flask import Blueprint, jsonify, request
from app.routes.productos import productos

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/stock/<int:producto_id>', methods=['GET'])
def verificar_stock(producto_id):
    producto = productos.get(producto_id)

    if not producto:
        return jsonify({'disponible': 0}), 404

    cantidad_solicitada = int(request.args.get('cantidad', 1))
    disponible = 1 if producto['stock'] >= cantidad_solicitada else 0

    return jsonify({'disponible': disponible}), 200


@stock_bp.route('/stock/<int:producto_id>', methods=['PATCH'])
def actualizar_stock(producto_id):
    producto = productos.get(producto_id)

    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404

    data = productos[producto_id]
    if data['stock'] <= 0:
        return jsonify({'error': 'Sin stock disponible'}), 400

    productos[producto_id]['stock'] -= 1

    return jsonify({
        'mensaje':   'Stock actualizado',
        'stock_actual': productos[producto_id]['stock']
    }), 200