from config.database import get_connection

def get_all_products():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return products

def get_product_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products WHERE id = %s', (id,))
    product = cursor.fetchone()
    cursor.close()
    connection.close()
    return product

def insert_product(name, description, price, id_category, id_brand):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'INSERT INTO products (name, description, price, id_category, id_brand) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(stmt, (name, description, price, id_category, id_brand))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except: 
        cursor.close()
        connection.close()
        return False

def delete_product(id):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'DELETE FROM products WHERE id = %s'
        cursor.execute(stmt, (id,))
        connection.commit()
        row_count = cursor.rowcount
        cursor.close()
        connection.close()
        return row_count > 0
    except: 
        cursor.close()
        connection.close()
        return False

def update_product(id, name, description, price, id_category, id_brand):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'UPDATE products SET updated_at = CURRENT_TIMESTAMP, name = %s, description = %s, price = %s, id_category = %s, id_brand = %s WHERE id = %s'
        cursor.execute(stmt, (name, description, price, id_category, id_brand, id))
        connection.commit()
        row_count = cursor.rowcount
        cursor.close()
        connection.close()
        return row_count > 0
    except: 
        cursor.close()
        connection.close()
        return False