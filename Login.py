# --- Librerías y módulos- --
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from pathlib import Path
from getpath import getpath as gp
from users import users
import sys
from strings import strings as txt
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


window = Tk()

def goto_window(x):
    window.destroy()
    gp.vxl(x)

username = users.current_user()
if username is not None:
    goto_window(txt.general()[29])
    sys.exit()


# --- Acceso a directorios ---
ASSETS_PATH = gp.getPath()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Gestión de usuarios ---
def new_user():
    goto_window(txt.login()[0])

def check_login():
    if users.login(user_input.get(), pass_input.get()) is True:
        goto_window(txt.general()[29])
    else:
        messagebox.showerror(txt.login()[1], txt.login()[2])
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Configuración de ventana ---
def center_window(window, width, height):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

window.overrideredirect(True)
center_window(window, 300, 480)

canvas = Canvas(
    window,
    bg = txt.general()[0],
    height = 480,
    width = 300,
    bd = 0,
    highlightthickness = 0)

canvas.place(x = 0, y = 0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Entradas de texto ---
userpass_image = PhotoImage(
    file=relative_to_assets(txt.general()[1]))

canvas.create_image(
    150.0,
    204.0,
    image=userpass_image)

user_input = Entry(
    bd=0,
    bg=txt.general()[2],
    fg=txt.general()[3],
    highlightthickness=0,
    font=(txt.general()[4], 12))

user_input.place(
    x=46.0,
    y=184.0,
    width=208.0,
    height=38.0)


password_bg = canvas.create_image(
    150.0,
    294.0,
    image=userpass_image)

pass_input = Entry(
    bd=0,
    bg=txt.general()[2],
    fg=txt.general()[3],
    highlightthickness=0,
    font=(txt.general()[4],11),
    show=txt.general()[6])

pass_input.place(
    x=46.0,
    y=274.0,
    width=208.0,
    height=38.0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Logo en pantalla ---
logo_image = PhotoImage(
    file=relative_to_assets(txt.login()[3]))

logo = canvas.create_image(
    150.0,
    82.0,
    image=logo_image)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Botones ---
sign_up_image = PhotoImage(
    file=relative_to_assets(txt.general()[8]))

sign_up_button = Button(
    image=sign_up_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: new_user())

sign_up_button.place(
    x=74.0,
    y=422.0,
    width=152.0,
    height=16.0)


login_image = PhotoImage(
    file=relative_to_assets(txt.login()[4]))

login_button = Button(
    image=login_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: check_login())

login_button.place(
    x=71.0,
    y=360.0,
    width=158.0,
    height=48.0)


forgot_pass_image = PhotoImage(
    file=relative_to_assets(txt.login()[5]))

forgot_pass_button = Button(
    image=forgot_pass_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(txt.login()[6]))# TO_DO

forgot_pass_button.place(
    x=74.0,
    y=331.0,
    width=152.0,
    height=17.0)


exit_image = PhotoImage(
    file=relative_to_assets(txt.general()[7]))

exit_button = Button(
    image=exit_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy())

exit_button.place(
    x=268.0,
    y=13.0,
    width=19.0,
    height=19.0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Textos ---
canvas.create_text(
    41.0,
    161.0,
    anchor=txt.general()[9],
    text=txt.general()[10],
    fill=txt.general()[11],
    font=(txt.general()[4], 18 * -1)
)

canvas.create_text(
    41.0,
    251.0,
    anchor=txt.general()[9],
    text=txt.general()[12],
    fill=txt.general()[11],
    font=(txt.general()[4], 18 * -1))
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

def on_enter(event):
    login_button.invoke()

window.bind(txt.general()[5], on_enter)

window.resizable(False, False)  # Fija el tamaño de la ventana en ambas posiciones (x, y).
window.mainloop()  # Hace que la ventana se mantenga abierta.
