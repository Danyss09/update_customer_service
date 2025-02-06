import pymysql
import requests
from services.db_config import get_connection

def read_customer(customer_id):
    url = f"http://54.84.180.78:5000/get_customer/{customer_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def update_customer(customer_id, data):
    connection = get_connection()
    try:
        # Obtener los datos actuales del cliente
        existing_customer = read_customer(customer_id)
        if not existing_customer:
            return None  # Cliente no encontrado

        with connection.cursor() as cursor:
            # SQL para actualizar un cliente de la base de datos
            update_query = """
            UPDATE Customers
            SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s, Address = %s, UpdatedAt = CURRENT_TIMESTAMP
            WHERE CustomerID = %s
            """
            cursor.execute(update_query, (
                data.get('FirstName', existing_customer['FirstName']),
                data.get('LastName', existing_customer['LastName']),
                data.get('Email', existing_customer['Email']),
                data.get('PhoneNumber', existing_customer['PhoneNumber']),
                data.get('Address', existing_customer['Address']),
                customer_id
            ))
            connection.commit()

            if cursor.rowcount == 0:
                return None  # No se actualizó ningún cliente

            # Recuperamos el cliente actualizado
            cursor.execute("SELECT * FROM Customers WHERE CustomerID = %s", (customer_id,))
            updated_customer = cursor.fetchone()
            return updated_customer
    except Exception as e:
        print(f"Error updating customer: {e}")
        return None
    finally:
        connection.close()
