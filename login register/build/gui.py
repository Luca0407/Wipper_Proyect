from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Admin\Desktop\ttk\login register\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1360x728")
window.configure(bg = "#191919")

window.overrideredirect(True)

window_width = 1360
window_height = 728

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
    15.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    28.0,
    15.0,
    image=image_image_2
)

canvas.create_text(
    58.0,
    7.0,
    anchor="nw",
    text="Wipper Insumos",
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
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
    x=223.1455078125,
    y=577.4705810546875,
    width=233.7083282470703,
    height=71.0
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
    x=224.0,
    y=425.0,
    width=232.4705810546875,
    height=24.47058868408203
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    464.0,
    368.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    309.5,
    368.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular", 20),
    show="●"
)
entry_1.place(
    x=183.0,
    y=338.0,
    width=253.0,
    height=58.0
)

canvas.create_text(
    178.0,
    297.0,
    anchor="nw",
    text="Contraseña",
    fill="#FFFFFF",
    font=("Montserrat Regular", 26 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=449.0,
    y=347.0,
    width=41.0,
    height=41.0
)


image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1144.0,
    500.0,
    image=image_image_4
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    989.5,
    500.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular", 20),
    show="●"
)
entry_2.place(
    x=863.0,
    y=470.0,
    width=253.0,
    height=58.0
)

canvas.create_text(
    858.0,
    429.0,
    anchor="nw",
    text="Contraseña",
    fill="#FFFFFF",
    font=("Montserrat Regular", 26 * -1)
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
    x=1129.0,
    y=479.0,
    width=41.0,
    height=41.0
)


entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    339.5,
    240.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular", 20)
)
entry_3.place(
    x=183.0,
    y=210.0,
    width=313.0,
    height=58.0
)

canvas.create_text(
    178.0,
    169.0,
    anchor="nw",
    text="Usuario",
    fill="#FFFFFF",
    font=("Montserrat Regular", 26 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1019.5,
    370.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular", 20)
)
entry_4.place(
    x=863.0,
    y=340.0,
    width=313.0,
    height=58.0
)

canvas.create_text(
    858.0,
    299.0,
    anchor="nw",
    text="Usuario",
    fill="#FFFFFF",
    font=("Montserrat Regular", 26 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    441.0,
    367.0,
    image=image_image_5
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    1019.5,
    240.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular", 20)
)
entry_5.place(
    x=863.0,
    y=210.0,
    width=313.0,
    height=58.0
)

canvas.create_text(
    858.0,
    169.0,
    anchor="nw",
    text="Correo",
    fill="#FFFFFF",
    font=("Montserrat Regular", 26 * -1)
)

canvas.create_text(
    191.0,
    79.0,
    anchor="nw",
    text="Iniciar Sesión",
    fill="#FFFFFF",
    font=("Montserrat Regular", 45 * -1)
)

canvas.create_text(
    893.0,
    79.0,
    anchor="nw",
    text="Registrarse",
    fill="#FFFFFF",
    font=("Montserrat Regular", 45 * -1)
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=903.0,
    y=577.0,
    width=233.7083282470703,
    height=71.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    1121.0,
    499.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    679.9999737731669,
    364.0,
    image=image_image_7
)

# Agregar las imágenes adicionales para el cambio de estado
button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))

# Estado de visibilidad de la contraseña
password_visible_1 = False
password_visible_2 = False

# Función para el botón 5
def toggle_password_1():
    global password_visible_1
    if password_visible_1:
        entry_1.config(show="●")
        button_5.config(image=button_image_5)
    else:
        entry_1.config(show="")
        button_5.config(image=button_image_6)
    password_visible_1 = not password_visible_1

# Función para el botón 7
def toggle_password_2():
    global password_visible_2
    if password_visible_2:
        entry_2.config(show="●")
        button_7.config(image=button_image_7)
    else:
        entry_2.config(show="")
        button_7.config(image=button_image_8)
    password_visible_2 = not password_visible_2

# Cambia el parámetro `command` de los botones 5 y 7 para que usen las nuevas funciones
button_5.config(command=toggle_password_1)
button_7.config(command=toggle_password_2)


window.resizable(False, False)
window.mainloop()
