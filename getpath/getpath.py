# --Librerías y módulos--
import inspect
from pathlib import Path
import subprocess
from tkinter import PhotoImage
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

def cambiar_imagen_boton(btn, image_type, button_key, button_images):
    if image_type == "alternative":
        btn.configure(image=button_images[button_key]["alternative"])
        print(f"Cambiando imagen de {button_key} a alternativa")  # Agregar para verificar
    else:
        btn.configure(image=button_images[button_key]["original"])
        print(f"Cambiando imagen de {button_key} a original")  # Agregar para verificar

# Función vxl que ejecuta un tercer archivo Python
def vxl(screen, btn, button_images, button_key):
    print(f"Iniciando vxl para la pantalla: {screen}")  # Agregar para verificar
    if screen in {"Register", "Menu", "Login", "Clients", "Products", "Records"}:
        # Cambiar la imagen a "alternative" antes de ejecutar el archivo
        cambiar_imagen_boton(btn, "alternative", button_key, button_images)  # Cambiar la imagen del botón
        
        # Actualizar la interfaz inmediatamente (esto es importante para que el cambio de imagen se vea)
        btn.master.update()

        # Ejecutar el tercer archivo de forma asíncrona
        goto_path = OUTPUT_PATH / f'{screen}.py'
        print(f"Ejecutando archivo: {goto_path}")  # Agregar para verificar
        process = subprocess.Popen(["python", str(goto_path)])
        
        # Usamos after() para cambiar la imagen de vuelta a la original después de un retraso
        process.wait()  # Esperamos a que el proceso termine
        print("Proceso terminado. Restaurando la imagen original.")
        
        # Restaurar la imagen después de que el proceso haya terminado
        cambiar_imagen_boton(btn, "original", button_key, button_images)