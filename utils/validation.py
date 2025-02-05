def validate_customer_data(data):
    # Validar que los campos necesarios estén presentes
    if not data.get('FirstName') or not data.get('LastName') or not data.get('Email') or not data.get('PhoneNumber') or not data.get('Address'):
        return False, "All fields (FirstName, LastName, Email, PhoneNumber, Address) are required"
    
    # Validar que el correo electrónico tenga un formato válido
    if '@' not in data['Email']:
        return False, "Invalid email format"

    # Validar que el número de teléfono sea válido (aquí puedes agregar más reglas)
    if len(data['PhoneNumber']) != 10:
        return False, "Phone number must be 10 digits"
    
    return True, "Data is valid"
