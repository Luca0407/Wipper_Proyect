import tkinter as tk
from tkinter import ttk, messagebox
from getpath import getpath as gp
import sqlite3
import time

connect = sqlite3.connect('wipper.db')  # Crea la conexión a la base de datos.
cursor = connect.cursor()
init_path = gp.getPath()  # Constante PATH obtiene la ubicación donde estan las imágenes.
cols = ("ID", "Marca", "Modelo", "Cantidad", "Fecha Ingreso")

def close():
    root.destroy()

def load_data():
    cursor.execute("SELECT ID_Products, brand, model, quantity, entry_date FROM products")
    db_data = cursor.fetchall()

    for col_marca in cols:
        treeview.heading(col_marca, text=col_marca, anchor=tk.CENTER)
        treeview.column(col_marca, anchor=tk.CENTER)

    for value_tuple in db_data:
        treeview.insert('', tk.END, values=value_tuple)

def insert_row():
    marca = marca_entry.get()
    cantidad = cantidad_entry.get()
    modelo = modelo_entry.get()
    fecha_ingreso = time.strftime('%d/%m/%y')
    
    # Validación de campos vacíos
    if not all([marca, cantidad, modelo]):
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return 0
    
    product = cursor.execute("SELECT brand, model, quantity FROM products")
    product_reg = product.fetchall()
    product_data = (marca, int(modelo), int(cantidad))
    for entry in product_reg:
        print(entry)
        if entry == product_data:
            messagebox.showwarning("Advertencia", "Este producto ya se encuentra registrado")
            break
    else:
        cursor.execute("""INSERT INTO products ('brand', 'model', 'quantity', 'entry_date')
                        VALUES (?, ?, ?, ?)""", (marca, modelo, cantidad, fecha_ingreso))
        connect.commit()
        reset_entries()  # Reiniciar los campos

def reset_entries():
    marca_entry.delete(0, "")
    marca_entry.insert(0, "Marca")
    modelo_entry.delete(0, "")
    modelo_entry.insert(0, "Modelo")
    cantidad_entry.delete(0, "")
    cantidad_entry.insert(0, "Cantidad")

def keep_used():
    if marca_entry.get() == "":
        reset_entries()

    if modelo_entry.get() == "":
        reset_entries()

    if cantidad_entry.get() == "":
        reset_entries()

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
marca_entry = ttk.Entry(widgets_frame)
marca_entry.insert(0, "Marca")
marca_entry.bind("<FocusIn>", lambda e: clear_entry(e, marca_entry, "Marca"))
marca_entry.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")
marca_entry.bind("<FocusOut>", lambda e: keep_used())

modelo_entry = ttk.Entry(widgets_frame)
modelo_entry.insert(0, "Modelo")
modelo_entry.bind("<FocusIn>", lambda e: clear_entry(e, modelo_entry, "Modelo"))
modelo_entry.grid(row=1, column=0, padx=5, pady=(0, 5), sticky="ew")
modelo_entry.bind("<FocusOut>", lambda e: keep_used())

cantidad_entry = ttk.Entry(widgets_frame)
cantidad_entry.insert(0, "Cantidad")
cantidad_entry.bind("<FocusIn>", lambda e: clear_entry(e, cantidad_entry, "Cantidad"))
cantidad_entry.grid(row=2, column=0, padx=5, pady=(0, 5), sticky="ew")
cantidad_entry.bind("<FocusOut>", lambda e: keep_used())

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
treeview.column("ID", width=20)
treeview.column("Marca", width=260)
treeview.column("Modelo", width=220)
treeview.column("Cantidad", width=210)
treeview.column("Fecha Ingreso", width=210)
treeview.pack()
treeScroll.config(command=treeview.yview)

load_data()
root.mainloop()
