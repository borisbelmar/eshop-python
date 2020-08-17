from config.database import get_connection
from models.CategorySchema import CategorySchema

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

def get_all_categories():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, description, created_at, updated_at FROM categories')
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    categories = []
    for item in rows:
        categories.append(
            dict(
                id=item[0],
                name=item[1],
                description=item[2],
                created_at=item[3],
                updated_at=item[4]
            )
        )
    return categories_schema.dump(categories)

def get_category_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, description, created_at, updated_at FROM categories WHERE id = %s', (id,))
    category = cursor.fetchone()
    cursor.close()
    connection.close()
    return category

def insert_category(name, description):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'INSERT INTO categories (name, description) VALUES (%s, %s)'
        cursor.execute(stmt, (name, description))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except: 
        cursor.close()
        connection.close()
        return False

def delete_category(id):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'DELETE FROM categories WHERE id = %s'
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

def update_category(id, name, description):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'UPDATE categories SET updated_at = CURRENT_TIMESTAMP, name = %s, description = %s  WHERE id = %s'
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