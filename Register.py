from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from pathlib import Path
from getpath import getpath as gp
from users import users


PATH = gp.getPath()

def relative_to_assets(path: str) -> Path:
    return PATH / Path(path)

window = Tk()

window.geometry("300x480")
window.configure(bg = "#191919")

window.overrideredirect(True)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 300
window_height = 480

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

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

button_image_1 = PhotoImage(
    file=relative_to_assets("sign_up.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: users.register(entry_3.get(), entry_2.get(), entry_1.get(), window),
    relief="flat"
)

button_1.place(
    x=71.0,
    y=362.0,
    width=158.0,
    height=48.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("exit.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
)
button_2.place(
    x=268.0,
    y=13.0,
    width=19.0,
    height=19.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("input.png"))
entry_bg_3 = canvas.create_image(
    150.0,
    112.0,
    image=entry_image_3
)

entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular",12)
    
)

entry_3.place(
    x=46.0,
    y=92.0,
    width=208.0,
    height=38.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("input.png"))
entry_bg_2 = canvas.create_image(
    150.0,
    202.0,
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
    y=182.0,
    width=208.0,
    height=38.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("input.png"))
entry_bg_1 = canvas.create_image(
    150.0,
    292.0,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular",12),
    show="●"
)

entry_1.place(
    x=46.0,
    y=272.0,
    width=208.0,
    height=38.0
)

window.resizable(False, False)
window.mainloop()

