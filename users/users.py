import sqlite3
from db_manager import db_manager as db
from tkinter import messagebox
import re
from strings import strings as txt



queries = txt.queries()

def validate_mail(mail):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'
    return re.match(regex, mail) is not None


def validate_pass(passwd):
    regex = r'^[a-zA-Z0-9_.¿?=/&%^$·"¡!ºª|#~€¬*-]{8,20}$'
    return re.match(regex, passwd) is not None


# --- Función para registrar usuarios ---
def register(entry1, entry2, entry3):
    if "" in (entry1, entry2, entry3):
        return messagebox.showerror("ERROR", "Uno o más campos se encuentran vacíos.")
    else:
        if (validate_mail(entry3) and validate_pass(entry2)) is True:
            values = (entry1, entry2, entry3, 1)
            db.other_queries(queries[8], values)
            return True
        else:
            return messagebox.showerror("ERROR", "Contraseña o correo invalido.")
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --Función para revisar usuario y correo--
def check(entry1, entry2):
    users_reg = db.fetch_all(queries[9])
    for entry in users_reg:
        if entry[0] == entry1 or entry[1] == entry2:
            return True
    else:
        return False
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --Función para iniciar sesión con la cuenta de un determinado usuario--
def login(entry1, entry2):
    connect = sqlite3.connect('wipper.db')  # Crea la conexión a la base de datos.
    cursor = connect.cursor()  # Crea un cursor para ejecutar consultas SQL.
    user = cursor.execute("SELECT name, passwd FROM users")
    usuarios = user.fetchall()
    user_data = (entry1, entry2)
    for entry in usuarios:
        if entry == user_data:
            cursor.execute(f"UPDATE users SET active = 1 WHERE name = '{user_data[0]}'")
            connect.commit()
            return True
        
    else:
        return False
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


def current_user():
    try:
        username = db.fetch_all(queries[10])
        return username[0]
    except Exception as e:
        return


def logout(name):
    db.other_queries(queries[11], name)
    connect = sqlite3.connect('wipper.db')  # Crea la conexión a la base de datos.
    cursor = connect.cursor()  # Crea un cursor para ejecutar consultas SQL.
    cursor.execute(f"UPDATE users SET active = 0 WHERE name = '{name}'")
    connect.commit()
