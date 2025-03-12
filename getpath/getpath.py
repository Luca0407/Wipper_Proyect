# --Librerías y módulos--
import inspect
from pathlib import Path
import subprocess
from tkinter import PhotoImage
import sys
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


def get_script_name():
    return Path(sys.argv[0]).stem

current_frame = inspect.currentframe()  # Devuelve el marco de pila en el que se está ejecutando el modulo getpath.
caller_frame = inspect.getouterframes(current_frame, 2)  # Devuelve una lista de marcos de pila externos.
script_name = get_script_name()  # Convierte el nombre del archivo en un objeto Path.
OUTPUT_PATH = Path(__file__).parent.parent  # Constante que obtiene una ubicación de la cual empezar a buscar archivos.
# --Función que obtiene la ubicación de las imagenes necesarias para cada módulo del software--
def getPath():
    assets_path = None
    
    if getattr(sys, 'frozen', False):  # Si está congelado con cx_Freeze
        base_path = Path(sys.executable).parent  # Carpeta donde está el ejecutable
    else:
        base_path = Path(__file__).parent

    match script_name:
        case "Login":
            assets_path = OUTPUT_PATH / 'Login_Screen' / 'build' / 'assets' / 'frame0'
            return assets_path

        case "Register":
            assets_path = OUTPUT_PATH / 'Register_Screen' / 'build' / 'assets' / 'frame0'
            return assets_path

        case "Menu":
            assets_path = OUTPUT_PATH / 'Menu_Screen' / 'build' / 'assets' / 'frame0'
            return assets_path

        case "testing":
            assets_path = OUTPUT_PATH / 'Menu_Screen' / 'build' / 'assets' / 'frame0'
            return assets_path
        
        case "Clients":
            assets_path = OUTPUT_PATH
            return assets_path
        
        case "Products":
            assets_path = OUTPUT_PATH
            return assets_path

        case "Records":
            assets_path = OUTPUT_PATH
            return assets_path
        
        case _:
            print(f"⚠ Advertencia: script_name '{script_name}' no reconocido. Usando ruta por defecto.")
            assets_path = OUTPUT_PATH  # Ruta predeterminada para evitar errores

    if assets_path is None:
        raise ValueError(f"Error crítico: No se encontró ruta para '{script_name}'.")

    return assets_path

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

def cambiar_imagen_boton(btn, image_type, button_key, button_images):
    if image_type == "alternative":
        btn.configure(image=button_images[button_key]["alternative"])
    else:
        btn.configure(image=button_images[button_key]["original"])

def vxl(screen):
    if screen in {"Register", "Menu", "Login", "Clients", "Products", "Records", "testing"}:
        goto_path = OUTPUT_PATH / f'{screen}.py'
        process = subprocess.Popen(["python", str(goto_path)])

# Función vxl que ejecuta un tercer archivo Python
def vxl_button(screen, btn, button_images, button_key):
    if screen in {"Register", "Menu", "Login", "Clients", "Products", "Records"}:
        cambiar_imagen_boton(btn, "alternative", button_key, button_images)  # Cambiar la imagen del botón
        
        # Actualizar la interfaz inmediatamente (esto es importante para que el cambio de imagen se vea)
        btn.master.update()
    
        goto_path = OUTPUT_PATH / f'{screen}.py'
        process = subprocess.Popen(["python", str(goto_path)])

        process.wait()  # Esperamos a que el proceso termine
        
        # Restaurar la imagen después de que el proceso haya terminado
        cambiar_imagen_boton(btn, "original", button_key, button_images)
        
