# --- Librerías y módulos ---
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, messagebox
from getpath import getpath as gp
from users import users
from time import strftime
from strings import strings as txt
import sys
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --



general = txt.general()
mainmenu = txt.menu()

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
window = Tk()
username = users.current_user()

if username is None:
    window.destroy()
    gp.vxl(general[30])
    sys.exit()


def relative_to_assets(path: str) -> Path:
    PATH = gp.getPath()
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
    current_time = strftime(mainmenu[0])
    win.itemconfig(clock_text, text=current_time)

    current_date = strftime(general[35])
    win.itemconfig(date_text, text=current_date)

    win.after(1000, update_clock_and_date, win, clock_text, date_text)  # Llama de nuevo después de 1 segundo

# --- Cierre de sesión ---
def logout():
    window.destroy()
    users.logout(username)
    gp.vxl(general[30])
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

def center_window(window, width, height):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

window.overrideredirect(True)
center_window(window, 1360, 728)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

canvas = Canvas(
    window,
    bg = general[0],
    height = 728,
    width = 1360,
    bd = 0,
    highlightthickness = 0,
    relief = general[34])

canvas.place(x = 0, y = 0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# Lista con las configuraciones de imágenes
images = [
    (mainmenu[7],  680.0, 404.0), 
    (mainmenu[8],  499.0, 392.0), 
    (mainmenu[9],  680.0, 15.0),  
    (mainmenu[10], 680.0, 80.0),  
    (mainmenu[11], 680.0, 703.0), 
    (mainmenu[12], 28.0,  15.0),  
    (mainmenu[13], 24.0,  703.0), 
    (mainmenu[14], 1131.0, 703.0),
    (mainmenu[15], 1275.0, 703.0),
    (mainmenu[16], 1290.0, 14.5),
    (mainmenu[17], 1335.0, 14.5),
    (mainmenu[18], 1200.0, 79.3),
    (mainmenu[20], 150.0, 79.3),
    (mainmenu[1], 413, 83),
    (mainmenu[3], 954, 83),
    (mainmenu[5], 680, 83)
    ]

image_references = {}
# Diccionarios para almacenar posiciones de imágenes
image_positions = {}

# Crear y posicionar imágenes en el canvas
for index, (image_path, x, y) in enumerate(images):
    image_references[f"img_{index}"] = PhotoImage(file=relative_to_assets(image_path))
    
    # Guardamos la posición de la imagen en el diccionario
    image_positions[f"img_{index}"] = (x, y)
    
    # Crear la imagen en el canvas con una etiqueta
    canvas.create_image(x, y, image=image_references[f"img_{index}"], tags=f"img_{index}")

alternate_images = {
    "img_1a": PhotoImage(file=relative_to_assets(mainmenu[2])),  # Por ejemplo, la imagen de otro color
    "img_2a": PhotoImage(file=relative_to_assets(mainmenu[4])),
    "img_3a": PhotoImage(file=relative_to_assets(mainmenu[6])),
    # Agrega más imágenes alternas según sea necesario
}

button_images = {
    "img_1": {
        "original": image_references["img_13"],
        "alternative": PhotoImage(file=relative_to_assets(mainmenu[2]))
    },
    "img_2": {
        "original": image_references["img_14"],
        "alternative": PhotoImage(file=relative_to_assets(mainmenu[4]))
    },
    "img_3": {
        "original": image_references["img_15"],
        "alternative": PhotoImage(file=relative_to_assets(mainmenu[6]))
    },
}

def cambiar_imagen_boton(btn, image_type, button_key, func=None):
    if image_type == "alternative":
        btn.configure(image=button_images[button_key]["alternative"])
    else:
        btn.configure(image=button_images[button_key]["original"])
    
    if func:
            func()

# Función que llama a la función vxl del archivo 2 y pasa la información necesaria
def ejecutar_vxl(screen, btn, button_images, bk):
    # Llamamos a la función vxl pasando el botón y las imágenes
    gp.vxl(screen, btn, button_images, bk)

button_data = [
    (image_references["img_12"], lambda: messagebox.showinfo(mainmenu[21], mainmenu[22]), 60.0, 51),
    (image_references["img_13"], lambda: (ejecutar_vxl(mainmenu[23], buttons_dict["img_1"], button_images, "img_1")), 315, 51),
    (image_references["img_14"], lambda: (ejecutar_vxl(mainmenu[19], buttons_dict["img_2"], button_images, "img_2")), 855, 51),
    (image_references["img_15"], lambda: (ejecutar_vxl(mainmenu[24], buttons_dict["img_3"], button_images, "img_3")), 585, 51),
    (image_references["img_9"], lambda: print("minimize clicked"), 1280.0, 2),  # Minimizar
    (image_references["img_10"], window.destroy, 1325, 2),  # Cerrar
    (image_references["img_11"], logout, 1100, 51),  # Logout
]

buttons_dict = {}  # Diccionario para almacenar referencias a botones
buttons = []

for index, (img, cmd, x, y) in enumerate(button_data):
    btn = Button(
        image=img,
        borderwidth=0,
        highlightthickness=0,
        command=cmd,
        relief=general[31]
    )
    buttons_dict[f"img_{index}"] = btn  # Guardamos la referencia del botón en el diccionario
    print(str(img))
    # Colocamos los botones en el canvas
    if str(img) in ("pyimage12", "pyimage13", "pyimage14", "pyimage15", "pyimage16"):
        btn.place(x=x, y=y, width=190, height=60)
    else:
        btn.place(x=x, y=y, width=26, height=26)

    buttons.append(btn)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# Lista con las configuraciones de los textos
texts = [
    (726.0, 356.0, mainmenu[25], mainmenu[26], mainmenu[27], 16),  # Teclas rápidas
    (726.0, 288.0, mainmenu[28], mainmenu[26], mainmenu[27], 36),  
    (14.0, 657.0, mainmenu[29], mainmenu[26], mainmenu[27], 10),   # Versión
    (58.0, 7.0, mainmenu[30], general[11], mainmenu[31], 13),      # Otro texto
    (44.0, 695.0, username, general[11], mainmenu[31], 13)         # Usuario
]

# Crear los textos dinámicamente
for x, y, text, fill, font_family, font_size in texts:
    canvas.create_text(
        x, y, anchor=general[9], text=text, fill=fill, font=(font_family, font_size * -1))

# Crear los textos del reloj y la fecha
clock_text = canvas.create_text(
    1295.0, 695.0, anchor=general[9], text="", fill=general[11], font=(mainmenu[31], 13 * -1))
date_text = canvas.create_text(
    1151.0, 695.0, anchor=general[9], text="", fill=general[11], font=(mainmenu[31], 13 * -1))

# Inicia la actualización del reloj
update_clock_and_date(canvas, clock_text, date_text)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# Diccionario de eventos y funciones para canvas y ventana
bindings = {
    mainmenu[32]: (canvas, start_move),
    mainmenu[33]: (canvas, do_move)
}

# Vincula cada evento con su respectiva función en el objeto correspondiente
for key, (obj, function) in bindings.items():
    obj.bind(key, function)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window.resizable(False, False)
window.mainloop()
