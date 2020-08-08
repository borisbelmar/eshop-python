from mysql.connector import connect

CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'port': 9998,
    'database': 'eshop',
    'auth_plugin': 'mysql_native_password'
}

# Función para conectar a la base de datos
def get_connection():
    return connect(
        host = CONFIG['host'],
        user = CONFIG['user'],
        password = CONFIG['password'],
        port = CONFIG['port'],
        database = CONFIG['database'],
        auth_plugin = CONFIG['auth_plugin']
    )