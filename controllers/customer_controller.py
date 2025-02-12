from flask import Blueprint, request, jsonify
from models.customer_models import update_customer
from services.db_config import get_connection

customer_controller = Blueprint('customer_controller', __name__)

# Ruta para actualizar un cliente
@customer_controller.route('/update_customer', methods=['PUT'])
def update_customer_route():
    customer_id = request.args.get('customer_id')
    
    if not customer_id:
        return jsonify({'error': 'No customer_id provided'}), 400
    
    # Obtener los datos del cliente a actualizar
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        # Llamamos a la función de actualización
        updated_customer = update_customer(customer_id, data)
        
        if updated_customer:
            return jsonify(updated_customer), 200  # Cliente actualizado con éxito
        else:
            return jsonify({'error': 'Customer not found'}), 404  # Cliente no encontrado
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Error en el servidor
