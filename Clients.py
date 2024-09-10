import tkinter as tk
from tkinter import ttk, messagebox
from getpath import getpath as gp
import sqlite3


connect = sqlite3.connect('wipper.db')  # Crea la conexión a la base de datos.
cursor = connect.cursor()
init_path = gp.getPath()  # Constante PATH obtiene la ubicación donde estan las imágenes.

def close():
    root.destroy()

def insert_row():
    name = name_entry.get()
    lastname = lastname_entry.get()
    dni = dni_entry.get()
    postal = postal_entry.get()
    address = address_entry.get()
    cuit = cuit_entry.get()
    phone = phone_entry.get()
    mail = mail_entry.get()

    # Validación de campos vacíos
    if not all([name, lastname, dni, postal, address, cuit, phone, mail]):
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    treeview.insert('', tk.END, values= 0)

    # Reiniciar los campos
    reset_entries()

def reset_entries():
    name_entry.delete(0, "end")
    name_entry.insert(0, "Nombre")
    lastname_entry.delete(0, "end")
    lastname_entry.insert(0, "Apellido")
    dni_entry.delete(0, "end")
    dni_entry.insert(0, "DNI")
    postal_entry.delete(0, "end")
    postal_entry.insert(0, "Código Postal")
    address_entry.delete(0, "end")
    address_entry.insert(0, "Domicilio")
    cuit_entry.delete(0, "end")
    cuit_entry.insert(0, "CUIT")
    phone_entry.delete(0, "end")
    phone_entry.insert(0, "Teléfono")
    mail_entry.delete(0, "end")
    mail_entry.insert(0, "Correo Electrónico")

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

widgets_frame = ttk.LabelFrame(frame, text="Datos del Cliente")
widgets_frame.grid(row=0, column=0, padx=20, pady=10)

# Entradas de texto
name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0, "Nombre")
name_entry.bind("<FocusIn>", lambda e: clear_entry(e, name_entry, "Nombre"))
name_entry.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")

lastname_entry = ttk.Entry(widgets_frame)
lastname_entry.insert(1, "Apellido")
lastname_entry.bind("<FocusIn>", lambda e: clear_entry(e, lastname_entry, "Apellido"))
lastname_entry.grid(row=1, column=0, padx=5, pady=(0, 5), sticky="ew")

dni_entry = ttk.Entry(widgets_frame)
dni_entry.insert(0, "DNI")
dni_entry.bind("<FocusIn>", lambda e: clear_entry(e, dni_entry, "DNI"))
dni_entry.grid(row=2, column=0, padx=5, pady=(0, 5), sticky="ew")

postal_entry = ttk.Entry(widgets_frame)
postal_entry.insert(0, "Código Postal")
postal_entry.bind("<FocusIn>", lambda e: clear_entry(e, postal_entry, "Código Postal"))
postal_entry.grid(row=3, column=0, padx=5, pady=(0, 5), sticky="ew")

address_entry = ttk.Entry(widgets_frame)
address_entry.insert(0, "Domicilio")
address_entry.bind("<FocusIn>", lambda e: clear_entry(e, address_entry, "Domicilio"))
address_entry.grid(row=4, column=0, padx=5, pady=(0, 5), sticky="ew")

cuit_entry = ttk.Entry(widgets_frame)
cuit_entry.insert(0, "CUIT")
cuit_entry.bind("<FocusIn>", lambda e: clear_entry(e, cuit_entry, "CUIT"))
cuit_entry.grid(row=5, column=0, padx=5, pady=(0, 5), sticky="ew")

phone_entry = ttk.Entry(widgets_frame)
phone_entry.insert(0, "Teléfono")
phone_entry.bind("<FocusIn>", lambda e: clear_entry(e, phone_entry, "Teléfono"))
phone_entry.grid(row=6, column=0, padx=5, pady=(0, 5), sticky="ew")

mail_entry = ttk.Entry(widgets_frame)
mail_entry.insert(0, "Correo Electrónico")
mail_entry.bind("<FocusIn>", lambda e: clear_entry(e, mail_entry, "Correo Electrónico"))
mail_entry.grid(row=7, column=0, padx=5, pady=(0, 5), sticky="ew")

separator = ttk.Separator(widgets_frame)
separator.grid(row=8, column=0, padx=10, pady=10, sticky="ew")

button = ttk.Button(widgets_frame, text="Agregar", command=insert_row)
button.grid(row=9, column=0, padx=5, pady=(0, 5), sticky="nsew")

button_close = ttk.Button(widgets_frame, text="Cerrar", command=close)
button_close.grid(row=10, column=0, padx=5, pady=(0, 5), sticky="nsew")

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

cols = ("Nombre", "Apellido", "DNI", "Código Postal", "Domicilio", "CUIT",
        "Teléfono", "Correo Electrónico")
treeview = ttk.Treeview(treeFrame, show="headings",
                        yscrollcommand=treeScroll.set, columns=cols, height=23)
treeview.column("Nombre", width=100)
treeview.column("Apellido", width=100)
treeview.column("DNI", width=80)
treeview.column("Código Postal", width=100)
treeview.column("Domicilio", width=200)
treeview.column("CUIT", width=100)
treeview.column("Teléfono", width=100)
treeview.column("Correo Electrónico", width=250)
treeview.pack()
treeScroll.config(command=treeview.yview)

root.mainloop()
