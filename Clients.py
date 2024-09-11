import tkinter as tk
from tkinter import ttk, messagebox
from getpath import getpath as gp
import sqlite3


connect = sqlite3.connect('wipper.db')  # Crea la conexión a la base de datos.
cursor = connect.cursor()
init_path = gp.getPath()  # Constante PATH obtiene la ubicación donde estan las imágenes.
cols = ("ID", "Dueño", "Teléfono", "DNI", "CUIT")

def close():
    root.destroy()

def load_data():
    cursor.execute("SELECT * FROM clients")
    db_data = cursor.fetchall()
    print(db_data)

    for col_name in cols:
        treeview.heading(col_name, text=col_name, anchor=tk.CENTER)
        treeview.column(col_name, anchor=tk.CENTER)

    for value_tuple in db_data:
        treeview.insert('', tk.END, values=value_tuple)

def insert_row():
    name = name_entry.get()
    dni = dni_entry.get()
    phone = phone_entry.get()
    cuit = cuit_entry.get()
    
    # Validación de campos vacíos
    if not all([name, dni, cuit, phone]):
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return 0
    
    client = cursor.execute("SELECT phone, doc_no, cuit FROM clients")
    client_reg = client.fetchall()
    client_data = (int(phone), int(dni), int(cuit))
    print(client_data)
    for entry in client_reg:
        print(entry)
        if entry == client_data:
            messagebox.showwarning("Advertencia", "Este cliente ya se encuentra registrado")
            break
    else:
        cursor.execute("""INSERT INTO clients ('owner_name', 'phone', 'doc_no', 'cuit')
                        VALUES (?, ?, ?, ?)""", (name, phone, dni, cuit))
        connect.commit()
        reset_entries()  # Reiniciar los campos
        load_data()

def reset_entries():
    name_entry.delete(0, "")
    name_entry.insert(0, "Nombre y Apellido")
    phone_entry.delete(0, "")
    phone_entry.insert(0, "Teléfono")
    dni_entry.delete(0, "")
    dni_entry.insert(0, "DNI")
    cuit_entry.delete(0, "")
    cuit_entry.insert(0, "CUIT")

def keep_used():
    if name_entry.get() == "":
        reset_entries()

    if phone_entry.get() == "":
        reset_entries()

    if dni_entry.get() == "":
        reset_entries()

    if cuit_entry.get() == "":
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

widgets_frame = ttk.LabelFrame(frame, text="Datos del Cliente")
widgets_frame.grid(row=0, column=0, padx=20, pady=10)

# Entradas de texto
name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0, "Nombre y Apellido")
name_entry.bind("<FocusIn>", lambda e: clear_entry(e, name_entry, "Nombre y Apellido"))
name_entry.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")
name_entry.bind("<FocusOut>", lambda e: keep_used())

phone_entry = ttk.Entry(widgets_frame)
phone_entry.insert(0, "Teléfono")
phone_entry.bind("<FocusIn>", lambda e: clear_entry(e, phone_entry, "Teléfono"))
phone_entry.grid(row=1, column=0, padx=5, pady=(0, 5), sticky="ew")
phone_entry.bind("<FocusOut>", lambda e: keep_used())

dni_entry = ttk.Entry(widgets_frame)
dni_entry.insert(0, "DNI")
dni_entry.bind("<FocusIn>", lambda e: clear_entry(e, dni_entry, "DNI"))
dni_entry.grid(row=2, column=0, padx=5, pady=(0, 5), sticky="ew")
dni_entry.bind("<FocusOut>", lambda e: keep_used())

cuit_entry = ttk.Entry(widgets_frame)
cuit_entry.insert(0, "CUIT")
cuit_entry.bind("<FocusIn>", lambda e: clear_entry(e, cuit_entry, "CUIT"))
cuit_entry.grid(row=3, column=0, padx=5, pady=(0, 5), sticky="ew")
cuit_entry.bind("<FocusOut>", lambda e: keep_used())

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
treeview.column("Dueño", width=260)
treeview.column("Teléfono", width=220)
treeview.column("DNI", width=210)
treeview.column("CUIT", width=220)
treeview.pack()
treeScroll.config(command=treeview.yview)

load_data()
root.mainloop()
