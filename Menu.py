from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from getpath import getpath as gp


init_path = Path(__file__).parent
PATH = gp.getPath()

def relative_to_assets(path: str) -> Path:
    return PATH / Path(path)

def logout(path):
    window.destroy()
    gp.login_screen(path)

window = Tk()

# título de la ventana
window.title("Wipper Insumos")

# icono de la ventana
icon_image = PhotoImage(file=relative_to_assets("logo.png"))
window.iconphoto(False, icon_image)

# maximiza la ventana
window.state('zoomed')

window.geometry("1360x700")
window.configure(bg = "#191919")

canvas = Canvas(
    window,
    bg = "#191919",
    height = 700,
    width = 1360,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    157.0,
    612.0,
    anchor="nw",
    text="v1.0",
    fill="#8F9191",
    font=("MontserratRoman Medium", 14 * -1)
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
    x=11.0,
    y=501.0,
    width=318.0,
    height=80.0
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
    x=11.0,
    y=396.0,
    width=318.0,
    height=80.0
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
    x=11.0,
    y=291.0,
    width=318.0,
    height=80.0
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
    x=11.0,
    y=185.0,
    width=318.0,
    height=80.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))

image_1 = canvas.create_image(
    170.0,
    107.0,
    image=image_image_1
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))

button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: logout(init_path),
    relief="flat"
)

button_5.place(
    x=127.0,
    y=117.0,
    width=114.0,
    height=22.0
)

canvas.create_text(
    141.0,
    83.0,
    anchor="nw",
    text="Admin",
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 25 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    57.0,
    107.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    859.0,
    348.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    360.0,
    348.0,
    image=image_image_4
)

window.resizable(True, True)
window.mainloop()
