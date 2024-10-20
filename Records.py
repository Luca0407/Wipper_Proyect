# --- Librerías y Módulos ---
import tkinter as tk
from tkinter import ttk
from getpath import getpath as gp
import sqlite3
from strings import strings as txt
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --



# --- x ---
connect = sqlite3.connect(txt.general()[13])
cursor = connect.cursor()
init_path = gp.getPath()
cols = (txt.records()[0], txt.records()[1], txt.records()[2],
        txt.records()[3], txt.records()[4], txt.records()[5],
        txt.records()[6], txt.records()[7], txt.records()[8])


def close():
    root.destroy()
    connect.close()


def load_data(x):
    query_map = {1: txt.queries()[0], 2: txt.queries()[7]}
    cursor.execute(query_map.get(x))
    db_data = cursor.fetchall()

    if x == 1:
        for col_marca in cols:
            treeview.heading(col_marca, text=col_marca, anchor=tk.CENTER)
            treeview.column(col_marca, anchor=tk.CENTER)

    for value_tuple in db_data:
        treeview.insert('', tk.END, values=value_tuple)


def center_window(window, width, height):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2) + 37
    window.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.overrideredirect(True)
center_window(root, 1360, 550)

style = ttk.Style(root)
theme_path = rf"{init_path}\forest-dark.tcl"
root.tk.call(txt.general()[15], theme_path)
style.theme_use(txt.general()[16])

frame = ttk.Frame(root)
frame.pack()

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side=txt.general()[17], fill=txt.general()[18])
widgets_frame = ttk.LabelFrame(frame, text=txt.records()[9])
widgets_frame.grid(row=1, column=1, padx=1, pady=0)

button_close = ttk.Button(widgets_frame, text=txt.general()[25], command=close)
button_close.grid(row=0, column=2, padx=(20, 5), pady=(0, 5), sticky=txt.records()[10])


# --Crea y posiciona --
def on_enter(event):
    button_mod.invoke()

button_mod = ttk.Button(widgets_frame, text=txt.records()[11], command=print("modificando"))
button_mod.grid(row=0, column=0, padx=(5, 20), pady=(0, 5), sticky=txt.records()[10])

button_del = ttk.Button(widgets_frame, text=txt.records()[12], command=print("borrando"))
button_del.grid(row=0, column=1, padx=50, pady=(0, 5), sticky=txt.records()[10])

root.bind(txt.general()[14], lambda e: button_close.invoke())
root.bind(txt.general()[5], lambda e: button_mod.invoke())
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

treeview = ttk.Treeview(treeFrame, show=txt.general()[19], yscrollcommand=treeScroll.set, columns=cols, height=20)

for col, width in zip(cols, [70, 190, 200, 190, 70, 150, 180, 180, 70]):
    treeview.column(col, width=width)

treeview.pack()
treeScroll.config(command=treeview.yview)

load_data(1)
root.mainloop()
