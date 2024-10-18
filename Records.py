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

def load_data():
    cursor.execute(txt.queries()[0])

    db_data = cursor.fetchall()

    for col_marca in cols:
        treeview.heading(col_marca, text=col_marca, anchor=tk.CENTER)
        treeview.column(col_marca, anchor=tk.CENTER)

    for value_tuple in db_data:
        treeview.insert('', tk.END, values=value_tuple)


def center_window(window, width=800, height=600):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
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

def on_escape(event):
    button_close.invoke()

root.bind(txt.general()[14], on_escape)

button_close = ttk.Button(widgets_frame, text=txt.general()[25], command=close)
button_close.grid(row=0, column=2, padx=(20, 5), pady=(0, 5), sticky=txt.records()[10])

# --Crea y posiciona --
def on_enter(event):
    button_mod.invoke()

def modify():
    print("Modificando...")

button_mod = ttk.Button(widgets_frame, text=txt.records()[11], command=modify)
button_mod.grid(row=0, column=0, padx=(5, 20), pady=(0, 5), sticky=txt.records()[10])

def delete():
    print("Borrando...")

button_del = ttk.Button(widgets_frame, text=txt.records()[12], command=delete)
button_del.grid(row=0, column=1, padx=50, pady=(0, 5), sticky=txt.records()[10])

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

treeview = ttk.Treeview(treeFrame, show=txt.general()[19],
    yscrollcommand=treeScroll.set, columns=cols, height=20)
treeview.column(txt.records()[0], width=70)
treeview.column(txt.records()[1], width=190)
treeview.column(txt.records()[2], width=200)
treeview.column(txt.records()[3], width=190)
treeview.column(txt.records()[4], width=70)
treeview.column(txt.records()[5], width=150)
treeview.column(txt.records()[6], width=180)
treeview.column(txt.records()[7], width=180)
treeview.column(txt.records()[8], width=70)
treeview.pack()
treeScroll.config(command=treeview.yview)

load_data()
root.mainloop()
