# --- Librerías y módulos ---
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, messagebox, Frame, ttk
from getpath import getpath as gp
from users import users
from time import strftime
from strings import strings as txt
import sys
import tkinter as tk
from db_manager import db_manager as db
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


general = txt.general()
mainmenu = txt.menu()
products = txt.products()
clients = txt.clients()
queries = txt.queries()
records = txt.records()
window = Tk()
username = users.current_user()
window.attributes("-topmost", True)

if username is None:
    window.destroy()
    gp.vxl(general[30])
    sys.exit()

def only_numbers_input(P):
    return P.isdigit() or P == ""

vcmd = (window.register(only_numbers_input), "%P")

def relative_to_assets(path: str) -> Path:
    PATH = gp.getPath()
    return PATH / Path(path)


# --- Movimiento de la ventana ---
def start_move(event):
    if event.y <= 30:
        window.x, window.y = event.x, event.y
    else:
        window.x, window.y = None, None


def do_move(event):
    if window.x is not None and window.y is not None:
        deltax = event.x - window.x
        deltay = event.y - window.y
        x = window.winfo_x() + deltax
        y = window.winfo_y() + deltay
        window.geometry(f"+{x}+{y}")
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# --- Fecha y hora ---
def update_clock_and_date(win, clock_text, date_text):
    current_time = strftime(mainmenu[0])
    win.itemconfig(clock_text, text=current_time)

    current_date = strftime(general[35])
    win.itemconfig(date_text, text=current_date)

    win.after(1000, update_clock_and_date, win, clock_text, date_text)  # Llama de nuevo después de 1 segundo

# --- Cierre de sesión ---
def logout():
    window.destroy()
    users.logout(username)
    gp.vxl(general[30])
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

def center_window(window, width, height):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

window.overrideredirect(True)
center_window(window, 1360, 728)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

canvas = Canvas(
    window,
    bg = general[0],
    height = 728,
    width = 1360,
    bd = 0,
    highlightthickness = 0,
    relief = general[34])

canvas.place(x = 0, y = 0)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# Lista con las configuraciones de imágenes
images = [
    (mainmenu[7],  680.0, 404.0), 
    (mainmenu[8],  499.0, 392.0), 
    (mainmenu[9],  680.0, 15.0),  
    (mainmenu[10], 680.0, 80.0),  
    (mainmenu[11], 680.0, 703.0), 
    (mainmenu[12], 28.0,  15.0),  
    (mainmenu[13], 24.0,  703.0), 
    (mainmenu[14], 1131.0, 703.0),
    (mainmenu[15], 1275.0, 703.0),
    (mainmenu[16], 1290.0, 14.5),
    (mainmenu[17], 1335.0, 14.5),
    (mainmenu[18], 1200.0, 79.3),
    (mainmenu[20], 150.0, 79.3),
    (mainmenu[1], 413, 83),
    (mainmenu[3], 954, 83),
    (mainmenu[5], 680, 83)
    ]

image_references = {}
# Diccionarios para almacenar posiciones de imágenes
image_positions = {}

# Crear y posicionar imágenes en el canvas
for index, (image_path, x, y) in enumerate(images):
    image_references[f"img_{index}"] = PhotoImage(file=relative_to_assets(image_path))
    
    # Guardamos la posición de la imagen en el diccionario
    image_positions[f"img_{index}"] = (x, y)
    
    # Crear la imagen en el canvas con una etiqueta
    canvas.create_image(x, y, image=image_references[f"img_{index}"], tags=f"img_{index}")

button_images = {
    "img_1": {
        "original": image_references["img_13"],
        "alternative": PhotoImage(file=relative_to_assets(mainmenu[2]))
    },
    "img_2": {
        "original": image_references["img_14"],
        "alternative": PhotoImage(file=relative_to_assets(mainmenu[4]))
    },
    "img_3": {
        "original": image_references["img_15"],
        "alternative": PhotoImage(file=relative_to_assets(mainmenu[6]))
    },
}

def cambiar_imagen_boton(btn, image_type, button_key, func=None):
    if image_type == "alternative":
        btn.configure(image=button_images[button_key]["alternative"])
    else:
        btn.configure(image=button_images[button_key]["original"])
    btn.master.update()
    if func:
            func()

button_data = [
    (image_references["img_12"], lambda: messagebox.showinfo(mainmenu[21], mainmenu[22]), 60.0, 51),
    (image_references["img_13"], lambda: (cambiar_imagen_boton(buttons_dict["img_1"], "alternative", "img_1", cli_frame())), 315, 51),
    (image_references["img_14"], lambda: (cambiar_imagen_boton(buttons_dict["img_2"], "alternative", "img_2", rec_frame())), 855, 51),
    (image_references["img_15"], lambda: (cambiar_imagen_boton(buttons_dict["img_3"], "alternative", "img_3", prod_frame())), 585, 51),
    (image_references["img_9"], lambda: print("minimize clicked"), 1280.0, 2),  # Minimizar
    (image_references["img_10"], window.destroy, 1325, 2),  # Cerrar
    (image_references["img_11"], logout, 1100, 51),  # Logout
]

buttons_dict = {}  # Diccionario para almacenar referencias a botones
buttons = []

for index, (img, cmd, x, y) in enumerate(button_data):
    btn = Button(
        image=img,
        borderwidth=0,
        highlightthickness=0,
        command=cmd,
        relief=general[31]
    )
    buttons_dict[f"img_{index}"] = btn  # Guardamos la referencia del botón en el diccionario
    # Colocamos los botones en el canvas
    if str(img) in ("pyimage12", "pyimage13", "pyimage14", "pyimage15", "pyimage16"):
        btn.place(x=x, y=y, width=190, height=60)
    else:
        btn.place(x=x, y=y, width=26, height=26)

    buttons.append(btn)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
prod = buttons_dict["img_3"]
rec = buttons_dict["img_2"]
cli = buttons_dict["img_1"]

# Lista con las configuraciones de los textos
texts = [
    (726.0, 356.0, mainmenu[25], mainmenu[26], mainmenu[27], 16),  # Teclas rápidas
    (726.0, 288.0, mainmenu[28], mainmenu[26], mainmenu[27], 36),  
    (14.0, 657.0, mainmenu[29], mainmenu[26], mainmenu[27], 10),   # Versión
    (58.0, 7.0, mainmenu[30], general[11], mainmenu[31], 13),      # Otro texto
    (44.0, 695.0, username, general[11], mainmenu[31], 13)         # Usuario
]

# Crear los textos dinámicamente
for x, y, text, fill, font_family, font_size in texts:
    canvas.create_text(
        x, y, anchor=general[9], text=text, fill=fill, font=(font_family, font_size * -1))

# Crear los textos del reloj y la fecha
clock_text = canvas.create_text(
    1295.0, 695.0, anchor=general[9], text="", fill=general[11], font=(mainmenu[31], 13 * -1))
date_text = canvas.create_text(
    1151.0, 695.0, anchor=general[9], text="", fill=general[11], font=(mainmenu[31], 13 * -1))

# Inicia la actualización del reloj
update_clock_and_date(canvas, clock_text, date_text)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

def nokeys(x):
    new_arr = []
    for i in x:
        new_arr.append(i.strip("{}"))
    return new_arr

def load_client(entry1, entry2, entry3, entry4):
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()

    if any("- Seleccione " in e for e in (e1, e2, e3)):
        messagebox.showerror(general[28], general[32])
        return
    try:
        params = (e3, e1, e2, e4)
        db.other_queries(queries[12], params)
        messagebox.showinfo(records[15], records[16])
        # load_data(2)
    except Exception as e:
        messagebox.showerror(records[17], str(e))

def toggle_frame(frame, visible):
    if visible:
        frame.place_forget()
    else:
        frame.place(x=0, y=131)

    visible = not visible

style = ttk.Style(window)
tclpath = gp.getPath().parents[3]
theme_path = rf"{tclpath}\forest-dark.tcl"
window.tk.call(general[15], theme_path)
style.theme_use(general[16])

def prod_frame():
    dbcols = ("ID_Products", "product_name", "initial_cost")
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
        rid = treeview.item(item_id, "values")[0]

        # Crear una variable de control para el OptionMenu
        global varid
        var = tk.StringVar()
        varid = tk.StringVar()
        varid.set(rid)
        var.set(current_value)
        match col_index:
            case 1:
                option_menu = tk.Entry(treeview)
                option_menu.insert(0, treeview.item(item_id, "values")[col_index])  # Insertar valor actual
                option_menu.bind("<Return>", lambda event: on_return(event, option_menu, col_index))  # Verificar antes de guardar
            case 2:
                vcmd = (window.register(only_numbers_input), "%P")
                option_menu = tk.Entry(treeview, validate="key", validatecommand=vcmd)
                option_menu.insert(0, treeview.item(item_id, "values")[col_index])  # Insertar valor actual
                option_menu.bind("<Return>", lambda event: on_return(event, option_menu, col_index))  # Verificar antes de guardar
            case other:
                return

        option_menu.place(x=x + treeview.winfo_x(), y=y + treeview.winfo_y(), width=width, height=height)
        option_menu.focus()

        # Destruir OptionMenu si pierde el foco
        option_menu.bind("<FocusOut>", lambda e: option_menu.destroy())
    
    def on_return(event, option_menu, col_index):
        check = f"SELECT product_name FROM products WHERE product_name = '{option_menu.get().strip()}';"
        checking = db.fetch_all(check)
        if checking != []:
            print("si", checking)
            messagebox.showwarning(f"{cols[col_index]} duplicado", f"Realizar esta modificación duplicará un {cols[col_index].lower()} ya existente.")
            load_data(1)
            return
        if option_menu.get().strip() == "":  # Verifica si el Entry está vacío
            messagebox.showwarning("ADVERTENCIA", "El campo no puede estar vacío.")
            return "break"  # Impide que se ejecute el comando asociado al Return
        query = f"UPDATE products SET '{dbcols[col_index]}' = '{option_menu.get()}' WHERE ID_Products = '{varid.get()}';"
        db.commit(query)
        option_menu.destroy()  # Eliminar OptionMenu después de guardar
        load_data(1)
    
    def load_data(x):
        query_map = {1: queries[4], 2: queries[5]}
        db_data = db.fetch_all(query_map.get(x))

        if x == 1:
            for col_marca in cols:
                treeview.heading(col_marca, text=col_marca, anchor=tk.CENTER)
                treeview.column(col_marca, anchor=tk.CENTER)

            treeview.delete(*treeview.get_children())

        for value_tuple in db_data:
            treeview.insert('', tk.END, values=value_tuple)
    
    def delete_row():
        item_id = treeview.focus()  # Obtener el ID del ítem seleccionado
        if item_id == "":
            messagebox.showerror("ERROR", "Ninguna fila se encuentra seleccionada")
            return
        rid = treeview.item(item_id, "values")[0]
        varid = tk.StringVar()
        varid.set(rid)
        query = f"DELETE FROM products WHERE ID_Products = '{varid.get()}'"
        db.commit(query)
        load_data(1)
    
    def reset_entries(x):
        match x:
            case 1:
                product_entry.delete(0, "")
                product_entry.insert(0, products[0])

            case 2:
                cost_entry.delete(0, tk.END)
                cost_entry.insert(0, products[1])
                on_focus_out("<FocusOut>")
    
    def keep_used():
        if product_entry.get().strip() == "":
            reset_entries(1)
        if cost_entry.get().strip() == "":
            reset_entries(2)

    def clear_entry(event, entry, default_text):
        if entry.get() == default_text:
            entry.delete(0, tk.END)
    
    def insert_row():
        product_name, cost = product_entry.get(), cost_entry.get()

        if product_name != products[0]:
            product_name = product_name.strip().upper()
        else:
            messagebox.showerror(general[28], "Producto invalido")
            return

        if cost == products[1]:
            messagebox.showerror(general[28], products[6])
            return

        product_data = db.fetch_all(queries[6])
        if any(entry[0] == product_name for entry in product_data):
            messagebox.showwarning(general[27], products[5])
            return

        query = f"INSERT INTO products (product_name, initial_cost) VALUES ('{product_name}', {cost})"
        db.commit(query)
        
        for i in range(1, 3):
            print(i)
            reset_entries(i)
        load_data(2)
    
    frame_container = Frame(window, width=1360, height=550, bg="#333")
    frame_container_visible = False
    frame_container.place_forget()
    
    toggle_frame(frame_container, frame_container_visible)
    
    products_frame = ttk.LabelFrame(frame_container, text=products[4])
    products_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    delete_frame = ttk.LabelFrame(frame_container)
    delete_frame.grid(row=0, column=0, padx=10, pady=10, sticky="s")
    
    button_delete = ttk.Button(delete_frame, text="Eliminar", command=lambda: delete_row())
    button_delete.grid(row=0, column=0, padx=10, pady=10)
    
    product_entry = ttk.Entry(products_frame)
    cost_entry = ttk.Entry(products_frame, validate="none", validatecommand=vcmd)
    entries = [(product_entry, products[0]), (cost_entry, products[1])]

    for i, (entry, default_text) in enumerate(entries):
        entry.insert(0, default_text)
        entry.bind(general[21], lambda e, entry=entry, dt=default_text: clear_entry(e, entry, dt))
        entry.grid(row=i, column=0, padx=5, pady=(0, 5), sticky=general[22])
        entry.bind(general[23], lambda e: keep_used())

    separator = ttk.Separator(products_frame)
    separator.grid(row=3, column=0, padx=10, pady=10, sticky=general[22])

    button = ttk.Button(products_frame, text=general[24], command=lambda: insert_row())
    button.grid(row=4, column=0, padx=5, pady=(0, 5), sticky=general[26])
    
    button_close = ttk.Button(products_frame, text=general[25], command=lambda: cambiar_imagen_boton(prod, "original", "img_3", toggle_frame(frame_container, True)))
    button_close.grid(row=5, column=0, padx=5, pady=(0, 5), sticky=general[26])
    
    treeFrame = ttk.Frame(frame_container)
    treeFrame.grid(row=0, column=1, padx= 101, pady=3)
    
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side=general[17], fill=general[18])
    
    treeview = ttk.Treeview(treeFrame, show=general[19], yscrollcommand=treeScroll.set, columns=[], height=24)
    
    cols = (general[20], products[0], products[1])
    treeview.config(columns=cols)
    for col, width in zip(cols, [300, 300, 300]):
        treeview.column(col, width=width)
        treeview.heading(col, text=col, anchor=records[14])
    
    treeview.pack()
    treeScroll.config(command=treeview.yview)
    
    def on_focus_in(event):
        """Borra el placeholder cuando el usuario hace clic en el Entry."""
        if cost_entry.get() == products[1]:
            cost_entry.config(validate="none")  # Desactivar validación temporalmente
            cost_entry.delete(0, tk.END)
            cost_entry.config(validate="key")  # Restaurar validación

    def on_focus_out(event):
        """Si el campo queda vacío, vuelve a poner el placeholder."""
        if not cost_entry.get():
            cost_entry.config(validate="none")  # Desactivar validación para insertar texto
            cost_entry.insert(0, products[1])
            cost_entry.config(validate="key")  # Restaurar validación
    
    window.bind(general[14], lambda e: button_close.invoke())
    treeview.bind("<Double-1>", on_double_click)
    cost_entry.bind("<FocusIn>", on_focus_in)
    cost_entry.bind("<FocusOut>", on_focus_out)
    load_data(1)

def rec_frame():
    dbcols = ("ID_Clients", "ID_Products", "ID_Services", "quantity", "Precio Final", "Fecha de Ingreso", "left_date", "done", "ID_Records")
    
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
        rid = treeview.item(item_id, "values")[8]

        # Opciones del OptionMenu (puedes personalizar estas opciones)
        cl = [row[0] for row in db.fetch_all("SELECT owner_name FROM clients;")]
        clients = nokeys(cl)

        pr = [row[0] for row in db.fetch_all("SELECT product_name FROM products;")]
        products = nokeys(pr)

        sv = [row[0] for row in db.fetch_all("SELECT service_name FROM services;")]
        services = nokeys(sv)

        done = ["-", "✔", "✘"]

        departure = ["-", f"{strftime(general[35])}"]

        # Crear una variable de control para el OptionMenu
        global vardate
        global varid
        var = tk.StringVar()
        vardate = tk.StringVar()
        varid = tk.StringVar()
        varid.set(rid)
        var.set(current_value)
        vardate.set(date)
        print("xd", var.get())
        print("xd", vardate.get())
        print("ID: ", varid.get())
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
                option_menu.bind("<Return>", lambda event: on_return(event, option_menu, item_id, col_index, var))  # Verificar antes de guardar
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
                            load_data(1)
                            return

                query = f"""UPDATE records SET {dbcols[col_index]} = 
                (SELECT {dbcols[col_index]} FROM clients WHERE owner_name = '{nuevo_valor}')
                WHERE ID_Records = '{varid.get()}' AND left_date = '-' AND done = '-';"""
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
                            load_data(1)
                            return

                query = f"""UPDATE records SET {dbcols[col_index]} = 
                (SELECT {dbcols[col_index]} FROM products WHERE product_name = '{nuevo_valor}')
                WHERE ID_Records = '{varid.get()}' AND left_date = '-' AND done = '-';"""
                db.commit(query)

            case 2:
                nuevo_valor = var.get()
                print(dbcols[col_index], "xd", nuevo_valor, valor[0])
                check = f"""SELECT r.ID_Clients, r.ID_Products, r.quantity, r.entry_date FROM records r
                JOIN services s ON r.ID_Services = s.ID_Services WHERE s.service_name = '{nuevo_valor}'
                AND r.entry_date = '{vardate.get()}';"""
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
                            load_data(1)
                            return

                query = f"""UPDATE records SET {dbcols[col_index]} = 
                (SELECT {dbcols[col_index]} FROM services WHERE service_name = '{nuevo_valor}')
                WHERE ID_Records = '{varid.get()}' AND left_date = '-' AND done = '-';"""
                db.commit(query)

            case 6:
                nuevo_valor = var.get()  # Obtener el valor seleccionado del OptionMenu
                print(dbcols[col_index])
                query = f"UPDATE records SET {dbcols[col_index]} = '{nuevo_valor}' WHERE ID_Records = '{varid.get()}';"
                db.commit(query)

            case 7:
                nuevo_valor = var.get()  # Obtener el valor seleccionado del OptionMenu
                query = f"UPDATE records SET {dbcols[col_index]} = '{nuevo_valor}' WHERE ID_Records = '{varid.get()}';"
                db.commit(query)

        option_menu.destroy()  # Eliminar OptionMenu después de guardar
        load_data(1)
    
    def on_return(event, option_menu, item_id, col_index, var):
        valor = []
        valor.append(treeview.item(item_id, "values")[col_index])
        if option_menu.get().strip() == "":  # Verifica si el Entry está vacío
            messagebox.showwarning("ADVERTENCIA", "El campo no puede estar vacío.")
            return "break"  # Impide que se ejecute el comando asociado al Return

        query = f"UPDATE records SET {dbcols[col_index]} = {option_menu.get()} WHERE ID_Records = '{varid.get()}' AND left_date = '-' AND done = '-';"
        db.commit(query)
        save_edit(option_menu.get(), item_id, col_index, option_menu, valor, var)

    def load_client(entry1, entry2, entry3, entry4):
        e1 = entry1.get()
        e2 = entry2.get()
        e3 = entry3.get()
        e4 = entry4.get()

        if any("- Seleccione " in e for e in (e1, e2, e3)):
            messagebox.showerror(general[28], general[32])
            return
        try:
            params = (e3, e1, e2, e4)
            db.other_queries(queries[12], params)
            messagebox.showinfo(records[15], records[16])
            load_data(2)
        except Exception as e:
            messagebox.showerror(records[17], str(e))
        
    def load_data(x):
        query_map = {1: queries[0], 2: queries[7]}
        db_data = db.fetch_all(query_map.get(x))

        if x == 1:
            for col_name in cols:
                treeview.heading(col_name, text=col_name, anchor=tk.CENTER)
                treeview.column(col_name, anchor=tk.CENTER)

            treeview.delete(*treeview.get_children())

        for value_tuple in db_data:
            treeview.insert('', tk.END, values=value_tuple)
    
    def delete_row():
        item_id = treeview.focus()  # Obtener el ID del ítem seleccionado
        if item_id == "":
            messagebox.showerror("ERROR", "Ninguna fila se encuentra seleccionada")
            return
        rid = treeview.item(item_id, "values")[8]
        varid = tk.StringVar()
        varid.set(rid)
        query = f"DELETE FROM records WHERE ID_Records = '{varid.get()}'"
        db.commit(query)
        load_data(1)

    frame_container = Frame(window, width=1360, height=500, bg="#333")
    frame_container_visible = False
    frame_container.place_forget()
    
    toggle_frame(frame_container, frame_container_visible)
    rec_frame = ttk.LabelFrame(frame_container, text=records[12])
    rec_frame.grid(row=0, column=0, padx=10, pady=10)
    
    delete_frame = ttk.LabelFrame(frame_container)
    delete_frame.grid(row=0, column=0, padx=25, pady=10, sticky="e")
    
    button_delete = ttk.Button(delete_frame, text="Eliminar", command=lambda: delete_row())
    button_delete.grid(row=0, column=0, padx=10, pady=10)
    
    cl = [row[0] for row in db.fetch_all("SELECT owner_name FROM clients;")]
    cl.insert(0, records[18])
    clients = nokeys(cl)

    pr = [row[0] for row in db.fetch_all("SELECT product_name FROM products;")]
    pr.insert(0, records[19])
    products = nokeys(pr)

    sv = [row[0] for row in db.fetch_all("SELECT service_name FROM services;")]
    sv.insert(0, records[20])
    services = nokeys(sv)

    clientsbox = ttk.Combobox(rec_frame, state=records[13], values=clients)
    clientsbox.current(0)
    clientsbox.grid(row=0, column=0, padx=10, pady=10)

    productsbox = ttk.Combobox(rec_frame, state=records[13], values=products)
    productsbox.current(0)
    productsbox.grid(row=0, column=1, padx=10, pady=10)

    servicesbox = ttk.Combobox(rec_frame, state=records[13], values=services)
    servicesbox.current(0)
    servicesbox.grid(row=0, column=2, padx=10, pady=10)

    vcmd = (window.register(only_numbers_input), "%P")
    quantity_entry = ttk.Entry(rec_frame, foreground="gray", validate="none", validatecommand=vcmd)
    quantity_entry.insert(0, "Ingrese una cantidad")
    quantity_entry.grid(row=0, column=3, padx=10, pady=10)
    
    button_submit = ttk.Button(rec_frame, text=records[22], command=lambda: load_client(clientsbox, productsbox, servicesbox, quantity_entry))
    button_submit.grid(row=0, column=4, padx=10, pady=10)
    
    button_close = ttk.Button(rec_frame, text=general[25], command=lambda: cambiar_imagen_boton(rec, "original", "img_2", toggle_frame(frame_container, True)))
    
    cols = (records[0], records[1], records[2], records[3], records[4], records[5], records[6], records[7])
    
    treeFrame = ttk.Frame(frame_container)
    treeFrame.grid(row=1, column=0, padx=8, pady=18)
    
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side=general[17], fill=general[18])
    
    treeview = ttk.Treeview(treeFrame, show=general[19], yscrollcommand=treeScroll.set, columns=cols, height=18)
    
    for col, width in zip(cols, [200, 200, 200, 90, 160, 180, 180, 90]):
        treeview.column(col, width=width)
        treeview.heading(col, text=col, anchor=records[14])
    
    treeview.pack()
    treeScroll.config(command=treeview.yview)
    
    def on_focus_in(event):
        """Borra el placeholder cuando el usuario hace clic en el Entry."""
        if quantity_entry.get() == "Ingrese una cantidad":
            quantity_entry.config(validate="none")  # Desactivar validación temporalmente
            quantity_entry.delete(0, tk.END)
            quantity_entry.config(foreground="white", validate="key")  # Restaurar validación

    def on_focus_out(event):
        """Si el campo queda vacío, vuelve a poner el placeholder."""
        if not quantity_entry.get():
            quantity_entry.config(validate="none")  # Desactivar validación para insertar texto
            quantity_entry.insert(0, "Ingrese una cantidad")
            quantity_entry.config(foreground="gray", validate="key")  # Restaurar validación

    load_data(1)
    window.bind(general[14], lambda e: button_close.invoke())
    treeview.bind("<Double-1>", on_double_click)
    quantity_entry.bind("<FocusIn>", on_focus_in)
    quantity_entry.bind("<FocusOut>", on_focus_out)

def cli_frame():
    dbcols = (clients[9], clients[2], clients[3], clients[8])
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
        rid = treeview.item(item_id, "values")[0]

        # Crear una variable de control para el OptionMenu
        global varid
        var = tk.StringVar()
        varid = tk.StringVar()
        varid.set(rid)
        var.set(current_value)
        match col_index:
            case 1:
                option_menu = tk.Entry(treeview)
                option_menu.insert(0, treeview.item(item_id, "values")[col_index])  # Insertar valor actual
                option_menu.bind("<Return>", lambda event: on_return(event, option_menu, col_index))  # Verificar antes de guardar
            case 2:
                vcmd = (window.register(only_numbers_input), "%P")
                option_menu = tk.Entry(treeview, validate="key", validatecommand=vcmd)
                option_menu.insert(0, treeview.item(item_id, "values")[col_index])  # Insertar valor actual
                option_menu.bind("<Return>", lambda event: on_return(event, option_menu, col_index))  # Verificar antes de guardar
            case 3:
                option_menu = tk.Entry(treeview)
                option_menu.insert(0, treeview.item(item_id, "values")[col_index])  # Insertar valor actual
                option_menu.bind("<Return>", lambda event: on_return(event, option_menu, col_index))  # Verificar antes de guardar
            case other:
                return

        option_menu.place(x=x + treeview.winfo_x(), y=y + treeview.winfo_y(), width=width, height=height)
        option_menu.focus()

        # Destruir OptionMenu si pierde el foco
        option_menu.bind("<FocusOut>", lambda e: option_menu.destroy())

    def only_numbers_input(P):
        return P.isdigit() or P == ""

    def on_return(event, option_menu, col_index):
        check = f"SELECT {dbcols[col_index]} FROM clients WHERE {dbcols[col_index]} = '{option_menu.get().strip()}';"
        checking = db.fetch_all(check)
        if checking != []:
            print("si", checking)
            messagebox.showwarning(f"{cols[col_index]} duplicado", f"Realizar esta modificación duplicará un {cols[col_index].lower()} ya existente.")
            load_data(1)
            return
        if option_menu.get().strip() == "":  # Verifica si el Entry está vacío
            messagebox.showwarning("ADVERTENCIA", "El campo no puede estar vacío.")
            return "break"  # Impide que se ejecute el comando asociado al Return
        query = f"UPDATE clients SET '{dbcols[col_index]}' = '{option_menu.get()}' WHERE {clients[9]} = '{varid.get()}';"
        db.commit(query)
        option_menu.destroy()  # Eliminar OptionMenu después de guardar
        load_data(1)
    
    def reset_entries(x):
        match x:
            case 1:
                name_entry.delete(0, "")
                name_entry.insert(0, clients[0])
            case 2:
                phone_entry.delete(0, "")
                phone_entry.insert(0, clients[1])
                on_focus_out("<FocusOut>")
            case 3:
                mail_entry.delete(0, "")
                mail_entry.insert(0, clients[7])

    def keep_used():
        if name_entry.get().strip() == "":
            reset_entries(1)
        if phone_entry.get().strip() == "":
            reset_entries(2)
        if mail_entry.get().strip() == "":
            reset_entries(3)
            

    def clear_entry(event, entry, default_text):
        if entry.get() == default_text:
            entry.delete(0, tk.END)
            
    def load_data(x):
        query_map = {1: queries[1], 2: queries[2]}
        db_data = db.fetch_all(query_map.get(x))

        if x == 1:
            for col_name in cols:
                treeview.heading(col_name, text=col_name, anchor=tk.CENTER)
                treeview.column(col_name, anchor=tk.CENTER)

            treeview.delete(*treeview.get_children())

        for value_tuple in db_data:
            treeview.insert('', tk.END, values=value_tuple)

    frame_container = Frame(window, width=1360, height=550, bg="#333")
    frame_container.place(x=0, y=130)
    frame_container.pack_propagate(False)
    frame_container_visible = False
    frame_container.place_forget()
    
    toggle_frame(frame_container, frame_container_visible)
    clients_frame = ttk.LabelFrame(frame_container, text=clients[5])
    clients_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
    
    delete_frame = ttk.LabelFrame(frame_container)
    delete_frame.grid(row=0, column=0, padx=10, pady=10, sticky="s")
    
    button_delete = ttk.Button(delete_frame, text="Eliminar", command=lambda: delete_row())
    button_delete.grid(row=0, column=0, padx=10, pady=10)

    name_entry = ttk.Entry(clients_frame)
    phone_entry = ttk.Entry(clients_frame, validate="none", validatecommand=vcmd)
    mail_entry = ttk.Entry(clients_frame)
    entries = [(name_entry, clients[0]),
            (phone_entry, clients[1]),
            (mail_entry, clients[7])]

    for i, (entry, default_text) in enumerate(entries):
        entry.insert(0, default_text)
        entry.bind(general[21], lambda e, entry=entry, dt=default_text: clear_entry(e, entry, dt))
        entry.grid(row=i, column=0, padx=5, pady=(0, 5), sticky=general[22])
        entry.bind(general[23], lambda e: keep_used())

    def on_focus_in(event):
        """Borra el placeholder cuando el usuario hace clic en el Entry."""
        if phone_entry.get() == clients[1]:
            phone_entry.config(validate="none")  # Desactivar validación temporalmente
            phone_entry.delete(0, tk.END)
            phone_entry.config(validate="key")  # Restaurar validación

    def on_focus_out(event):
        """Si el campo queda vacío, vuelve a poner el placeholder."""
        if not phone_entry.get():
            phone_entry.config(validate="none")  # Desactivar validación para insertar texto
            phone_entry.insert(0, clients[1])
            phone_entry.config(validate="key")  # Restaurar validación
    
    separator = ttk.Separator(clients_frame)
    separator.grid(row=3, column=0, padx=10, pady=10, sticky=general[22])
    
    button = ttk.Button(clients_frame, text=general[24], command=lambda: insert_row())
    button.grid(row=4, column=0, padx=5, pady=(0, 5), sticky=general[26])
    
    button_close = ttk.Button(clients_frame, text=general[25], command=lambda: cambiar_imagen_boton(cli, "original", "img_1", toggle_frame(frame_container, True)))
    button_close.grid(row=5, column=0, padx=5, pady=(0, 5), sticky=general[26])

    cols = (general[20], clients[0], clients[1], clients[7])
    
    treeFrame = ttk.Frame(frame_container)
    treeFrame.grid(row=0, column=1, padx= 101, pady=3)
    
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side=general[17], fill=general[18])
    
    treeview = ttk.Treeview(treeFrame, show=general[19], yscrollcommand=treeScroll.set, columns=cols, height=24)
    
    for col, width in zip(cols, [100, 275, 250, 275]):
        treeview.column(col, width=width)
        treeview.heading(col, text=col, anchor=records[14])
    
    treeview.pack()
    treeScroll.config(command=treeview.yview)
    
    def insert_row():
        name, phone, mail = name_entry.get(), phone_entry.get(), mail_entry.get()

        if name != clients[0]:
            name = name.strip().capitalize()

            client_data = db.fetch_all(queries[3])
            if any(entry[0] == phone for entry in client_data): 
                messagebox.showwarning(general[27], clients[4])
                return
            elif phone == clients[1] or len(phone) != 10 :
                messagebox.showwarning(general[27], "Número invalido. Debe ser de 10 digitos")
                return

            query = f"INSERT INTO clients ('{clients[2]}', '{clients[3]}', '{clients[8]}') VALUES ('{name}', '{phone}', '{mail}');"
            db.commit(query)

            for i in range(1, 4):
                reset_entries(i)
            load_data(2)
        else:
            messagebox.showwarning(general[27], "Nombre invalido.")
            return
    
    def delete_row():
        item_id = treeview.focus()  # Obtener el ID del ítem seleccionado
        if item_id == "":
            messagebox.showerror("ERROR", "Ninguna fila se encuentra seleccionada")
            return
        rid = treeview.item(item_id, "values")[0]
        varid = tk.StringVar()
        varid.set(rid)
        query = f"DELETE FROM clients WHERE {clients[9]} = '{varid.get()}'"
        db.commit(query)
        load_data(1)
    
    window.bind(general[14], lambda e: button_close.invoke())
    treeview.bind("<Double-1>", on_double_click)
    phone_entry.bind("<FocusIn>", on_focus_in)
    phone_entry.bind("<FocusOut>", on_focus_out)
    load_data(1)

def press_clients(event):
    cli.invoke()  # Simula el clic en el botón de clientes

def press_products(event):
    prod.invoke()  # Simula el clic en el botón de productos

def press_records(event):
    rec.invoke()  # Simula el clic en el botón de registros

# Diccionario de eventos y funciones para canvas y ventana
bindings = {
    mainmenu[32]: (canvas, start_move),
    mainmenu[33]: (canvas, do_move),
    mainmenu[34]: (window, press_clients),
    mainmenu[35]: (window, press_products),
    mainmenu[36]: (window, press_records)
}
# Vincula cada evento con su respectiva función en el objeto correspondiente
for key, (obj, function) in bindings.items():
    obj.bind(key, function)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

window.resizable(False, False)
window.mainloop()
