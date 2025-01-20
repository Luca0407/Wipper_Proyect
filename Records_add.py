from pathlib import Path
import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox
from db_manager import db_manager as db
from strings import strings as txt
from getpath import getpath as gp
from time import strftime


def relative_to_assets(path: str) -> Path:
    PATH = gp.getPath()
    return PATH / Path(path)

root = tk.Tk()

general = txt.general()
mainmenu = txt.menu()

# Mantener ventana siempre al frente y hacerla modal
root.attributes("-topmost", True)  # Ventana siempre al frente
root.grab_set()  # Captura eventos y bloquea acceso a otras ventanas

def center_window(window, width, height):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Eliminar título y icono
center_window(root, 900, 120)
root.overrideredirect(True)
style = ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

clients = db.fetch_all("SELECT owner_name FROM clients")
clients.insert(0, "- Seleccione Cliente -")

products = db.fetch_all("SELECT concat(brand, ' ', model) FROM products")
products.insert(0, "- Seleccione Producto -")

services = db.fetch_all("SELECT service_name FROM services")
services.insert(0, "- Seleccione Servicio -")

def load_client(entry1, entry2, entry3):
    e1 = entry1.get().strip("{}")
    e2 = entry2.get().strip("{}")
    e3 = entry3.get().strip("{}")
    if any("- Seleccione " in e for e in (e1, e2, e3)):
        messagebox.showerror("ERROR", "Uno o más campos se encuentran vacíos.")
        return

    try:
        # Consulta combinada con subconsultas
        query = """
            INSERT INTO records (ID_Services, ID_Clients, ID_Products, quantity, entry_date, left_date, done)
            VALUES (
                (SELECT ID_Services FROM services WHERE service_name = ?),
                (SELECT ID_Clients FROM clients WHERE owner_name = ?),
                (SELECT ID_Products FROM products WHERE concat(brand, ' ', model) = ?),
                ?, ?, ?, ?
            )
        """
        params = (e3, e1, e2, 1, strftime(mainmenu[1]), strftime(mainmenu[1]), 1)
        print(e1, e2, e3)
        db.other_queries(query, params)

        messagebox.showinfo("Éxito", "Registro agregado correctamente.")
    except Exception as e:
        messagebox.showerror("Error en la base de datos", str(e))

frame = ttk.Frame(root)
frame.pack()

close_icon = PhotoImage(
    file=relative_to_assets(mainmenu[39]))

close = Button(
    image=close_icon,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: root.destroy(),
    relief=general[31]
)

close.place(
    x=860.0,
    y=5.0,
    width=26.0,
    height=26.0
)

widgets_frame = ttk.LabelFrame(frame, text=("Encargo"))
widgets_frame.grid(row=10, column=10, padx=10, pady=40)

clientsbox = ttk.Combobox(widgets_frame, state="readonly", values=clients)
clientsbox.current(0)
clientsbox.grid(row=0, column=0,padx=(10, 20), pady=(5, 10), sticky="ew")

productsbox = ttk.Combobox(widgets_frame, state="readonly", values=products)
productsbox.current(0) 
productsbox.grid(row=0, column=1,padx=(10, 20), pady=(5, 10), sticky="ew")

servicesbox = ttk.Combobox(widgets_frame, state="readonly", values=services)
servicesbox.current(0)
servicesbox.grid(row=0, column=2,padx=(10, 20), pady=(5, 10), sticky="ew")

brand_entry = ttk.Entry(widgets_frame), products[0]

button = ttk.Button(widgets_frame, text="Nuevo Servicio")
button.grid(row=0, column=3,padx=(10, 20), pady=(5, 10), sticky="ew")

button = ttk.Button(widgets_frame, text="Encargar", command=lambda: load_client(clientsbox, productsbox, servicesbox))
button.grid(row=0, column=4,padx=(10, 10), pady=(5, 10), sticky="ew")

root.resizable(False, False)
root.mainloop()