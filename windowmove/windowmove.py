from tkinter import Tk


window = Tk()

# --Función que permite mover si el clic está en los primeros 30 píxeles--
def start_move(event):
    if event.y <= 30:
        window.x = event.x
        window.y = event.y
    else:
        window.x = None
        window.y = None
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Función que detiene el movimiento de la ventana--
def stop_move(event):
    window.x = None
    window.y = None
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Función que mueve la ventana si las coordenadas no son None--
def do_move(event):
    if window.x is not None and window.y is not None:  # Solo mueve si las coordenadas no son None
        deltax = event.x - window.x
        deltay = event.y - window.y
        x = window.winfo_x() + deltax
        y = window.winfo_y() + deltay
        window.geometry(f"+{x}+{y}")
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --