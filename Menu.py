# --Librerías y módulos--
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from getpath import getpath as gp
from users import users
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


window = Tk()
PATH = gp.getPath()  # Constante PATH obtiene la ubicación donde estan las imágenes.

def relative_to_assets(path: str) -> Path:
    return PATH / Path(path)  # Retorna la ubicación de las imágenes usadas en la ventana.

# --Función que permite mover la ventana si el clic está en los primeros 30 píxeles--
def start_move(event):
    if event.y <= 30:
        window.x = event.x
        window.y = event.y
    else:
        window.x = None
        window.y = None
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --´

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

# --Función para registrar un nuevo usuario--.
def logout():
    window.destroy()
    gp.login_screen()
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window.configure(bg = "#191919")
window.overrideredirect(True)  # Elimina los bordes y decoraciones de la ventana.

# --Centra y posiciona la ventana en pantalla--
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 1360
window_height = 728

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona la ventana--
canvas = Canvas(
    window,
    bg = "#191919",
    height = 728,
    width = 1360,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona el logo decorativo (transparente)--
logo_watermark = PhotoImage(
    file=relative_to_assets("watermark.png"))

background_logo = canvas.create_image(
    678.0,
    392.0,
    image=logo_watermark
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona la barra de titulo--
title_bar = PhotoImage(
    file=relative_to_assets("title_bar.png"))

title = canvas.create_image(
    680.0,
    15.0,
    image=title_bar
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona la barra de menú--
menu_bar = PhotoImage(
    file=relative_to_assets("menu_bar.png"))

menu = canvas.create_image(
    680.0,
    80.0,
    image=menu_bar
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona la barra de estado--
status_bar = PhotoImage(
    file=relative_to_assets("status_bar.png"))

status = canvas.create_image(
    680.0,
    703.0,
    image=status_bar
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona el icono del logo--
logo_icon = PhotoImage(
    file=relative_to_assets("logo_icon.png"))

logo = canvas.create_image(
    28.0,
    15.0,
    image=logo_icon
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona el icono del usuario--
user_icon = PhotoImage(
    file=relative_to_assets("user_icon.png"))

user = canvas.create_image(
    24.0,
    703.0,
    image=user_icon
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona el icono de la fecha--
date_icon = PhotoImage(
    file=relative_to_assets("date_icon.png"))

date = canvas.create_image(
    1131.0,
    703.0,
    image=date_icon
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona el icono de la hora--
time_icon = PhotoImage(
    file=relative_to_assets("time_icon.png"))

time = canvas.create_image(
    1275.0,
    703.0,
    image=time_icon
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona--
minimize_icon = PhotoImage(
    file=relative_to_assets("minimize.png"))

minimize = Button(
    image=minimize_icon,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("minimize clicked"),
    relief="flat"
)

minimize.place(
    x=1281.0,
    y=2.0,
    width=26.0,
    height=26.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona --
close_icon = PhotoImage(
    file=relative_to_assets("close.png"))

close = Button(
    image=close_icon,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)

close.place(
    x=1321.0,
    y=2.0,
    width=26.0,
    height=26.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona --
logout_button = PhotoImage(
    file=relative_to_assets("logout.png"))

logout_b = Button(
    image=logout_button,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: logout(),
    relief="flat"
)

logout_b.place(
    x=1159.0,
    y=50.0,
    width=190.0,
    height=60.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona --
records_button = PhotoImage(
    file=relative_to_assets("records.png"))

records = Button(
    image=records_button,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("records clicked"),
    relief="flat"
)

records.place(
    x=929.0,
    y=50.0,
    width=190.0,
    height=60.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona --
commerce_button = PhotoImage(
    file=relative_to_assets("commerce.png"))

commerce = Button(
    image=commerce_button,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("commerce clicked"),
    relief="flat"
)

commerce.place(
    x=9.0,
    y=50.0,
    width=190.0,
    height=60.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona --
costs_button = PhotoImage(
    file=relative_to_assets("costs.png"))

costs = Button(
    image=costs_button,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("costs clicked"),
    relief="flat"
)

costs.place(
    x=239.0,
    y=50.0,
    width=190.0,
    height=60.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona --
clients_button = PhotoImage(
    file=relative_to_assets("clients.png"))

clients = Button(
    image=clients_button,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gp.clients(),
    relief="flat"
)

clients.place(
    x=469.0,
    y=50.0,
    width=190.0,
    height=60.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona --
products_button = PhotoImage(
    file=relative_to_assets("products.png"))

products = Button(
    image=products_button,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("products clicked"),
    relief="flat"
)

products.place(
    x=699.0,
    y=50.0,
    width=190.0,
    height=60.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --create_text() inserta texto en la ventana segun los parametros que se le den--
canvas.create_text(
    58.0,
    7.0,
    anchor="nw",
    text="Wipper Insumos",
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)

canvas.create_text(
    1295.0,
    695.0,
    anchor="nw",
    text="HH:MM",
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)

canvas.create_text(
    1151.0,
    695.0,
    anchor="nw",
    text="DD/MM/AA",
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)

canvas.create_text(
    44.0,
    695.0,
    anchor="nw",
    text="User",
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --Se llama a las funciones para interactuar con la ventana--
canvas.bind("<Button-1>", start_move)
canvas.bind("<ButtonRelease-1>", stop_move)
canvas.bind("<B1-Motion>", do_move)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window.resizable(False, False)  # Fija el tamaño de la ventana en ambas posiciones (x, y).
window.mainloop()  # Hace que la ventana se mantenga abierta.
