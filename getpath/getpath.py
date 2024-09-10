# --Librerías y módulos--
import inspect
from pathlib import Path
import subprocess
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


current_frame = inspect.currentframe()  # Devuelve el marco de pila en el que se está ejecutando la función getPath().
caller_frame = inspect.getouterframes(current_frame, 2)  # Devuelve una lista de marcos de pila externos.
script_name = Path(caller_frame[-1].filename).stem  # Convierte el nombre del archivo en un objeto Path.

OUTPUT_PATH = Path(__file__).parent.parent  # Constante que obtiene una ubicación de la cual empezar a buscar archivos.

# --Función que obtiene la ubicación de las imagenes necesarias para cada módulo del software--
def getPath():
    match script_name:
        case "Login":
            assets_path = OUTPUT_PATH

        case "Register":
            assets_path = OUTPUT_PATH / 'Register_Screen' / 'build' / 'assets' / 'frame0'

        case "Menu":
            assets_path = OUTPUT_PATH / 'Menu_Screen' / 'build' / 'assets' / 'frame0'

        case "Clients":
            assets_path = OUTPUT_PATH

        case other:
            print("eh?", OUTPUT_PATH)

    return assets_path
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

def register_screen():
    goto_path = OUTPUT_PATH / 'Register.py'  # Obtiene la ubicación del módulo que queramos abrir.
    subprocess.Popen(["python", str(goto_path)])  # Especifica que es un archivo de python y lo abre.

def wipper_menu():
    goto_path = OUTPUT_PATH / 'Menu.py'
    subprocess.Popen(["python", str(goto_path)])  # Mismo accionar en las demas funciones.

def login_screen():
    goto_path = OUTPUT_PATH / 'Login.py'
    subprocess.Popen(["python", str(goto_path)])  # Mismo accionar en las demas funciones.

def clients():
    goto_path = OUTPUT_PATH / 'Clients_Screens' / 'forest-dark'
    pypath = OUTPUT_PATH / 'Clients.py'
    subprocess.Popen(["python", str(pypath)])
