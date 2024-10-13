# --Librerías y módulos--
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from getpath import getpath as gp
from users import users
from time import strftime
import sys
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


window = Tk()
PATH = gp.getPath()
username = users.current_user()
if username is None:
    window.destroy()
    gp.vxl("Login")
    sys.exit()
    

def relative_to_assets(path: str) -> Path:
    return PATH / Path(path)


# --- Movimiento de la ventana ---
def start_move(event):
    if event.y <= 30:
        window.x = event.x
        window.y = event.y
    else:
        window.x = None
        window.y = None

def do_move(event):
    if window.x is not None and window.y is not None:
        deltax = event.x - window.x
        deltay = event.y - window.y
        x = window.winfo_x() + deltax
        y = window.winfo_y() + deltay
        window.geometry(f"+{x}+{y}")
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Fecha y hora ---
def update_clock(canvas, clock_text):
    current_time = strftime('%H:%M')  # Obtén la hora actual
    canvas.itemconfig(clock_text, text=current_time)  # Actualiza el texto en el canvas
    canvas.after(1000, update_clock, canvas, clock_text)  # Llama de nuevo después de 1 segundo

def update_date(canvas, date_text):
    current_date = strftime('%d/%m/%y')  # Obtén la hora actual
    canvas.itemconfig(date_text, text=current_date)  # Actualiza el texto en el canvas
    canvas.after(1000, update_date, canvas, date_text)  # Llama de nuevo después de 1 segundo

def goto_commerce():
    window.destroy()
    gp.vxl("Commerce")

# --- Cierre de sesión ---
def logout():
    window.destroy()
    users.logout(username)
    gp.vxl("Login")
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

# --Carga las imágenes de los botones normales y clickeados--
clients_normal = PhotoImage(file=relative_to_assets("clients.png"))
clients_clicked = PhotoImage(file=relative_to_assets("clients_clicked.png"))

records_normal = PhotoImage(file=relative_to_assets("records.png"))
records_clicked = PhotoImage(file=relative_to_assets("records_clicked.png"))

products_normal = PhotoImage(file=relative_to_assets("products.png"))
products_clicked = PhotoImage(file=relative_to_assets("products_clicked.png"))

# Variables para mantener el estado del botón actual
current_button = None
current_image = None

def change_button_image(button, normal_image, clicked_image):
    global current_button, current_image
    
    # Cambia la imagen del botón clickeado
    button.config(image=clicked_image)
    
    # Si hay un botón actualmente seleccionado, reestablece su imagen
    if current_button and current_button != button:
        current_button.config(image=current_image)
    
    # Actualiza el botón actual
    current_button = button
    current_image = normal_image  # Guarda la imagen normal del botón actual

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
# --Crea y posiciona el fondo--
bg = PhotoImage(
    file=relative_to_assets("background.png"))
bg_menu = canvas.create_image(
    680.0,
    404.0,
    image=bg
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona el logo decorativo (transparente)--
logo_watermark = PhotoImage(
    file=relative_to_assets("watermark.png"))

background_logo = canvas.create_image(
    499.0,
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

time_img = canvas.create_image(
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
    x=1125.0,
    y=50.0,
    width=190.0,
    height=60.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona --
records_button = PhotoImage(
    file=relative_to_assets("records.png"))

records = Button(
    image=records_normal,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [
        change_button_image(records, records_normal, records_clicked), 
        gp.vxl("Records")
    ],
    relief="flat"
)

records.place(
    x=855.0,
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
    command=lambda: goto_commerce(),
    relief="flat"
)

commerce.place(
    x=45.0,
    y=50.0,
    width=190.0,
    height=60.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# --Crea y posiciona --
clients_button = PhotoImage(
    file=relative_to_assets("clients.png"))

clients = Button(
    image=clients_normal,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [
        change_button_image(clients, clients_normal, clients_clicked), 
        gp.vxl("Clients")
    ],
    relief="flat"
)

clients.place(
    x=315.0,
    y=50.0,
    width=190.0,
    height=60.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona --
products_button = PhotoImage(
    file=relative_to_assets("products.png"))

products = Button(
    image=products_normal,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [
        change_button_image(products, products_normal, products_clicked), 
        gp.vxl("Products")
    ],
    relief="flat"
)

products.place(
    x=585.0,
    y=50.0,
    width=190.0,
    height=60.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# --Crea y posiciona teclas rapidas--
canvas.create_text(
    726.0,
    356.0,
    anchor="nw",
    text="F2: Abrir Clientes\n\nF3: Abrir Productos\n\nF4: Abrir Registros\n\nF5: Modo Claro/Oscuro",
    fill="#555454",
    font=("Montserrat Bold", 16 * -1)
)

canvas.create_text(
    726.0,
    288.0,
    anchor="nw",
    text="Teclas Rápidas",
    fill="#555454",
    font=("Montserrat Bold", 36 * -1)
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# --Crea y posiciona version--
canvas.create_text(
    14.0,
    657.0,
    anchor="nw",
    text="v0.8.1.1",
    fill="#555454",
    font=("Montserrat Bold", 10 * -1)
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

clock_text = canvas.create_text(
    1295.0,
    695.0,
    anchor="nw",
    text=" ",  # Texto vacío inicialmente
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)

# Inicia la actualización del reloj
update_clock(canvas, clock_text)

date_text = canvas.create_text(
    1151.0,
    695.0,
    anchor="nw",
    text="",  # Texto vacío inicialmente
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)

# Inicia la actualización del reloj
update_date(canvas, date_text)

canvas.create_text(
    44.0,
    695.0,
    anchor="nw",
    text=username,
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# --Se llama a las funciones para interactuar con la ventana--
canvas.bind("<Button-1>", start_move)
canvas.bind("<B1-Motion>", do_move)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# --Funciones para teclas rápidas
def press_clients(event):
    clients.invoke()  # Simula el clic en el botón de clientes

def press_products(event):
    products.invoke()  # Simula el clic en el botón de productos

def press_records(event):
    records.invoke()  # Simula el clic en el botón de registros

# Asignar las teclas F2, F3 y F4 a sus respectivas funciones
window.bind("<F2>", press_clients)
window.bind("<F3>", press_products)
window.bind("<F4>", press_records)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window.resizable(False, False)  # Fija el tamaño de la ventana en ambas posiciones (x, y).
window.mainloop()  # Hace que la ventana se mantenga abierta.