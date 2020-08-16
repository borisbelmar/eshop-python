from config.database import get_connection
from flask import abort
import bcrypt
import mysql.connector

def customer_register(customer):
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