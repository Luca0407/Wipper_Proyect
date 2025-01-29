import sqlite3
from contextlib import closing

# Ruta a la base de datos
DATABASE_PATH = 'wipper.db'

# Función para obtener una conexión a la base de datos
def get_connection():
    return sqlite3.connect(DATABASE_PATH)


# Función genérica para ejecutar consultas de selección (SELECT)
def fetch_all(query):
    with closing(get_connection()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(query)
        return cursor.fetchall()

def fetch_all2(query, params=()):  # cambiar nombre
    with closing(get_connection()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(query, params)
        return cursor.fetchall()

# Función genérica para ejecutar consultas de modificación (INSERT, UPDATE, DELETE)
def other_queries(query, params=()):
    with closing(get_connection()) as conn, closing(conn.cursor()) as cursor:
        try:
            cursor.execute(query, params)
            conn.commit()
        except sqlite3.DatabaseError as e:
            conn.rollback()
            print(f"Error en la base de datos: {e}")

