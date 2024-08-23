import sqlite3  # Importa librería


connect = sqlite3.connect('wipper.db')  # Crea la conexión a la base de datos.
cursor = connect.cursor()  # Crea un cursor para ejecutar consultas SQL.

# --Función para registrar usuarios--
def register(entry1, entry2, entry3):
    user = cursor.execute("""INSERT INTO usuarios ('nombre', 'contra', 'correo')
                        VALUES (?, ?, ?)""", (entry1, entry2, entry3))
    connect.commit()
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Función para iniciar sesión con la cuenta de un determinado usuario--
def login(entry1, entry2):
    user = cursor.execute("SELECT nombre, contra FROM usuarios")
    usuarios = user.fetchall()
    user_data = (entry1, entry2)
    for entry in usuarios:
        if entry == user_data:
            return True
        
    else:
        return False
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
