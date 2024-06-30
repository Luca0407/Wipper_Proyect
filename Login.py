from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from getpath import getpath as gp


init_path = gp.getPath()
ASSETS_PATH = init_path / 'Login_Screen' / 'build' / 'assets' / 'frame0'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def check_login():
    if entry_2.get() == "admin" and entry_1.get() == "12345":
        messagebox.showinfo("Ingreso exitoso", "Bienvenido al gestor de Wipper.")
        window.destroy()
        gp.wipper_menu(init_path)
    elif entry_2.get() == "" and entry_1.get() == "":
        messagebox.showerror("Ingreso incorrecto", "Rellene los campos, no sea imbecil.")
    else:
        messagebox.showerror("Ingreso incorrecto", "Usuario o contraseña incorrectos.")

window = Tk()

window.geometry("300x480")
window.configure(bg = "#191919")

window.overrideredirect(True)

#calcula tamaño de la pantalla
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calcula la posición x e y para centrar la ventana
window_width = 300
window_height = 480
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

# Coloca la ventana en el centro de la pantalla
window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

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
button_image_1 = PhotoImage(
    file=relative_to_assets("sign_up.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gp.register_screen(init_path),
    relief="flat"
)

button_1.place(
    x=74.0,
    y=422.0,
    width=152.0,
    height=16.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("login.png"))

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: check_login(),
    relief="flat"
)

button_2.place(
    x=71.0,
    y=360.0,
    width=158.0,
    height=48.0
)

# Función para simular el clic en el botón 2 (boton ingresar)
def on_enter(event):
    button_2.invoke()

# Vincula la tecla "Enter" a la función on_enter
window.bind('<Return>', on_enter)

button_image_3 = PhotoImage(
    file=relative_to_assets("forgot_pass.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=74.0,
    y=331.0,
    width=152.0,
    height=17.0
)

canvas.create_text(
    41.0,
    161.0,
    anchor="nw",
    text="Usuario",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("input.png"))
entry_bg_2 = canvas.create_image(
    150.0,
    204.0,
    image=entry_image_2
)

entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular",12)
)

entry_2.place(
    x=46.0,
    y=184.0,
    width=208.0,
    height=38.0
)

canvas.create_text(
    41.0,
    251.0,
    anchor="nw",
    text="Contraseña",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("input.png"))
entry_bg_1 = canvas.create_image(
    150.0,
    294.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular",11),
    show="●"
)
entry_1.place(
    x=46.0,
    y=274.0,
    width=208.0,
    height=38.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("logo.png"))
image_1 = canvas.create_image(
    150.0,
    82.0,
    image=image_image_1
)

button_image_4 = PhotoImage(file=relative_to_assets("exit.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy, #cierra el programa
    relief="flat"
)
button_4.place(
    x=268.0,
    y=13.0,
    width=19.0,
    height=19.0
)
window.resizable(False, False)
window.mainloop()
