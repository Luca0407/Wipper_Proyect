import tkinter as tk
from tkinter import ttk, messagebox
from getpath import getpath as gp
import sqlite3


connect = sqlite3.connect('wipper.db')  # Crea la conexión a la base de datos.
cursor = connect.cursor()
init_path = gp.getPath()  # Constante PATH obtiene la ubicación donde estan las imágenes.
cols = ("ID", "Nombre", "Apellido", "Teléfono")
root = tk.Tk()

def close():
    root.destroy()
    connect.close()

def load_data(x):
    match x:
        case 1:
            cursor.execute("SELECT * FROM clients")
            db_data = cursor.fetchall()

            for col_name in cols:
                treeview.heading(col_name, text=col_name, anchor=tk.CENTER)
                treeview.column(col_name, anchor=tk.CENTER)

        case 2:
            cursor.execute("SELECT * FROM clients ORDER BY ID_Clients DESC LIMIT 1;")
            db_data = cursor.fetchall()

    for value_tuple in db_data:
        treeview.insert('', tk.END, values=value_tuple)

def insert_row():
    columns = []
    values = []
    name = name_entry.get()
    surname = surname_entry.get()
    phone = phone_entry.get()

    if (name_entry.get()) not in cols:
        columns.append('owner_name')
        values.append(name)

    if (surname_entry.get()) not in cols:
        columns.append('owner_surname')
        values.append(surname)

    columns.append('phone')
    values.append(phone)

    client = cursor.execute("SELECT phone FROM clients")
    client_data = client.fetchall()
    for entry in client_data:
        if entry[0] == int(phone):
            messagebox.showwarning("Advertencia", "Este cliente ya se encuentra registrado")
            break
    else:
        query = f"INSERT INTO clients ({', '.join(columns)}) VALUES ({', '.join(['?'] * len(values))})"
        cursor.execute(query, values)
        connect.commit()
        for i in range(1, 4):
            reset_entries(i)

        load_data(2)

def reset_entries(x):
    match x:
        case 1:
            name_entry.delete(0, "")
            name_entry.insert(0, "Nombre")
            
        case 2:
            surname_entry.delete(0, "")
            surname_entry.insert(0, "Apellido")
        
        case 3:
            phone_entry.delete(0, "")
            phone_entry.insert(0, "Teléfono")
        
        

def keep_used():
    if name_entry.get() == "":
        reset_entries(1)

    if surname_entry.get() == "":
        reset_entries(2)

    if phone_entry.get() == "":
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

root.overrideredirect(True)
center_window(root, 1360, 550)

style = ttk.Style(root)
theme_path = rf"{init_path}\forest-dark.tcl"
root.tk.call('source', theme_path)
style.theme_use("forest-dark")

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text="Datos del Cliente")
widgets_frame.grid(row=0, column=0, padx=20, pady=10)


name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0, "Nombre")
name_entry.bind("<FocusIn>", lambda e: clear_entry(e, name_entry, "Nombre"))
name_entry.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")
name_entry.bind("<FocusOut>", lambda e: keep_used())

surname_entry = ttk.Entry(widgets_frame)
surname_entry.insert(0, "Apellido")
surname_entry.bind("<FocusIn>", lambda e: clear_entry(e, surname_entry, "Apellido"))
surname_entry.grid(row=1, column=0, padx=5, pady=(0, 5), sticky="ew")
surname_entry.bind("<FocusOut>", lambda e: keep_used())

phone_entry = ttk.Entry(widgets_frame)
phone_entry.insert(0, "Teléfono")
phone_entry.bind("<FocusIn>", lambda e: clear_entry(e, phone_entry, "Teléfono"))
phone_entry.grid(row=2, column=0, padx=5, pady=(0, 5), sticky="ew")
phone_entry.bind("<FocusOut>", lambda e: keep_used())

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
treeview.column("ID", width=30)
treeview.column("Nombre", width=300)
treeview.column("Apellido", width=300)
treeview.column("Teléfono", width=300)
treeview.pack()
treeScroll.config(command=treeview.yview)

load_data(1)
root.mainloop()
