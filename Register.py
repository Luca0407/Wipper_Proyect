# --- Librerías y módulos ---
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from pathlib import Path
from getpath import getpath as gp
from users import users
from strings import strings as txt


general = txt.general()
register = txt.register()

# --- Acceso a directorios ---
def relative_to_assets(path: str) -> Path:
    assets_path = gp.getPath()
    return assets_path / Path(path)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --- Registro de usuario ---
def user_signup():
    if users.check(user_input.get(), mail_input.get()) is False:
        if users.register(user_input.get(), password_input.get(), mail_input.get()) is True:
            messagebox.showinfo(register[0], register[1])
            window.destroy()
            return gp.vxl(general[29])
    else:
        messagebox.showerror(general[28], register[2])
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
    bg = general[0],
    height = 480,
    width = 300,
    bd = 0,
    highlightthickness = 0)

canvas.place(x = 0, y = 0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --- Entradas de texto ---
data_image = PhotoImage(
    file=relative_to_assets(general[1]))

mail_bg = canvas.create_image(
    150.0,
    112.0,
    image=data_image)

mail_input = Entry(
    bd=0,
    bg=general[2],
    fg=general[3],
    highlightthickness=0,
    font=(general[4],12))

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
    bg=general[2],
    fg=general[3],
    highlightthickness=0,
    font=(general[4], 12))

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
    bg=general[2],
    fg=general[3],
    highlightthickness=0,
    font=(general[4], 12),
    show=general[6])

password_input.place(
    x=46.0,
    y=272.0,
    width=165.0,
    height=38.0)

image_image_2 = PhotoImage(
    file=relative_to_assets(general[36]))
image_2 = canvas.create_image(
    219.0,
    292.0,
    image=image_image_2
)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# Agregar las imágenes adicionales para el cambio de estado
button_image_3 = PhotoImage(file=relative_to_assets(general[37]))

# Estado de visibilidad de la contraseña
password_visible_1 = False

button_image_2 = PhotoImage(
    file=relative_to_assets(general[38]))

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    relief=general[31]
)
button_2.place(
    x=225.0,
    y=278.0,
    width=27.0,
    height=27.0
)

# Función para el botón 5
def toggle_password_1():
    global password_visible_1
    if password_visible_1:
        password_input.config(show=general[6])
        button_2.config(image=button_image_2)
    else:
        password_input.config(show="")
        button_2.config(image=button_image_3)
    password_visible_1 = not password_visible_1

# Cambia el parámetro `command` de los botones 5 y 7 para que usen las nuevas funciones
button_2.config(command=toggle_password_1)

# --- Botones ---
exit_image = PhotoImage(
    file=relative_to_assets(general[7]))

exit_button = Button(
    image=exit_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief=general[31])

exit_button.place(
    x=268.0,
    y=13.0,
    width=22.0,
    height=22.0)

sign_up_image = PhotoImage(
    file=relative_to_assets(general[8]))

sign_up_button = Button(
    image=sign_up_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: user_signup(),
    relief=general[31])

sign_up_button.place(
    x=71.0,
    y=362.0,
    width=158.0,
    height=48.0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


# --- Textos ---
canvas.create_text(
    41.0,
    69.0,
    anchor=general[9],
    text=register[3],
    fill=general[11],
    font=(general[4], 18 * -1))


canvas.create_text(
    41.0,
    159.0,
    anchor=general[9],
    text=general[10],
    fill=general[11],
    font=(general[4], 18 * -1))


canvas.create_text(
    41.0,
    249.0,
    anchor=general[9],
    text=general[12],
    fill=general[11],
    font=(general[4], 18 * -1))
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window.bind(general[5], lambda e: sign_up_button.invoke())

window.resizable(False, False)
window.mainloop()