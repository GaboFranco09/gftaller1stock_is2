from flask import Blueprint, request, jsonify
from firebase_admin import db

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/stock/<string:producto_id>', methods=['GET'])
def verificar_stock(producto_id):
    ref = db.reference(f'productos/{producto_id}')
    producto = ref.get()

    if not producto:
        return jsonify({'disponible': 0}), 404

    cantidad_solicitada = int(request.args.get('cantidad', 1))
    disponible = 1 if producto['stock'] >= cantidad_solicitada else 0

    return jsonify({'disponible': disponible}), 200


@stock_bp.route('/stock/<string:producto_id>', methods=['PATCH'])
def actualizar_stock(producto_id):
    ref = db.reference(f'productos/{producto_id}')
    producto = ref.get()

    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404

    cantidad = int(request.args.get('cantidad', 1))

    if producto['stock'] < cantidad:
        return jsonify({'error': 'Sin stock suficiente'}), 400

    producto['stock'] -= cantidad
    ref.set(producto)

    return jsonify({
        'mensaje':      'Stock actualizado',
        'stock_actual': producto['stock']
    }), 200