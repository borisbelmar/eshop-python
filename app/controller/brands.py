#TODO: Actualizar get_product_by_id.

from ..config import get_connection
from ..models import BrandSchema

brand_schema = BrandSchema()
brands_schema = BrandSchema(many=True)

def get_all_brands():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, description, created_at, updated_at FROM brands')
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    brands = []
    for item in rows:
        brands.append(
            dict(
                id=item[0],
                name=item[1],
                description=item[2],
                created_at=item[3],
                updated_at=item[4]
            )
        )
    return brands_schema.dump(brands)

def get_brand_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, description, created_at, updated_at FROM brands WHERE id = %s', (id,))
    brand = cursor.fetchone()
    cursor.close()
    connection.close()
    return brand

def insert_brand(name, description):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'INSERT INTO brands (name, description) VALUES (%s, %s)'
        cursor.execute(stmt, (name, description))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except: 
        cursor.close()
        connection.close()
        return False

def delete_brand(id):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'DELETE FROM brands WHERE id = %s'
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

def update_brand(id, name, description):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'UPDATE brands SET updated_at = CURRENT_TIMESTAMP, name = %s, description = %s  WHERE id = %s'
        cursor.execute(stmt, (name, description, id))
        connection.commit()
        row_count = cursor.rowcount
        cursor.close()
        connection.close()
        return row_count > 0
    except: 
        cursor.close()
        connection.close()
        return False