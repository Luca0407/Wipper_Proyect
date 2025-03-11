# --- Librerías y módulos ---
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, messagebox, ttk, Frame
from getpath import getpath as gp
from users import users
from time import strftime
from strings import strings as txt
import sys

# --- Inicialización ---
general = txt.general()
mainmenu = txt.menu()
products = txt.products()
queries = txt.queries()
window = Tk()
username = users.current_user()
window.attributes("-topmost", True)

if username is None:
    window.destroy()
    gp.vxl(general[30])
    sys.exit()

def relative_to_assets(path: str) -> Path:
    PATH = gp.getPath()
    return PATH / Path(path)

def center_window(window, width, height):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# --- Frame para mostrar u ocultar ---
frame_container = Frame(window, width=1360, height=550, bg="#333")
frame_container.place(x=0, y=100)
frame_container.pack_propagate(False)
frame_container_visible = False

def toggle_frame():
    global frame_container_visible
    if frame_container_visible:
        frame_container.place_forget()
    else:
        frame_container.place(x=0, y=100)
    frame_container_visible = not frame_container_visible

# --- Contenido del Frame ---
style = ttk.Style(window)
theme_path = rf"{gp.getPath()}\forest-dark.tcl"
window.tk.call(general[15], theme_path)
style.theme_use(general[16])

widgets_frame = ttk.LabelFrame(frame_container, text=products[4])
widgets_frame.pack(padx=20, pady=10)

def only_numbers_input(P):
    return P.isdigit() or P == ""

vcmd = (window.register(only_numbers_input), "%P")

product_entry = ttk.Entry(widgets_frame)
cost_entry = ttk.Entry(widgets_frame, validate="none", validatecommand=vcmd)
entries = [(product_entry, products[0]), (cost_entry, products[1])]

for i, (entry, default_text) in enumerate(entries):
    entry.insert(0, default_text)
    entry.grid(row=i, column=0, padx=5, pady=(0, 5), sticky=general[22])

separator = ttk.Separator(widgets_frame)
separator.grid(row=3, column=0, padx=10, pady=10, sticky=general[22])

button_close = ttk.Button(widgets_frame, text=general[25], command=toggle_frame)
button_close.grid(row=5, column=0, padx=5, pady=(0, 5), sticky=general[26])

treeFrame = ttk.Frame(frame_container)
treeFrame.pack(pady=10)

treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side=general[17], fill=general[18])

cols = (general[20], products[0], products[1])
treeview = ttk.Treeview(treeFrame, show=general[19], yscrollcommand=treeScroll.set, columns=cols, height=23)
for col, width in zip(cols, [50, 438, 442]):
    treeview.column(col, width=width)
treeview.pack()
treeScroll.config(command=treeview.yview)

# --- Botón para mostrar/ocultar el frame ---
button_toggle_frame = Button(window, text="Mostrar/Ocultar Panel", command=toggle_frame)
button_toggle_frame.place(x=600, y=600, width=160, height=40)

window.overrideredirect(True)
center_window(window, 1360, 728)
window.mainloop()