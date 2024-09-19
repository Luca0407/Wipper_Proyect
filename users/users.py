import sqlite3  # Importa librería


connect = sqlite3.connect('wipper.db')  # Crea la conexión a la base de datos.
cursor = connect.cursor()  # Crea un cursor para ejecutar consultas SQL.

# --Función para registrar usuarios--
def register(entry1, entry2, entry3):
    user = cursor.execute("""INSERT INTO users ('name', 'passwd', 'mail', 'active')
                        VALUES (?, ?, ?, ?)""", (entry1, entry2, entry3, 0))
    connect.commit()
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Función para revisar usuario y correo--
def check(entry1, entry2):
    user = cursor.execute("SELECT name, mail FROM users")
    users_reg = user.fetchall()
    user_data = (entry1, entry2)
    for entry in users_reg:
        if entry == user_data:
            return True

    else:
        return False
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Función para iniciar sesión con la cuenta de un determinado usuario--
def login(entry1, entry2):
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
    cursor.execute("SELECT name FROM users WHERE active = 1")
    username = cursor.fetchone()
    return username[0]

def logout(name):
    cursor.execute(f"UPDATE users SET active = 0 WHERE name = '{name}'")
    connect.commit()
