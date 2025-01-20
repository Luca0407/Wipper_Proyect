# --Librerías y módulos--
import inspect
from pathlib import Path
import subprocess
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


current_frame = inspect.currentframe()  # Devuelve el marco de pila en el que se está ejecutando el modulo getpath.
caller_frame = inspect.getouterframes(current_frame, 2)  # Devuelve una lista de marcos de pila externos.
script_name = Path(caller_frame[-1].filename).stem  # Convierte el nombre del archivo en un objeto Path.
OUTPUT_PATH = Path(__file__).parent.parent  # Constante que obtiene una ubicación de la cual empezar a buscar archivos.
# --Función que obtiene la ubicación de las imagenes necesarias para cada módulo del software--
def getPath():
    match script_name:
        case "Login":
            assets_path = OUTPUT_PATH / 'Login_Screen' / 'build' / 'assets' / 'frame0'

        case "Register":
            assets_path = OUTPUT_PATH / 'Register_Screen' / 'build' / 'assets' / 'frame0'

        case "Menu":
            assets_path = OUTPUT_PATH / 'Menu_Screen' / 'build' / 'assets' / 'frame0'

        case "Clients":
            assets_path = OUTPUT_PATH
        
        case "Products":
            assets_path = OUTPUT_PATH

        case "Records":
            assets_path = OUTPUT_PATH

    return assets_path
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

def vxl(screen):
    if screen in {"Register", "Menu", "Login", "Clients", "Products", "Records"}:
        goto_path = OUTPUT_PATH / f'{screen}.py'
        subprocess.Popen(["python", str(goto_path)])
