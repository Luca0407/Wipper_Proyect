# --- Librerías y Módulos ---
import tkinter as tk
from tkinter import ttk, messagebox
from time import strftime
import sqlite3
from db_manager import db_manager as db
from strings import strings as txt
from getpath import getpath as gp


general = txt.general()
mainmenu = txt.menu()
records = txt.records()
queries = txt.queries()

connect = sqlite3.connect(general[13])
cursor = connect.cursor()


def center_window(window, width, height):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2) + 37
    window.geometry(f"{width}x{height}+{x}+{y}")


def load_client(entry1, entry2, entry3):
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    
    if any("- Seleccione " in e for e in (e1, e2, e3)):
        messagebox.showerror("ERROR", "Uno o más campos se encuentran vacíos.")
        return
    
    try:
        params = (e3, e1, e2, 1, strftime(mainmenu[1]), strftime(mainmenu[1]), 0)
        db.other_queries(queries[15], params)
        messagebox.showinfo("Éxito", "Registro agregado correctamente.")
        load_data(2)
    except Exception as e:
        messagebox.showerror("Error en la base de datos", str(e))

root = tk.Tk()
root.overrideredirect(True)
center_window(root, 1360, 550)

style = ttk.Style(root)
theme_path = rf"{gp.getPath()}\forest-dark.tcl"
root.tk.call(general[15], theme_path)
style.theme_use(general[16])

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text="Encargo")
widgets_frame.grid(row=0, column=0, padx=10, pady=10)

def nokeys(x):
    new_arr = []
    for i in x:
        new_arr.append(i.strip("{}"))
    return new_arr

cl = [row[0] for row in db.fetch_all(queries[12])]
cl.insert(0, "- Seleccione Cliente -")
clients = nokeys(cl)

pr = [row[0] for row in db.fetch_all(queries[13])]
pr.insert(0, "- Seleccione Producto -")
products = nokeys(pr)

sv = [row[0] for row in db.fetch_all(queries[14])]
sv.insert(0, "- Seleccione Servicio -")
services = nokeys(sv)

clientsbox = ttk.Combobox(widgets_frame, state="readonly", values=clients)
clientsbox.current(0)
clientsbox.grid(row=0, column=0, padx=10, pady=10)

productsbox = ttk.Combobox(widgets_frame, state="readonly", values=products)
productsbox.current(0)
productsbox.grid(row=0, column=1, padx=10, pady=10)

servicesbox = ttk.Combobox(widgets_frame, state="readonly", values=services)
servicesbox.current(0)
servicesbox.grid(row=0, column=2, padx=10, pady=10)

button_new_service = ttk.Button(widgets_frame, text="Nuevo Servicio", command=lambda: print("en desarollo."))
button_new_service.grid(row=0, column=3, padx=10, pady=10)

button_submit = ttk.Button(widgets_frame, text="Encargar", command=lambda: load_client(clientsbox, productsbox, servicesbox))
button_submit.grid(row=0, column=4, padx=10, pady=10)

button_close = ttk.Button(widgets_frame, text="Cerrar", command=root.destroy)
button_close.grid(row=0, column=5, padx=10, pady=10)

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=1, column=0, pady=20)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

cols = (records[0], records[1], records[2], records[3], records[4], records[5], records[6], records[7])
treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=cols, height=18)

for col, width in zip(cols, [200, 200, 200, 90, 160, 180, 180, 90]):
    treeview.column(col, width=width)
    treeview.heading(col, text=col, anchor="center")

treeview.pack()
treeScroll.config(command=treeview.yview)

def load_data(x):
    query_map = {1: queries[0], 2: queries[7]}
    cursor.execute(query_map.get(x))
    db_data = cursor.fetchall()

    if x == 1:
        for col_marca in cols:
            treeview.heading(col_marca, text=col_marca, anchor=tk.CENTER)
            treeview.column(col_marca, anchor=tk.CENTER)

    for value_tuple in db_data:
        treeview.insert('', tk.END, values=value_tuple)

load_data(1)

root.mainloop()
