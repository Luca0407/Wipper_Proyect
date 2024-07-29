# --Librerías y módulos--
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from getpath import getpath as gp
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window = Tk()

# --Se obiente la ubicación de módulo y la de las imágenes--
init_path = gp.getPath()
ASSETS_PATH = init_path / 'Login_Screen' / 'build' / 'assets' / 'frame0'
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)  # Retorna la ubicación de las imágenes usadas en la ventana.

# --Función comprueba usuario y contraseña obtenidos para llamar al módulo del menú--
def check_login():
    if user_input.get() == "admin" and pass_input.get() == "12345":
        messagebox.showinfo("Ingreso exitoso", "Bienvenido al gestor de Wipper.")
        window.destroy()
        gp.wipper_menu()
    else:
        messagebox.showerror("Ingreso incorrecto", "Usuario o contraseña incorrectos.")
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

def on_enter(event):
    login_button.invoke()  # Función para simular un clic en el botón para ingresar.

def new_user():
    window.destroy()
    gp.register_screen()  # Función para abrir el módulo "Register.py".

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
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --create_text() inserta texto en la ventana segun los parametros que se le den--
canvas.create_text(
    41.0,
    161.0,
    anchor="nw",
    text="Usuario",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_text(
    41.0,
    251.0,
    anchor="nw",
    text="Contraseña",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad a la entrada de texto para el usuario--
user_image = PhotoImage(
    file=relative_to_assets("input.png"))

user_bg = canvas.create_image(
    150.0,
    204.0,
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
    y=184.0,
    width=208.0,
    height=38.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad a la entrada de texto para la contraseña--
pass_image = PhotoImage(
    file=relative_to_assets("input.png"))

password_bg = canvas.create_image(
    150.0,
    294.0,
    image=pass_image
)

pass_input = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular",11),
    show="●"
)

pass_input.place(
    x=46.0,
    y=274.0,
    width=208.0,
    height=38.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Instancia una imágen del logo em la ventana--
logo_image = PhotoImage(
    file=relative_to_assets("logo.png"))

logo = canvas.create_image(
    150.0,
    82.0,
    image=logo_image
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# --Crea, posiciona y da funcionalidad al botón para registrarse--
sign_up_image = PhotoImage(
    file=relative_to_assets("sign_up.png"))

sign_up_button = Button(
    image=sign_up_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: new_user(),  # Abre el módulo de registro.
    relief="flat"
)

sign_up_button.place(
    x=74.0,
    y=422.0,
    width=152.0,
    height=16.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad al botón para iniciar sesión--
login_image = PhotoImage(
    file=relative_to_assets("login.png"))

login_button = Button(
    image=login_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: check_login(), # Llama a la función para comprobar los input.
    relief="flat"
)

login_button.place(
    x=71.0,
    y=360.0,
    width=158.0,
    height=48.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad al botón de recuperar contraseña--
forgot_pass_image = PhotoImage(
    file=relative_to_assets("forgot_pass.png"))

forgot_pass_button = Button(
    image=forgot_pass_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("forgot_pass_button clicked"),  # temporal.
    relief="flat"
)

forgot_pass_button.place(
    x=74.0,
    y=331.0,
    width=152.0,
    height=17.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad al botón de salida--
exit_image = PhotoImage(
    file=relative_to_assets("exit.png"))

exit_button = Button(
    image=exit_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),  # Cierra el programa.
    relief="flat"
)

exit_button.place(
    x=268.0,
    y=13.0,
    width=19.0,
    height=19.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window.resizable(False, False)  # Fija el tamaño de la ventana en ambas posiciones (x, y).
window.mainloop()  # Hace que la ventana se mantenga abierta.
