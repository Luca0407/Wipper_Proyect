# --Librerías y módulos--
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from getpath import getpath as gp
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window = Tk()
INIT_PATH = gp.getPath()

def relative_to_assets(path: str) -> Path:
    return INIT_PATH / Path(path)  # Retorna la ubicación de las imágenes usadas en la ventana.

# --Función que permite mover si el clic está en los primeros 30 píxeles--
def start_move(event):
    if event.y <= 30:
        window.x = event.x
        window.y = event.y
    else:
        window.x = None
        window.y = None
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Función que detiene el movimiento de la ventana--
def stop_move(event):
    window.x = None
    window.y = None
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Función que mueve la ventana si las coordenadas no son None--
def do_move(event):
    if window.x is not None and window.y is not None:  # Solo mueve si las coordenadas no son None
        deltax = event.x - window.x
        deltay = event.y - window.y
        x = window.winfo_x() + deltax
        y = window.winfo_y() + deltay
        window.geometry(f"+{x}+{y}")
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Función para cerrar sesión--
def logout():
    gp.login_screen()
    window.destroy()
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Posiciona la ventana en pantalla--
window.configure(bg = "#191919")
window.overrideredirect(True)

window_width = 1360
window_height = 720

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
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

# --create_text() inserta texto en la ventana segun los parametros que se le den--
canvas.create_text(
    70.0,
    6.0,
    anchor="nw",
    text="Wipper Insumos",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 20 * -1)
)

canvas.create_text(
    1299.0,
    150.0,
    anchor="nw",
    text="v1.1\n",
    fill="#282828",
    font=("RobotoRoman Medium", 21 * -1)
)

canvas.create_text(
    102.0,
    65.0,
    anchor="nw",
    text="Admin",
    fill="#FFFFFF",
    font=("RobotoRoman Medium", 44 * -1)
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona la imagen "dashboard"--
dashboard = PhotoImage(
    file=relative_to_assets("dashboard.png"))

db = canvas.create_image(
    680.0,
    17.0,
    image=dashboard
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona el icono de Wipper--
wipper_icon = PhotoImage(
    file=relative_to_assets("icon.png"))

icon = canvas.create_image(
    35.0,
    18.0,
    image=wipper_icon
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona la imagen "windowboard"--
windowboard = PhotoImage(
    file=relative_to_assets("windowboard.png"))

wb = canvas.create_image(
    680.0,
    88.0,
    image=windowboard
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona la imagen del fondo--
background = PhotoImage(
    file=relative_to_assets("background.png"))

bg = canvas.create_image(
    678.0,
    438.0,
    image=background
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea y posiciona el icono del usuario--
user = PhotoImage(
    file=relative_to_assets("user.png"))

user_icon = canvas.create_image(
    46.0,
    87.0,
    image=user
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad al boton "clientes"--
button_clientes = PhotoImage(
    file=relative_to_assets("clientes.png"))

clientes = Button(
    image=button_clientes,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("clientes clicked"),
    relief="flat"
)

clientes.place(
    x=1124.0166015625,
    y=57.2484130859375,
    width=219.09884643554688,
    height=63.60934066772461
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad al boton "registros"--
button_registros = PhotoImage(
    file=relative_to_assets("registros.png"))

registros = Button(
    image=button_registros,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("registros clicked"),
    relief="flat"
)

registros.place(
    x=876.646484375,
    y=57.2484130859375,
    width=219.09884643554688,
    height=63.60934066772461
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad al boton "productos"--
button_productos = PhotoImage(
    file=relative_to_assets("productos.png"))

productos = Button(
    image=button_productos,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("productos clicked"),
    relief="flat"
)

productos.place(
    x=629.27734375,
    y=57.2484130859375,
    width=219.09884643554688,
    height=63.60934066772461
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad al boton "costos"--
button_costos = PhotoImage(
    file=relative_to_assets("costos.png"))

costos = Button(
    image=button_costos,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("costos clicked"),
    relief="flat"
)

costos.place(
    x=381.90771484375,
    y=57.2484130859375,
    width=219.09884643554688,
    height=63.60934066772461
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad al boton "logout"--
button_logout = PhotoImage(
    file=relative_to_assets("logout.png"))

logout_b = Button(
    image=button_logout,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: logout(),
    relief="flat"
)

logout_b.place(
    x=290.02783203125,
    y=57.2484130859375,
    width=63.60934066772461,
    height=63.60934066772461
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad al boton "close"--
button_close = PhotoImage(
    file=relative_to_assets("close.png"))

close = Button(
    image=button_close,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)

close.place(
    x=1315.0,
    y=0.0,
    width=45.0,
    height=32.0
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Crea, posiciona y da funcionalidad al boton "minimize"--
button_minimize = PhotoImage(
    file=relative_to_assets("minimize.png"))

minimize = Button(
    image=button_minimize,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("minimize clicked"),
    relief="flat"
)

minimize.place(
    x=1266.0,
    y=2.0,
    width=28.270816802978516,
    height=28.270816802978516
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --Funciones para mover la ventana--
canvas.bind("<Button-1>", start_move)
canvas.bind("<ButtonRelease-1>", stop_move)
canvas.bind("<B1-Motion>", do_move)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window.resizable(False, False)  # Fija el tamaño de la ventana en ambas posiciones (x, y).
window.mainloop()  # Hace que la ventana se mantenga abierta.
