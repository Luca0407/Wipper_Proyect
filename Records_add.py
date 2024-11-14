import tkinter as tk
from tkinter import ttk


root = tk.Tk()

# Mantener ventana siempre al frente y hacerla modal
root.attributes("-topmost", True)  # Ventana siempre al frente
root.grab_set()  # Captura eventos y bloquea acceso a otras ventanas


def center_window(window, width, height):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2) - 155
    window.geometry(f"{width}x{height}+{x}+{y}")

# Eliminar título y icono
root.title("")  # Elimina el título
root.iconbitmap("encargo.ico")  # Icono
center_window(root, 900, 90)


style = ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

clients_list = ["- Seleccione Cliente -","Agustín", "Luca", "Gonza", "Belén", "Profe"]

products_list = ["- Seleccione Producto -","Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5",
                  "Producto 6", "Producto 7", "Producto 8", "Producto 9", "Producto 10",
                    "Producto 11", "Producto 12", "Producto 13", "Producto 14", "Producto 15",
                      "Producto 16", "Producto 17", "Producto 18", "Producto 19", "Producto 20"]

services_list = ["- Seleccione Servicio -","Servicio 1", "Servicio 2", "Servicio 3", "Servicio 4", "Servicio 5"]

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text=("Encargo"))
widgets_frame.grid(row=10, column=10, padx=10, pady=10)

status_combobox = ttk.Combobox(widgets_frame, state="readonly", values=clients_list)
status_combobox.current(0)
status_combobox.grid(row=0, column=0,padx=(10, 20), pady=(5, 10), sticky="ew")

status_combobox = ttk.Combobox(widgets_frame, state="readonly", values=products_list)
status_combobox.current(0) 
status_combobox.grid(row=0, column=1,padx=(10, 20), pady=(5, 10), sticky="ew")

status_combobox = ttk.Combobox(widgets_frame, state="readonly", values=services_list)
status_combobox.current(0)
status_combobox.grid(row=0, column=2,padx=(10, 20), pady=(5, 10), sticky="ew")

button = ttk.Button(widgets_frame, text="Nuevo Servicio")
button.grid(row=0, column=3,padx=(10, 20), pady=(5, 10), sticky="ew")

button = ttk.Button(widgets_frame, text="Encargar", command=root.destroy)
button.grid(row=0, column=4,padx=(10, 10), pady=(5, 10), sticky="ew")

root.mainloop()