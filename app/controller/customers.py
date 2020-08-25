from flask import abort
import bcrypt
import mysql.connector
import marshmallow

from app.config import get_connection
from app.utils import generate_token
from app.models import CustomerSchema

customer_schema = CustomerSchema()

def customer_register(customer):
    try:
        customer_schema.load(customer)
        hashed_password = bcrypt.hashpw(customer['password'].encode('utf-8'), bcrypt.gensalt())
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'INSERT INTO customers (email, password, firstname, lastname, birth) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(stmt, (
            customer['email'],
            hashed_password.decode('utf-8'),
            customer['firstname'],
            customer['lastname'],
            customer['birth']
        ))
        connection.commit()
        last_row_id = cursor.lastrowid
        customer['password'] = hashed_password.decode('utf-8')
        customer['id'] = last_row_id
        response = { 'message': 'REGISTERED', 'record': customer }, 201
        cursor.close()
        connection.close()
        return response
    except KeyError:
        cursor.close()
        connection.close()
        abort(400)
    except mysql.connector.Error as err:
        cursor.close()
        connection.close()
        if err.errno == 1062:
            abort(409)
        if err.errno == 1452 or err.errno == 1366:
            abort(400)
        else:
            abort(500)
        raise Exception(err)
    except marshmallow.exceptions.ValidationError:
        abort(400)
    except:
        cursor.close()
        connection.close()
        abort(500)

def customer_login(email, password):
    connection = get_connection()
    cursor = connection.cursor()
    stmt = 'SELECT id, email, password, active FROM customers WHERE email = %s'
    cursor.execute(stmt, (email,))
    row = cursor.fetchone()
    if row is None:
        abort(403)
    is_valid = bcrypt.checkpw(password.encode('utf-8'), row[2].encode('utf-8'))
    if is_valid:
        token = generate_token({ 'sub': row[0], 'active': row[3] })
    else:
        abort(403)
    cursor.close()
    connection.close()
    return { 'accessToken': token.decode('utf-8') }

def customer_info(id):
    connection = get_connection()
    cursor = connection.cursor()
    stmt = 'SELECT id, email, firstname, lastname, birth, active, created_at, updated_at FROM customers WHERE id = %s'
    cursor.execute(stmt, (id,))
    row = cursor.fetchone()
    if row is None:
        abort(404)
    else:
        return dict(
                id=row[0],
                email=row[1],
                firstname=row[2],
                lastname=row[3],
                birth=row[4],
                active=row[5],
                created_at=row[6],
                updated_at=row[7]
            )