# --- Librerías y módulos ---
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, messagebox
from getpath import getpath as gp
from users import users
from time import strftime
from strings import strings as txt
import sys
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


window = Tk()
PATH = gp.getPath()
username = users.current_user()
if username is None:
    window.destroy()
    gp.vxl(txt.general()[30])
    sys.exit()


def relative_to_assets(path: str) -> Path:
    return PATH / Path(path)


# --- Movimiento de la ventana ---
def start_move(event):
    if event.y <= 30:
        window.x, window.y = event.x, event.y
    else:
        window.x, window.y = None, None


def do_move(event):
    if window.x is not None and window.y is not None:
        deltax = event.x - window.x
        deltay = event.y - window.y
        x = window.winfo_x() + deltax
        y = window.winfo_y() + deltay
        window.geometry(f"+{x}+{y}")
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --- Fecha y hora ---
def update_clock_and_date(win, clock_text, date_text):
    current_time = strftime(txt.menu()[0])
    win.itemconfig(clock_text, text=current_time)

    current_date = strftime(txt.menu()[1])
    win.itemconfig(date_text, text=current_date)

    win.after(1000, update_clock_and_date, win, clock_text, date_text)  # Llama de nuevo después de 1 segundo

# --- Cierre de sesión ---
def logout():
    window.destroy()
    users.logout(username)
    gp.vxl(txt.general()[30])
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

def center_window(window, width, height):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

window.overrideredirect(True)
center_window(window, 1360, 728)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Carga las imágenes de los botones normales y clickeados--
clients_normal = PhotoImage(file=relative_to_assets(txt.menu()[2]))
clients_clicked = PhotoImage(file=relative_to_assets(txt.menu()[3]))

records_normal = PhotoImage(file=relative_to_assets(txt.menu()[4]))
records_clicked = PhotoImage(file=relative_to_assets(txt.menu()[5]))

products_normal = PhotoImage(file=relative_to_assets(txt.menu()[6]))
products_clicked = PhotoImage(file=relative_to_assets(txt.menu()[7]))

current_button, current_image = None, None

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
    bg = txt.general()[0],
    height = 728,
    width = 1360,
    bd = 0,
    highlightthickness = 0,
    relief = txt.menu()[8])

canvas.place(x = 0, y = 0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --Crea y posiciona el fondo--
bg = PhotoImage(
    file=relative_to_assets(txt.menu()[9]))

bg_menu = canvas.create_image(
    680.0,
    404.0,
    image=bg)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --Crea y posiciona el logo decorativo (transparente)--
logo_watermark = PhotoImage(
    file=relative_to_assets(txt.menu()[10]))

background_logo = canvas.create_image(
    499.0,
    392.0,
    image=logo_watermark
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --Crea y posiciona la barra de titulo--
title_bar = PhotoImage(
    file=relative_to_assets(txt.menu()[11]))

title = canvas.create_image(
    680.0,
    15.0,
    image=title_bar
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --Crea y posiciona la barra de menú--
menu_bar = PhotoImage(
    file=relative_to_assets(txt.menu()[12]))

menu = canvas.create_image(
    680.0,
    80.0,
    image=menu_bar
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --Crea y posiciona la barra de estado--
status_bar = PhotoImage(
    file=relative_to_assets(txt.menu()[13]))

status = canvas.create_image(
    680.0,
    703.0,
    image=status_bar
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --Crea y posiciona el icono del logo--
logo_icon = PhotoImage(
    file=relative_to_assets(txt.menu()[14]))

logo = canvas.create_image(
    28.0,
    15.0,
    image=logo_icon
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --Crea y posiciona el icono del usuario--
user_icon = PhotoImage(
    file=relative_to_assets(txt.menu()[15]))

user = canvas.create_image(
    24.0,
    703.0,
    image=user_icon
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona el icono de la fecha--
date_icon = PhotoImage(
    file=relative_to_assets(txt.menu()[16]))

date = canvas.create_image(
    1131.0,
    703.0,
    image=date_icon
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona el icono de la hora--
time_icon = PhotoImage(
    file=relative_to_assets(txt.menu()[17]))

time_img = canvas.create_image(
    1275.0,
    703.0,
    image=time_icon
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona--
minimize_icon = PhotoImage(
    file=relative_to_assets(txt.menu()[18]))

minimize = Button(
    image=minimize_icon,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("minimize clicked"),
    relief=txt.general()[31]
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
    file=relative_to_assets(txt.menu()[19]))

close = Button(
    image=close_icon,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief=txt.general()[31]
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
    file=relative_to_assets(txt.menu()[20]))

logout_b = Button(
    image=logout_button,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: logout(),
    relief=txt.general()[31]
)

logout_b.place(
    x=1125.0,
    y=50.0,
    width=190.0,
    height=60.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona --
records = Button(
    image=records_normal,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [
        change_button_image(records, records_normal, records_clicked), 
        gp.vxl(txt.menu()[21])
    ],
    relief=txt.general()[31]
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
    file=relative_to_assets(txt.menu()[22]))

commerce = Button(
    image=commerce_button,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: messagebox.showinfo(txt.menu()[23], txt.menu()[24]),
    relief=txt.general()[31]
)

commerce.place(
    x=45.0,
    y=50.0,
    width=190.0,
    height=60.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona --
clients = Button(
    image=clients_normal,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [
        change_button_image(clients, clients_normal, clients_clicked), 
        gp.vxl(txt.menu()[25])
        
    ],
    relief=txt.general()[31]
)

clients.place(
    x=315.0,
    y=50.0,
    width=190.0,
    height=60.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona --
products = Button(
    image=products_normal,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [
        change_button_image(products, products_normal, products_clicked), 
        gp.vxl(txt.menu()[26])
    ],
    relief=txt.general()[31]
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
    anchor=txt.general()[9],
    text=txt.menu()[27],
    fill=txt.menu()[28],
    font=(txt.menu()[29], 16 * -1)
)

canvas.create_text(
    726.0,
    288.0,
    anchor=txt.general()[9],
    text=txt.menu()[30],
    fill=txt.menu()[28],
    font=(txt.menu()[29], 36 * -1)
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona version--
canvas.create_text(
    14.0,
    657.0,
    anchor=txt.general()[9],
    text=txt.menu()[31],
    fill=txt.menu()[28],
    font=(txt.menu()[29], 10 * -1)
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --create_text() inserta texto en la ventana segun los parametros que se le den--
canvas.create_text(
    58.0,
    7.0,
    anchor=txt.general()[9],
    text=txt.menu()[32],
    fill=txt.general()[11],
    font=(txt.menu()[33], 13 * -1)
)

clock_text = canvas.create_text(
    1295.0,
    695.0,
    anchor=txt.general()[9],
    text="",
    fill=txt.general()[11],
    font=(txt.menu()[33], 13 * -1)
)

date_text = canvas.create_text(
    1151.0,
    695.0,
    anchor=txt.general()[9],
    text="",
    fill=txt.general()[11],
    font=(txt.menu()[33], 13 * -1)
)

# Inicia la actualización del reloj
update_clock_and_date(canvas, clock_text, date_text)

canvas.create_text(
    44.0,
    695.0,
    anchor=txt.general()[9],
    text=username,
    fill=txt.general()[11],
    font=(txt.menu()[33], 13 * -1)
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Se llama a las funciones para interactuar con la ventana--
canvas.bind(txt.menu()[34], start_move)
canvas.bind(txt.menu()[35], do_move)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# Asignar las teclas F2, F3 y F4 a sus respectivas funciones
window.bind(txt.menu()[36], lambda e: clients.invoke())
window.bind(txt.menu()[37], lambda e: products.invoke())
window.bind(txt.menu()[38], lambda e: records.invoke())
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window.resizable(False, False)
window.mainloop()
