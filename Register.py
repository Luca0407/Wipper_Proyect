# --- Librerías y módulos ---
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from pathlib import Path
from getpath import getpath as gp
from users import users
from strings import strings as txt
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --



# --- Acceso a directorios ---
PATH = gp.getPath()

def relative_to_assets(path: str) -> Path:
    return PATH / Path(path)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Registro de usuario ---
def user_signup():
    if users.check(user_input.get(), mail_input.get()) is False:
        if users.register(user_input.get(), password_input.get(), mail_input.get()) is True:
            messagebox.showinfo(txt.register()[0], txt.register()[1])
            window.destroy()
            gp.vxl(txt.general()[29])
    else:
        messagebox.showerror(txt.general()[28], txt.register()[2])
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Configuración de ventana ---
def center_window(window, width, height):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x_cordinate = (screen_width//2) - (width//2)
    y_cordinate = (screen_height//2) - (height//2)
    window.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate}")

window = Tk()
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
data_image = PhotoImage(
    file=relative_to_assets(txt.general()[1]))

mail_bg = canvas.create_image(
    150.0,
    112.0,
    image=data_image)

mail_input = Entry(
    bd=0,
    bg=txt.general()[2],
    fg=txt.general()[3],
    highlightthickness=0,
    font=(txt.general()[4],12))

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
    bg=txt.general()[2],
    fg=txt.general()[3],
    highlightthickness=0,
    font=(txt.general()[4], 12))

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
    bg=txt.general()[2],
    fg=txt.general()[3],
    highlightthickness=0,
    font=(txt.general()[4], 12),
    show=txt.general()[6])

password_input.place(
    x=46.0,
    y=272.0,
    width=208.0,
    height=38.0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Botones ---
exit_image = PhotoImage(
    file=relative_to_assets(txt.general()[7]))

exit_button = Button(
    image=exit_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief=txt.register()[3])

exit_button.place(
    x=268.0,
    y=13.0,
    width=19.0,
    height=19.0)

sign_up_image = PhotoImage(
    file=relative_to_assets(txt.general()[8]))

sign_up_button = Button(
    image=sign_up_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: user_signup(),
    relief=txt.register()[3])

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
    anchor=txt.general()[9],
    text=txt.general()[12],
    fill=txt.general()[11],
    font=(txt.general()[4], 18 * -1))

canvas.create_text(
    41.0,
    159.0,
    anchor=txt.general()[9],
    text=txt.general()[10],
    fill=txt.general()[11],
    font=(txt.general()[4], 18 * -1))

canvas.create_text(
    41.0,
    69.0,
    anchor=txt.general()[9],
    text=txt.register()[4],
    fill=txt.general()[11],
    font=(txt.general()[4], 18 * -1))
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window.bind(txt.general()[5], lambda e: sign_up_button.invoke())

window.resizable(False, False)
window.mainloop()
