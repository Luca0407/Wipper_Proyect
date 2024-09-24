from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from getpath import getpath as gp
import time

window = Tk()
PATH = gp.getPath()  # Constante PATH obtiene la ubicación donde estan las imágenes.


def relative_to_assets(path: str) -> Path:
    return PATH / Path(path)

def start_move(event):
    if event.y <= 30:  # Solo permite mover si el clic está en los primeros 30 píxeles
        window.x = event.x
        window.y = event.y
    else:
        window.x = None
        window.y = None

def stop_move(event):
    window.x = None
    window.y = None

def do_move(event):
    if window.x is not None and window.y is not None:  # Solo mueve si las coordenadas no son None
        deltax = event.x - window.x
        deltay = event.y - window.y
        x = window.winfo_x() + deltax
        y = window.winfo_y() + deltay
        window.geometry(f"+{x}+{y}")

def goback():
    window.destroy()
    gp.vxl("Menu")

def update_clock(canvas, clock_text):
    current_time = time.strftime('%H:%M')  # Obtén la hora actual
    canvas.itemconfig(clock_text, text=current_time)  # Actualiza el texto en el canvas
    canvas.after(1000, update_clock, canvas, clock_text)  # Llama de nuevo después de 1 segundo

def update_date(canvas, date_text):
    current_date = time.strftime('%d/%m/%y')  # Obtén la hora actual
    canvas.itemconfig(date_text, text=current_date)  # Actualiza el texto en el canvas
    canvas.after(1000, update_date, canvas, date_text)  # Llama de nuevo después de 1 segundo

window.configure(bg = "#191919")

window.overrideredirect(True)

# Obtén el tamaño de la pantalla
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calcula la posición x e y para centrar la ventana
window_width = 1360
window_height = 728
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

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
bg_logo = PhotoImage(
    file=relative_to_assets("watermark.png"))
watermark = canvas.create_image(
    678.0,
    392.0,
    image=bg_logo
)

title = PhotoImage(
    file=relative_to_assets("title_bar.png"))
title_bar = canvas.create_image(
    680.0,
    15.0,
    image=title
)

menu = PhotoImage(
    file=relative_to_assets("menu_bar.png"))
menu_bar = canvas.create_image(
    680.0,
    80.0,
    image=menu
)

status = PhotoImage(
    file=relative_to_assets("status_bar.png"))
status_bar = canvas.create_image(
    680.0,
    703.0,
    image=status
)

logo = PhotoImage(
    file=relative_to_assets("logo_icon.png"))
logo_icon = canvas.create_image(
    28.0,
    15.0,
    image=logo
)

user = PhotoImage(
    file=relative_to_assets("user_icon.png"))
user_icon = canvas.create_image(
    24.0,
    703.0,
    image=user
)

fecha = PhotoImage(
    file=relative_to_assets("date_icon.png"))
date_icon = canvas.create_image(
    1131.0,
    703.0,
    image=fecha
)

time_i = PhotoImage(
    file=relative_to_assets("time_icon.png"))
time_icon = canvas.create_image(
    1275.0,
    703.0,
    image=time_i
)

button_watermark = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_watermark,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1281.0,
    y=2.0,
    width=26.0,
    height=26.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)
button_2.place(
    x=1321.0,
    y=2.0,
    width=26.0,
    height=26.0
)

button_menu_bar = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_menu_bar,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: goback(),
    relief="flat"
)
button_3.place(
    x=1159.0,
    y=50.0,
    width=190.0,
    height=60.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=929.0,
    y=50.0,
    width=190.0,
    height=60.0
)

button_logo_icon = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_logo_icon,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)

button_5.place(
    x=9.0,
    y=50.0,
    width=190.0,
    height=60.0
)

button_user_icon = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_user_icon,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=239.0,
    y=50.0,
    width=190.0,
    height=60.0
)

button_date_icon = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_date_icon,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=469.0,
    y=50.0,
    width=190.0,
    height=60.0
)

button_time_icon = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_time_icon,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=699.0,
    y=50.0,
    width=190.0,
    height=60.0
)

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
    text="User",
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)

# Mover la ventana
canvas.bind("<Button-1>", start_move)
canvas.bind("<ButtonRelease-1>", stop_move)
canvas.bind("<B1-Motion>", do_move)

window.resizable(False, False)
window.mainloop()
