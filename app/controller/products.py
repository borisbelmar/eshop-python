from app.config import get_connection
from app.models import ProductSchema
from flask import abort
import mysql.connector

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

def get_all_products():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, description, price, id_category, id_brand, created_at, updated_at FROM products')
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    products = []
    for item in rows:
        products.append(
            dict(
                id=item[0],
                name=item[1],
                description=item[2],
                price=item[3],
                id_category=item[4],
                id_brand=item[5],
                created_at=item[6],
                updated_at=item[7]
            )
        )
    return products_schema.dump(products)

def get_product_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, description, price, id_category, id_brand, created_at, updated_at FROM products WHERE id = %s', (id,))
    item = cursor.fetchone()
    if item is None:
        abort(404)
    cursor.close()
    connection.close()
    product = dict(
                id=item[0],
                name=item[1],
                description=item[2],
                price=item[3],
                id_category=item[4],
                id_brand=item[5],
                created_at=item[6],
                updated_at=item[7]
            )
    return product_schema.dump(product)

def insert_product(product):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'INSERT INTO products (name, description, price, id_category, id_brand) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(stmt, (product['name'], product['description'], product['price'], product['id_category'], product['id_brand']))
        connection.commit()
        last_row_id = cursor.lastrowid
        product['id'] = last_row_id
        response = { 'message': 'INSERTED', 'record': product }, 201
        cursor.close()
        connection.close()
        return response
    except KeyError as err:
        cursor.close()
        connection.close()
        abort(400)
    except mysql.connector.Error as err:
        cursor.close()
        connection.close()
        print(f'Error: {err.msg}')
        if err.errno == 1452 or err.errno == 1366:
            abort(400)
        else:
            abort(500)
    except:
        cursor.close()
        connection.close()
        abort(500)


def remove_product(id):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'DELETE FROM products WHERE id = %s'
        cursor.execute(stmt, (id,))
        connection.commit()
        cursor.close()
        connection.close()
        return { 'removed': id }
    except: 
        cursor.close()
        connection.close()
        abort(500)

def update_product(id, product):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'UPDATE products SET updated_at = CURRENT_TIMESTAMP, name = %s, description = %s, price = %s, id_category = %s, id_brand = %s WHERE id = %s'
        cursor.execute(stmt, (
            product['name'],
            product['description'],
            product['price'],
            product['id_category'],
            product['id_brand'],
            id
        ))
        connection.commit()
        row_count = cursor.rowcount
        cursor.close()
        connection.close()
        return { 'rows_affected': row_count }
    except mysql.connector.Error as err:
        cursor.close()
        connection.close()
        print(f'Error: {err.msg}')
        if err.errno == 1452 or err.errno == 1366:
            abort(400)
        else:
            abort(500)
    except:
        cursor.close()
        connection.close()
        abort(500)