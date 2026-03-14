from flask import Blueprint, request, jsonify
from firebase_admin import db

productos_bp = Blueprint('productos', __name__)
#decorador @ en flask para definir rutas, en este caso la ruta /productos para obtener todos los productos y /productos/<producto_id> para obtener un producto específico. También se define una ruta POST para crear un nuevo producto.
@productos_bp.route('/productos', methods=['GET'])
def get_productos():
    ref = db.reference('productos')
    productos = ref.get()

    if not productos:
        return jsonify([]), 200

    return jsonify(list(productos.values())), 200


@productos_bp.route('/productos/<string:producto_id>', methods=['GET'])
def get_producto(producto_id):
    ref = db.reference(f'productos/{producto_id}')
    producto = ref.get()

    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404

    return jsonify(producto), 200


@productos_bp.route('/productos', methods=['POST'])
def create_producto():
    data = request.get_json()

    if not data or 'nombre' not in data or 'stock' not in data:
        return jsonify({'error': 'nombre y stock son requeridos'}), 400

    ref = db.reference('productos')
    nuevo_ref = ref.push()

    producto = {
        'id':     nuevo_ref.key,
        'nombre': data['nombre'],
        'precio': data.get('precio', 0),
        'stock':  int(data['stock'])
    }

    nuevo_ref.set(producto)

    return jsonify(producto), 201

@productos_bp.route('/productos/<string:producto_id>', methods=['PUT'])
def update_producto(producto_id):
    ref = db.reference(f'productos/{producto_id}')
    producto = ref.get()

    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404

    data = request.get_json()

    if 'nombre' in data:
        producto['nombre'] = data['nombre']
    if 'precio' in data:
        producto['precio'] = data['precio']
    if 'stock' in data:
        producto['stock'] = int(data['stock'])

    ref.set(producto)

    return jsonify(producto), 200


@productos_bp.route('/productos/<string:producto_id>', methods=['DELETE'])
def delete_producto(producto_id):
    ref = db.reference(f'productos/{producto_id}')
    producto = ref.get()

    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404

    ref.delete()

    return jsonify({'mensaje': 'Producto eliminado correctamente'}), 200