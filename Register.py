# --- Librerías y módulos ---
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from pathlib import Path
from getpath import getpath as gp
from users import users
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


window = Tk()


# --- Acceso a directorios ---
PATH = gp.getPath()

def relative_to_assets(path: str) -> Path:
    return PATH / Path(path)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Registro de usuario ---
def user_signup():
    if users.check(user_input.get(), mail_input.get()) is False:
        users.register(user_input.get(), password_input.get(), mail_input.get())
        messagebox.showinfo("Registro exitoso", "Cuenta registrada con exito.")
        window.destroy()
        gp.login_screen()
    else:
        messagebox.showerror("ERROR","Este usuario ya se encuentra registrado.")
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Configuración de ventana ---
window.overrideredirect(True)

window_width = 300
window_height = 480

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

canvas = Canvas(
    window,
    bg = "#191919",
    height = 480,
    width = 300,
    bd = 0,
    highlightthickness = 0)

canvas.place(x = 0, y = 0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Entradas de texto ---
data_image = PhotoImage(
    file=relative_to_assets("input.png"))

mail_bg = canvas.create_image(
    150.0,
    112.0,
    image=data_image)

mail_input = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular",12))

mail_input.place(
    x=46.0,
    y=92.0,
    width=208.0,
    height=38.0)


user_bg = canvas.create_image(
    150.0,
    202.0,
    image=data_image)

user_input = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular",12))

user_input.place(
    x=46.0,
    y=182.0,
    width=208.0,
    height=38.0)


password_bg = canvas.create_image(
    150.0,
    292.0,
    image=data_image)

password_input = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular",12),
    show="●")

password_input.place(
    x=46.0,
    y=272.0,
    width=208.0,
    height=38.0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Botones ---
exit_image = PhotoImage(
    file=relative_to_assets("exit.png"))

exit_button = Button(
    image=exit_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat")

exit_button.place(
    x=268.0,
    y=13.0,
    width=19.0,
    height=19.0)


sign_up_image = PhotoImage(
    file=relative_to_assets("sign_up.png"))

sign_up_button = Button(
    image=sign_up_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: user_signup(),
    relief="flat")

sign_up_button.place(
    x=71.0,
    y=362.0,
    width=158.0,
    height=48.0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Textos ---
canvas.create_text(
    41.0,
    249.0,
    anchor="nw",
    text="Contraseña",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1))

canvas.create_text(
    41.0,
    159.0,
    anchor="nw",
    text="Usuario",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1))

canvas.create_text(
    41.0,
    69.0,
    anchor="nw",
    text="Correo",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1))
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


def on_enter(event):
    sign_up_button.invoke()

window.bind('<Return>', on_enter)

window.resizable(False, False)
window.mainloop()
