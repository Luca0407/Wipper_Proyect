# --- Librerías y módulos- --
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from pathlib import Path
from getpath import getpath as gp
from users import users
import sys
from strings import strings as txt
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


general = txt.general()
login = txt.login()

username = users.current_user()
if username is not None:
    gp.vxl(general[29])
    sys.exit()  # No creamos la ventana si el usuario ya está autenticado

window = Tk()


def goto_window(x):
    window.destroy()
    gp.vxl(x)

def relative_to_assets(path: str) -> Path:
    assets_path = gp.getPath()  # Centralizamos dentro de la función
    return assets_path / Path(path)


# --- Gestión de usuarios ---
def new_user():
    goto_window(login[0])

def check_login():
    if users.login(user_input.get(), pass_input.get()) is True:
        goto_window(general[29])
    else:
        messagebox.showerror(login[1], login[2])
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Configuración de ventana ---
def center_window(window, width, height):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

center_window(window, 300, 480)
window.overrideredirect(True)

# Crear el canvas
canvas = Canvas(
    window,
    bg=general[0],
    height=480,
    width=300,
    bd=0,
    highlightthickness=0
)
canvas.place(x=0, y=0)

# --- Entradas de texto ---
userpass_image = PhotoImage(file=relative_to_assets(general[1]))

entry_config = {
    "bd": 0,
    "bg": general[2],
    "fg": general[3],
    "highlightthickness": 0,
    "font": (general[4], 11)
}

def entry_bg(x, y):
    canvas.create_image(x, y, image=userpass_image)

# Campo de usuario
entry_bg(150, 204)
user_input = Entry(**entry_config)
user_input.place(x=46.0, y=184.0, width=208.0, height=38.0)

# Campo de contraseña
entry_bg(150, 294)
pass_input = Entry(**entry_config, show=general[6])
pass_input.place(x=46.0, y=274.0, width=208.0, height=38.0)

# --- Logo en pantalla ---
logo_image = PhotoImage(file=relative_to_assets(login[3]))
canvas.create_image(150.0, 82.0, image=logo_image)

# --- Botones ---
def create_button(image_path, command, x, y, width, height):
    image = PhotoImage(file=relative_to_assets(image_path))
    button = Button(
        image=image,
        borderwidth=0,
        highlightthickness=0,
        command=command)
    button.image = image  # Para evitar que se elimine la referencia
    button.place(x=x, y=y, width=width, height=height)
    return button

signup_button = create_button(general[8], lambda: new_user(), 74.0, 422.0, 152.0, 16.0)
login_button = create_button(login[4], lambda: check_login(), 71.0, 360.0, 158.0, 48.0)
forgot_button = create_button(login[5], lambda: print("forgot_pass_button clicked"), 74.0, 331.0, 152.0, 17.0)
exit_button = create_button(general[7], window.destroy, 268.0, 13.0, 19.0, 19.0)

# --- Textos ---
user = canvas.create_text(41.0, 161.0, anchor=general[9], text=general[10], fill=general[11], font=(general[4], 18 * -1))
passwd = canvas.create_text(41.0, 251.0, anchor=general[9], text=general[12], fill=general[11], font=(general[4], 18 * -1))
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window.bind(general[5], lambda e: login_button.invoke())

window.resizable(False, False)  # Fija el tamaño de la ventana en ambas posiciones (x, y).
window.mainloop()  # Hace que la ventana se mantenga abierta.
