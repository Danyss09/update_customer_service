import pymysql
from services.db_config import get_connection

def update_customer(customer_id, data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # SQL para actualizar un cliente de la base de datos
            update_query = """
            UPDATE Customers
            SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s, Address = %s, UpdatedAt = CURRENT_TIMESTAMP
            WHERE CustomerID = %s
            """
            cursor.execute(update_query, (data['FirstName'], data['LastName'], data['Email'], data['PhoneNumber'], data['Address'], customer_id))
            connection.commit()

            # Verificamos si se actualizó algún registro
            if cursor.rowcount == 0:
                return None  # Si no se actualizó ningún cliente

            # Recuperamos el cliente actualizado
            cursor.execute("SELECT * FROM Customers WHERE CustomerID = %s", (customer_id,))
            updated_customer = cursor.fetchone()
            return updated_customer
    except Exception as e:
        print(f"Error updating customer: {e}")
        return None
    finally:
        connection.close()
