# --Librerías y módulos--
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from pathlib import Path
from getpath import getpath as gp
from users import users
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


window = Tk()
PATH = gp.getPath()  # Constante PATH obtiene la ubicación donde estan las imágenes.

def relative_to_assets(path: str) -> Path:
    return PATH / Path(path)  # Retorna la ubicación de las imágenes usadas en la ventana.

# --Función para almacenar los datos en la base de datos. Redirige al módulo Login.py--
def user_signup():
    users.register(user_input.get(), password_input.get(), mail_input.get())
    messagebox.showinfo("Registro exitoso", "Cuenta registrada con exito.")
    window.destroy()
    gp.login_screen()
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

def on_enter(event):
    sign_up_button.invoke()  # Función para simular un clic en el botón para ingresar.

window.bind('<Return>', on_enter)  # Vincula la tecla "Enter" a la función on_enter.

window.configure(bg = "#191919")
window.overrideredirect(True)  # Elimina los bordes y decoraciones de la ventana.

# --Posiciona la ventana en pantalla--
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 300
window_height = 480

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona la ventana--
canvas = Canvas(
    window,
    bg = "#191919",
    height = 480,
    width = 300,
    bd = 0,
    highlightthickness = 0
)

canvas.place(x = 0, y = 0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --create_text() inserta texto en la ventana segun los parametros que se le den--
canvas.create_text(
    41.0,
    249.0,
    anchor="nw",
    text="Contraseña",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_text(
    41.0,
    159.0,
    anchor="nw",
    text="Usuario",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_text(
    41.0,
    69.0,
    anchor="nw",
    text="Correo",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad a la entrada de texto para el correo--
mail_image = PhotoImage(
    file=relative_to_assets("input.png"))

mail_bg = canvas.create_image(
    150.0,
    112.0,
    image=mail_image
)

mail_input = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular",12)
    
)

mail_input.place(
    x=46.0,
    y=92.0,
    width=208.0,
    height=38.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad a la entrada de texto para el usuario--
user_image = PhotoImage(
    file=relative_to_assets("input.png"))

user_bg = canvas.create_image(
    150.0,
    202.0,
    image=user_image
)

user_input = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular",12)
)

user_input.place(
    x=46.0,
    y=182.0,
    width=208.0,
    height=38.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad a la entrada de texto para la contraseña--
password_image = PhotoImage(
    file=relative_to_assets("input.png"))

password_bg = canvas.create_image(
    150.0,
    292.0,
    image=password_image
)

password_input = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular",12),
    show="●"
)

password_input.place(
    x=46.0,
    y=272.0,
    width=208.0,
    height=38.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad al botón de salida--
exit_image = PhotoImage(
    file=relative_to_assets("exit.png"))

exit_button = Button(
    image=exit_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)

exit_button.place(
    x=268.0,
    y=13.0,
    width=19.0,
    height=19.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad al botón de inicio de sesión--
sign_up_image = PhotoImage(
    file=relative_to_assets("sign_up.png"))

sign_up_button = Button(
    image=sign_up_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: user_signup(),  # temporal.
    relief="flat"
)

sign_up_button.place(
    x=71.0,
    y=362.0,
    width=158.0,
    height=48.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window.resizable(False, False)  # Fija el tamaño de la ventana en ambas posiciones (x, y).
window.mainloop()  # Hace que la ventana se mantenga abierta.
