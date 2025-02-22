# --- Librerías y Módulos ---
import tkinter as tk
from tkinter import ttk, messagebox
from time import strftime
from db_manager import db_manager as db
from strings import strings as txt
from getpath import getpath as gp


general = txt.general()
mainmenu = txt.menu()
records = txt.records()
queries = txt.queries()


def center_window(window, width, height):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2) + 37
    window.geometry(f"{width}x{height}+{x}+{y}")

def on_double_click(event):
    """ Función que permite editar una celda al hacer doble clic """
    # Obtener el índice del item seleccionado
    item_id = treeview.focus()
    
    # Obtener coordenadas del clic
    col = treeview.identify_column(event.x)  # Columna en formato #n
    col_index = int(col[1:]) - 1  # Convertir a índice de lista (0 basado)

    if item_id and col_index >= 0:
        x, y, width, height = treeview.bbox(item_id, col_index)
        
        # Crear Entry y posicionarlo en la celda seleccionada
        entry = tk.Entry(window)
        entry.place(x=x+treeview.winfo_x(), y=y+treeview.winfo_y(), width=width, height=height)
        
        # Insertar texto actual en el Entry
        entry.insert(0, treeview.item(item_id, "values")[col_index])
        entry.focus()

        def save_edit(event):
            """ Guarda el texto ingresado en la celda """
            new_text = entry.get()
            values = list(treeview.item(item_id, "values"))
            values[col_index] = new_text
            treeview.item(item_id, values=values)
            entry.destroy()  # Elimina el Entry después de guardar

        # Guardar cambios al presionar "Enter"
        entry.bind("<Return>", save_edit)
        entry.bind("<FocusOut>", lambda e: entry.destroy())  # Cierra si pierde foco

def load_client(entry1, entry2, entry3):
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    
    if any("- Seleccione " in e for e in (e1, e2, e3)):
        messagebox.showerror(general[28], general[32])
        return
    
    try:
        params = (e3, e1, e2, 1, strftime(general[35]), strftime(general[35]), 0)
        db.other_queries(queries[12], params)
        messagebox.showinfo(records[15], records[16])
        load_data(2)
    except Exception as e:
        messagebox.showerror(records[17], str(e))

window = tk.Tk()
window.overrideredirect(True)
center_window(window, 1360, 550)

style = ttk.Style(window)
theme_path = rf"{gp.getPath()}\forest-dark.tcl"
window.tk.call(general[15], theme_path)
style.theme_use(general[16])

frame = ttk.Frame(window)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text=records[12])
widgets_frame.grid(row=0, column=0, padx=10, pady=10)

def nokeys(x):
    new_arr = []
    for i in x:
        new_arr.append(i.strip("{}"))
    return new_arr

cl = [row[0] for row in db.fetch_all("SELECT owner_name FROM clients;")]
cl.insert(0, records[18])
clients = nokeys(cl)

pr = [row[0] for row in db.fetch_all("SELECT concat(brand, ' ', model) FROM products;")]
pr.insert(0, records[19])
products = nokeys(pr)

sv = [row[0] for row in db.fetch_all("SELECT service_name FROM services;")]
sv.insert(0, records[20])
services = nokeys(sv)

clientsbox = ttk.Combobox(widgets_frame, state=records[13], values=clients)
clientsbox.current(0)
clientsbox.grid(row=0, column=0, padx=10, pady=10)

productsbox = ttk.Combobox(widgets_frame, state=records[13], values=products)
productsbox.current(0)
productsbox.grid(row=0, column=1, padx=10, pady=10)

servicesbox = ttk.Combobox(widgets_frame, state=records[13], values=services)
servicesbox.current(0)
servicesbox.grid(row=0, column=2, padx=10, pady=10)

button_new_service = ttk.Button(widgets_frame, text=records[21], command=lambda: print("en desarollo."))
button_new_service.grid(row=0, column=3, padx=10, pady=10)

button_submit = ttk.Button(widgets_frame, text=records[22], command=lambda: load_client(clientsbox, productsbox, servicesbox))
button_submit.grid(row=0, column=4, padx=10, pady=10)

button_close = ttk.Button(widgets_frame, text=general[25], command=window.destroy)
button_close.grid(row=0, column=5, padx=10, pady=10)

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=1, column=0, pady=20)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side=general[17], fill=general[18])

cols = (records[0], records[1], records[2], records[3], records[4], records[5], records[6], records[7])
treeview = ttk.Treeview(treeFrame, show=general[19], yscrollcommand=treeScroll.set, columns=cols, height=18)

for col, width in zip(cols, [200, 200, 200, 90, 160, 180, 180, 90]):
    treeview.column(col, width=width)
    treeview.heading(col, text=col, anchor=records[14])

treeview.bind("<Double-1>", on_double_click)

treeview.pack()
treeScroll.config(command=treeview.yview)

def load_data(x):
    query_map = {1: queries[0], 2: queries[7]}
    db_data = db.fetch_all(query_map.get(x))

    if x == 1:
        for col_marca in cols:
            treeview.heading(col_marca, text=col_marca, anchor=tk.CENTER)
            treeview.column(col_marca, anchor=tk.CENTER)

    for value_tuple in db_data:
        treeview.insert('', tk.END, values=value_tuple)

load_data(1)
window.mainloop()
