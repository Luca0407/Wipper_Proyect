import tkinter as tk
from tkinter import ttk, messagebox
from getpath import getpath as gp
import sqlite3
from time import strftime


connect = sqlite3.connect('wipper.db')
cursor = connect.cursor()
init_path = gp.getPath()
cols = ("ID", "Marca", "Modelo", "Costo Inicial")

def close():
    root.destroy()

def load_data(x):
    match x:
        case 1:
            cursor.execute("SELECT ID_Products, brand, model, initial_cost FROM products")
            db_data = cursor.fetchall()


            for col_marca in cols:
                treeview.heading(col_marca, text=col_marca, anchor=tk.CENTER)
                treeview.column(col_marca, anchor=tk.CENTER)

        case 2:
            cursor.execute("""SELECT ID_Products, brand, model, initial_cost
                            FROM products ORDER BY ID_Products DESC LIMIT 1;""")
            db_data = cursor.fetchall()

    for value_tuple in db_data:
        treeview.insert('', tk.END, values=value_tuple)

def insert_row():
    columns = []
    values = []
    brand = brand_entry.get()
    model = model_entry.get()
    cost = cost_entry.get()
    
    if (brand_entry.get()) not in cols:
        columns.append('brand')
        values.append(brand)
    
    if (model_entry.get()) not in cols:
        columns.append('model')
        values.append(model)
    
    columns.append('initial_cost')
    values.append(cost)
    
    # Validación de campos vacíos
    if not all([brand, model, cost]):
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return 0
    
    query = f"INSERT INTO products ({', '.join(columns)}) VALUES ({', '.join(['?'] * len(values))})"
    cursor.execute(query, values)
    connect.commit()
    for i in range(1, 4):
        reset_entries(i)  # Reiniciar los campos
    load_data(2)

def reset_entries(x):
    match x:
        case 1:
            brand_entry.delete(0, "")
            brand_entry.insert(0, "Marca")
            
        case 2:
            model_entry.delete(0, "")
            model_entry.insert(0, "Modelo")
        
        case 3:
            cost_entry.delete(0, "")
            cost_entry.insert(0, "Costo Inicial")


def keep_used():
    if brand_entry.get() == "":
        reset_entries(1)

    if model_entry.get() == "":
        reset_entries(2)

    if cost_entry.get() == "":
        reset_entries(3)

def clear_entry(event, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, tk.END)

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

widgets_frame = ttk.LabelFrame(frame, text="Datos del Producto")
widgets_frame.grid(row=0, column=0, padx=20, pady=10)

# Entradas de texto
brand_entry = ttk.Entry(widgets_frame)
brand_entry.insert(0, "Marca")
brand_entry.bind("<FocusIn>", lambda e: clear_entry(e, brand_entry, "Marca"))
brand_entry.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")
brand_entry.bind("<FocusOut>", lambda e: keep_used())

model_entry = ttk.Entry(widgets_frame)
model_entry.insert(0, "Modelo")
model_entry.bind("<FocusIn>", lambda e: clear_entry(e, model_entry, "Modelo"))
model_entry.grid(row=1, column=0, padx=5, pady=(0, 5), sticky="ew")
model_entry.bind("<FocusOut>", lambda e: keep_used())

cost_entry = ttk.Entry(widgets_frame)
cost_entry.insert(0, "Costo Inicial")
cost_entry.bind("<FocusIn>", lambda e: clear_entry(e, cost_entry, "Costo Inicial"))
cost_entry.grid(row=2, column=0, padx=5, pady=(0, 5), sticky="ew")
cost_entry.bind("<FocusOut>", lambda e: keep_used())

separator = ttk.Separator(widgets_frame)
separator.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

def on_enter(event):
    button.invoke()

def on_escape(event):
    button_close.invoke()

root.bind('<Return>', on_enter)

root.bind('<Escape>', on_escape)

button = ttk.Button(widgets_frame, text="Agregar", command=insert_row)
button.grid(row=9, column=0, padx=5, pady=(0, 5), sticky="nsew")

button_close = ttk.Button(widgets_frame, text="Cerrar", command=close)
button_close.grid(row=10, column=0, padx=5, pady=(0, 5), sticky="nsew")

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

treeview = ttk.Treeview(treeFrame, show="headings",
    yscrollcommand=treeScroll.set, columns=cols, height=23)
treeview.column("ID", width=50)
treeview.column("Marca", width=292)
treeview.column("Modelo", width=296)
treeview.column("Costo Inicial", width=292)
treeview.pack()
treeScroll.config(command=treeview.yview)

load_data(1)
root.mainloop()
