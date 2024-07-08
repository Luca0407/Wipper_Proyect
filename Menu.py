from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from getpath import getpath as gp


init_path = gp.getPath()
def relative_to_assets(path: str) -> Path:
    return init_path / Path(path)

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

window = Tk()

def logout():
    gp.login_screen()
    window.destroy()

window.geometry("1360x728")
window.configure(bg = "#191919")

window.overrideredirect(True)

# Obtén el tamaño de la pantalla
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calcula la posición x e y para centrar la ventana
window_width = 300
window_height = 480
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    680.0,
    17.0,
    image=image_image_1
)

canvas.create_text(
    70.0,
    6.0,
    anchor="nw",
    text="Wipper Insumos",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    35.0,
    18.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    680.0,
    88.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    678.0,
    438.0,
    image=image_image_4
)

canvas.create_text(
    1299.0,
    150.0,
    anchor="nw",
    text="v1.1\n",
    fill="#282828",
    font=("RobotoRoman Medium", 21 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1124.0166015625,
    y=57.2484130859375,
    width=219.09884643554688,
    height=63.60934066772461
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=876.646484375,
    y=57.2484130859375,
    width=219.09884643554688,
    height=63.60934066772461
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=629.27734375,
    y=57.2484130859375,
    width=219.09884643554688,
    height=63.60934066772461
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
    x=381.90771484375,
    y=57.2484130859375,
    width=219.09884643554688,
    height=63.60934066772461
)

canvas.create_text(
    102.0,
    65.0,
    anchor="nw",
    text="Admin",
    fill="#FFFFFF",
    font=("RobotoRoman Medium", 44 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    46.0,
    87.0,
    image=image_image_5
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: logout(),
    relief="flat"
)
button_5.place(
    x=290.02783203125,
    y=57.2484130859375,
    width=63.60934066772461,
    height=63.60934066772461
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)
button_6.place(
    x=1315.0,
    y=0.0,
    width=45.0,
    height=32.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=1266.0,
    y=2.0,
    width=28.270816802978516,
    height=28.270816802978516
)

# Mover la ventana
canvas.bind("<Button-1>", start_move)
canvas.bind("<ButtonRelease-1>", stop_move)
canvas.bind("<B1-Motion>", do_move)

window.resizable(False, False)
window.mainloop()
