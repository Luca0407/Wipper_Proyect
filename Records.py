import tkinter as tk
from tkinter import ttk
from getpath import getpath as gp
import sqlite3

connect = sqlite3.connect('wipper.db')
cursor = connect.cursor()
init_path = gp.getPath()
cols = ("Servicio", "Cliente", "Producto", "Nombre del Servicio", "Cantidad", "Precio Final", "Fecha de Ingreso", "Fecha de Egreso", "Hecho")

def close():
    root.destroy()

def load_data():
    cursor.execute("""SELECT ID_Services, concat('(', clients.ID_Clients, ') - ', clients.owner_name), concat(products.brand, ' ', products.model),
                service_name, quantity, sum(products.initial_cost * quantity + aditional_cost ), entry_date, left_date, done
        FROM services
        JOIN clients ON
            services.ID_Clients = clients.ID_Clients
        JOIN products ON
            services.ID_Products = products.ID_Products
        GROUP BY ID_Services;""")

    db_data = cursor.fetchall()

    for col_marca in cols:
        treeview.heading(col_marca, text=col_marca, anchor=tk.CENTER)
        treeview.column(col_marca, anchor=tk.CENTER)

    for value_tuple in db_data:
        treeview.insert('', tk.END, values=value_tuple)

# Función para centrar la ventana en la pantalla, pero 37px más abajo
def center_window(window, width=800, height=600):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2) + 37  # Mueve la ventana 37px hacia abajo
    window.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()

# Ocultar la barra superior (title bar)
root.overrideredirect(True)

# Centrar la ventana en la pantalla y moverla 37px hacia abajo
center_window(root, 1360, 550)

style = ttk.Style(root)
theme_path = rf"{init_path}\forest-dark.tcl"
root.tk.call('source', theme_path)
style.theme_use("forest-dark")

frame = ttk.Frame(root)
frame.pack()

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")
widgets_frame = ttk.LabelFrame(frame, text="Comandos")
widgets_frame.grid(row=1, column=1, padx=1, pady=0)

def on_escape(event):
    button_close.invoke()

root.bind('<Escape>', on_escape)

button_close = ttk.Button(widgets_frame, text="Cerrar", command=close)
button_close.grid(row=0, column=2, padx=(20, 5), pady=(0, 5), sticky="ns")

# --Crea y posiciona --
def on_enter(event):
    button_mod.invoke()

def modify():
    print("Modificando...")

button_mod = ttk.Button(widgets_frame, text="Modificar", command=modify)
button_mod.grid(row=0, column=0, padx=(5, 20), pady=(0, 5), sticky="ns")

def delete():
    print("Borrando...")

button_del = ttk.Button(widgets_frame, text="Borrar", command=delete)
button_del.grid(row=0, column=1, padx=50, pady=(0, 5), sticky="ns")

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

treeview = ttk.Treeview(treeFrame, show="headings",
    yscrollcommand=treeScroll.set, columns=cols, height=20)
treeview.column("Servicio", width=70)
treeview.column("Cliente", width=190)
treeview.column("Producto", width=200)
treeview.column("Nombre del Servicio", width=190)
treeview.column("Cantidad", width=70)
treeview.column("Precio Final", width=150)
treeview.column("Fecha de Ingreso", width=180)
treeview.column("Fecha de Egreso", width=180)
treeview.column("Hecho", width=70)
treeview.pack()
treeScroll.config(command=treeview.yview)
load_data()
root.mainloop()
