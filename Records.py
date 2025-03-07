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
    """Permite editar una celda con un OptionMenu al hacer doble clic"""
    item_id = treeview.focus()  # Obtener el ID del ítem seleccionado
    col = treeview.identify_column(event.x)  # Columna en formato #n
    col_index = int(col[1:]) - 1  # Convertir a índice (0 basado)
    valor = []
    valor.append(treeview.item(item_id, "values")[col_index])
    if not item_id or col_index < 0:
        return  # Evita errores si no hay selección válida

    bbox = treeview.bbox(item_id, col_index)
    if not bbox:
        return  # Evita errores si bbox es None

    x, y, width, height = bbox

    # Obtener el valor actual de la celda
    current_value = treeview.item(item_id, "values")[col_index]
    date = treeview.item(item_id, "values")[5]
    
    # Opciones del OptionMenu (puedes personalizar estas opciones)
    cl = [row[0] for row in db.fetch_all("SELECT owner_name FROM clients;")]
    cl.insert(0, records[18])
    clients = nokeys(cl)
    
    pr = [row[0] for row in db.fetch_all("SELECT product_name FROM products;")]
    pr.insert(0, records[19])
    products = nokeys(pr)
    
    sv = [row[0] for row in db.fetch_all("SELECT service_name FROM services;")]
    sv.insert(0, records[20])
    services = nokeys(sv)

    done = ["-", "✔", "✘"]

    departure = ["-", f"{strftime(general[35])}"]

    # Crear una variable de control para el OptionMenu
    global var2
    var = tk.StringVar()
    var2 = tk.StringVar()
    var.set(current_value)
    var2.set(date)
    print("xd", var.get())
    print("xd", var2.get())
    match col_index:
        case 0:
            option_menu = tk.OptionMenu(treeview, var, *clients, command=lambda value: save_edit(value, item_id, col_index, option_menu, valor, var))
        case 1:
            option_menu = tk.OptionMenu(treeview, var, *products, command=lambda value: save_edit(value, item_id, col_index, option_menu, valor, var))
        case 2:
            option_menu = tk.OptionMenu(treeview, var, *services, command=lambda value: save_edit(value, item_id, col_index, option_menu, valor, var))
        case 3:
            vcmd = (window.register(only_numbers_input), "%P")
            option_menu = tk.Entry(treeview, validate="key", validatecommand=vcmd)
            option_menu.insert(0, treeview.item(item_id, "values")[col_index])  # Insertar valor actual
            option_menu.bind("<Return>", lambda event: on_return(event, option_menu, item_id, col_index))  # Verificar antes de guardar
        case 6:
            option_menu = tk.OptionMenu(treeview, var, *departure, command=lambda value: save_edit(value, item_id, col_index, option_menu, valor, var))
        case 7:
            option_menu = tk.OptionMenu(treeview, var, *done, command=lambda value: save_edit(value, item_id, col_index, option_menu, valor, var))
        case other:
            return

    option_menu.place(x=x + treeview.winfo_x(), y=y + treeview.winfo_y(), width=width, height=height)
    option_menu.focus()

    # Destruir OptionMenu si pierde el foco
    option_menu.bind("<FocusOut>", lambda e: option_menu.destroy())

def only_numbers_input(P):
    return P.isdigit() or P == ""

def save_edit(value, item_id, col_index, option_menu, valor, var):
    """Guarda el valor seleccionado en la celda"""
    values = list(treeview.item(item_id, "values"))
    values[col_index] = value
    treeview.item(item_id, values=values)

    match col_index:
        case 0:
            nuevo_valor = var.get()
            print(dbcols[col_index], nuevo_valor, valor[0])
            check = f"""SELECT ID_Services, ID_Products, quantity, entry_date FROM records r
            JOIN clients c ON r.ID_Clients = c.ID_Clients WHERE c.owner_name = '{nuevo_valor}';"""
            checking = db.fetch_all(check)
            new = f"""SELECT ID_Services, ID_Products, quantity, entry_date FROM records r
            JOIN clients c ON r.ID_Clients = c.ID_Clients WHERE c.owner_name = '{valor[0]}'
            AND left_date = '-' AND done = '-';"""
            to_check = db.fetch_all(new)
            print(checking)
            print(to_check)
            for i in checking:
                for j in to_check:
                    print("itemj", j)
                    print("itemi", i)
                    if i == j:
                        print("si", i == j)
                        messagebox.showwarning("Fila duplicada", "Realizar esta modificación duplicará una fila ya existente.")
                        return

            query = f"""UPDATE records SET {dbcols[col_index]} = 
            (SELECT {dbcols[col_index]} FROM clients WHERE owner_name = '{nuevo_valor}')
            WHERE ROWID = 
            (SELECT ROWID FROM records WHERE {dbcols[col_index]} = 
            (SELECT {dbcols[col_index]} FROM clients WHERE owner_name = '{valor[0]}')
            AND left_date = '-' AND done = '-' ORDER BY ROWID DESC);"""
            db.commit(query)

        case 1:
            nuevo_valor = var.get()
            print(dbcols[col_index], nuevo_valor, valor[0])
            check = f"""SELECT r.ID_Services, r.ID_Clients, r.quantity, r.entry_date FROM records r
            JOIN products p ON r.ID_Products = p.ID_Products WHERE p.product_name = '{nuevo_valor}';"""
            checking = db.fetch_all(check)
            new = f"""SELECT r.ID_Services, r.ID_Clients, r.quantity, r.entry_date FROM records r
            JOIN products p ON r.ID_Products = p.ID_Products WHERE p.product_name = '{valor[0]}'
            AND left_date = '-' AND done = '-';"""
            to_check = db.fetch_all(new)
            print(checking)
            print(to_check)
            for i in checking:
                for j in to_check:
                    print("itemj", j)
                    print("itemi", i)
                    if i == j:
                        print("si", i == j)
                        messagebox.showwarning("Fila duplicada", "Realizar esta modificación duplicará una fila ya existente.")
                        return

            query = f"""UPDATE records SET {dbcols[col_index]} = 
            (SELECT {dbcols[col_index]} FROM products WHERE product_name = '{nuevo_valor}')
            WHERE ROWID = 
            (SELECT ROWID FROM records WHERE {dbcols[col_index]} = 
            (SELECT {dbcols[col_index]} FROM products WHERE product_name = '{valor[0]}')
            AND left_date = '-' AND done = '-' ORDER BY ROWID DESC);"""
            db.commit(query)

        case 2:
            nuevo_valor = var.get()
            print(dbcols[col_index], "xd", nuevo_valor, valor[0])
            check = f"""SELECT r.ID_Clients, r.ID_Products, r.quantity, r.entry_date FROM records r
            JOIN services s ON r.ID_Services = s.ID_Services WHERE s.service_name = '{nuevo_valor}'
            AND r.entry_date = '{var2.get()}';"""
            checking = db.fetch_all(check)
            new = f"""SELECT r.ID_Clients, r.ID_Products, r.quantity, r.entry_date FROM records r
            JOIN services s ON r.ID_Services = s.ID_Services WHERE s.service_name = '{valor[0]}'
            AND left_date = '-' AND done = '-';"""
            to_check = db.fetch_all(new)
            print("nuevoxd", checking)
            print("viejoxd", to_check)
            for i in checking:
                for j in to_check:
                    print("nuevo", j)
                    print("viejo", i)
                    if i == j:
                        print("si", i == j)
                        messagebox.showwarning("Fila duplicada", "Realizar esta modificación duplicará una fila ya existente.")
                        return

            query = f"""UPDATE records SET {dbcols[col_index]} = 
            (SELECT {dbcols[col_index]} FROM services WHERE service_name = '{nuevo_valor}')
            WHERE ROWID = 
            (SELECT ROWID FROM records WHERE {dbcols[col_index]} = 
            (SELECT {dbcols[col_index]} FROM services WHERE service_name = '{valor[0]}')
            AND left_date = '-' AND done = '-' ORDER BY ROWID DESC);"""
            db.commit(query)

        case 6:
            nuevo_valor = var.get()  # Obtener el valor seleccionado del OptionMenu
            query = f"UPDATE records SET {dbcols[col_index]} = '{nuevo_valor}' WHERE {dbcols[col_index]} = '{valor[0]}';"
            db.commit(query)

        case 7:
            nuevo_valor = var.get()  # Obtener el valor seleccionado del OptionMenu
            query = f"UPDATE records SET {dbcols[col_index]} = '{nuevo_valor}' WHERE {dbcols[col_index]} = '{valor[0]}';"
            db.commit(query)

    option_menu.destroy()  # Eliminar OptionMenu después de guardar

def on_return(event, option_menu, item_id, col_index):
    valor = []
    valor.append(treeview.item(item_id, "values")[col_index])
    if option_menu.get().strip() == "":  # Verifica si el Entry está vacío
        messagebox.showwarning("ADVERTENCIA", "El campo no puede estar vacío.")
        return "break"  # Impide que se ejecute el comando asociado al Return
    
    query = f"UPDATE records SET {dbcols[col_index]} = {option_menu.get()} WHERE ID_Records = (SELECT ID_Records FROM records WHERE quantity = {valor[0]})"
    db.commit(query)
    save_edit(option_menu.get(), item_id, col_index, option_menu, valor)

def load_client(entry1, entry2, entry3):
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()

    if any("- Seleccione " in e for e in (e1, e2, e3)):
        messagebox.showerror(general[28], general[32])
        return
    try:
        params = (e3, e1, e2)
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

pr = [row[0] for row in db.fetch_all("SELECT product_name FROM products;")]
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
dbcols = ("ID_Clients", "ID_Products", "ID_Services", "quantity", "Precio Final", "Fecha de Ingreso", "left_date", "done",)
treeview = ttk.Treeview(treeFrame, show=general[19], yscrollcommand=treeScroll.set, columns=cols, height=18)

for col, width in zip(cols, [200, 200, 200, 90, 160, 180, 180, 90]):
    treeview.column(col, width=width)
    treeview.heading(col, text=col, anchor=records[14])

treeview.bind("<Double-1>", on_double_click)

treeview.pack()
treeScroll.config(command=treeview.yview)

treeview.bind("<Double-1>", on_double_click)

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
