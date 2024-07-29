# Módulo provisorio mientras se trabaja en la base de datos.
TXT_NAME = "userpass.txt"  # Apunta a un archivo .txt

def getMail(entry):
    with open(TXT_NAME, 'a') as file:  # Abre el archivo con la accion 'a' (add).
        file.write(f"\n{entry}")  # Escribe dentro el valor del parámetro entry.

def getUser(entry):
    with open(TXT_NAME, 'a') as file:
        file.write(f"\n{entry}")  # Mismo accionar en las demas funciones.

def getPass(entry):
    with open(TXT_NAME, 'a') as file:
        file.write(f"\n{entry}")  # Mismo accionar en las demas funciones.

# --Función para llamar a las demas funciones y agregar los valores al archivo--
def register(entry1, entry2, entry3): 
    getMail(entry1)
    getUser(entry2)
    getPass(entry3)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
