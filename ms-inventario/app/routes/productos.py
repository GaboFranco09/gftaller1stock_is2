from flask import Blueprint, request, jsonify

productos_bp = Blueprint('productos', __name__)

# Simulamos una base de datos en memoria por ahora
# Cuando conectemos Firebase, esto cambia
productos = {}
contador_id = 1

@productos_bp.route('/productos', methods=['GET'])
def get_productos():
    return jsonify(list(productos.values())), 200

@productos_bp.route('/productos/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    producto = productos.get(producto_id)
    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404
    return jsonify(producto), 200

@productos_bp.route('/productos', methods=['POST'])
def create_producto():
    global contador_id
    data = request.get_json()

    if not data or 'nombre' not in data or 'stock' not in data:
        return jsonify({'error': 'nombre y stock son requeridos'}), 400

    producto = {
        'id':     contador_id,
        'nombre': data['nombre'],
        'precio': data.get('precio', 0),
        'stock':  int(data['stock'])
    }

    productos[contador_id] = producto
    contador_id += 1

    return jsonify(producto), 201