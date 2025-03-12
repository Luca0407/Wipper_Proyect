# --- Librerías y Módulos ---
import tkinter as tk
from tkinter import ttk, messagebox
from getpath import getpath as gp
from strings import strings as txt
from db_manager import db_manager as db
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

general = txt.general()
clients = txt.clients()
queries = txt.queries()

# --- x ---
init_path = gp.getPath()
cols = (general[20], clients[0], clients[1])
dbcols = ("ID_Clients", "owner_name", "phone")


def close():
    window.destroy()

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
    print("xd", var.get())
    print("ID: ", varid.get())
    match col_index:
        case 1:
            option_menu = tk.Entry(treeview)
            option_menu.insert(0, treeview.item(item_id, "values")[col_index])  # Insertar valor actual
            option_menu.bind("<Return>", lambda event: on_return(event, option_menu, item_id, col_index, var))  # Verificar antes de guardar
        case 2:
            vcmd = (window.register(only_numbers_input), "%P")
            option_menu = tk.Entry(treeview, validate="key", validatecommand=vcmd)
            option_menu.insert(0, treeview.item(item_id, "values")[col_index])  # Insertar valor actual
            option_menu.bind("<Return>", lambda event: on_return(event, option_menu, item_id, col_index, var))  # Verificar antes de guardar
        case other:
            return

    option_menu.place(x=x + treeview.winfo_x(), y=y + treeview.winfo_y(), width=width, height=height)
    option_menu.focus()

    # Destruir OptionMenu si pierde el foco
    option_menu.bind("<FocusOut>", lambda e: option_menu.destroy())

def save_edit(value, item_id, col_index, option_menu, valor, var):
    """Guarda el valor seleccionado en la celda"""
    values = list(treeview.item(item_id, "values"))
    values[col_index] = value
    treeview.item(item_id, values=values)
    nuevo_valor = var.get()
    print(dbcols[col_index], nuevo_valor, valor[0])
    check = f"SELECT owner_name, phone FROM clients WHERE owner_name = '{nuevo_valor}';"
    checking = db.fetch_all(check)
    if checking != []:
        print("si", checking)
        messagebox.showwarning("Cliente duplicado", "Realizar esta modificación duplicará un cliente ya existente.")
        load_data(1)
        return

    option_menu.destroy()  # Eliminar OptionMenu después de guardar
    load_data(1)

def only_numbers_input(P):
    return P.isdigit() or P == ""

def on_return(event, option_menu, item_id, col_index, var):
    valor = []
    valor.append(treeview.item(item_id, "values")[col_index])
    if option_menu.get().strip() == "":  # Verifica si el Entry está vacío
        messagebox.showwarning("ADVERTENCIA", "El campo no puede estar vacío.")
        return "break"  # Impide que se ejecute el comando asociado al Return
    
    print("onreturn: ", dbcols[col_index], option_menu.get(), varid.get())
    query = f"UPDATE clients SET '{dbcols[col_index]}' = '{option_menu.get()}' WHERE ID_Clients = '{varid.get()}';"
    db.commit(query)
    save_edit(dbcols[col_index], item_id, col_index, option_menu, valor, var)

def delete_row():
    item_id = treeview.focus()  # Obtener el ID del ítem seleccionado
    if item_id == "":
        messagebox.showerror("ERROR", "Ninguna fila se encuentra seleccionada")
        return
    rid = treeview.item(item_id, "values")[0]
    varid = tk.StringVar()
    varid.set(rid)
    query = f"DELETE FROM clients WHERE ID_Clients = '{varid.get()}'"
    db.commit(query)
    load_data(1)

def insert_row():
    name, phone = name_entry.get(), phone_entry.get()

    if name != clients[0]:
        name = name.strip().capitalize()

        client_data = db.fetch_all(queries[3])
        if any(entry[0] == phone for entry in client_data): 
            messagebox.showwarning(general[27], clients[4])
            return
        elif phone == clients[1] or len(phone) != 10 :
            messagebox.showwarning(general[27], "Número invalido.")
            return

        query = f"INSERT INTO clients (owner_name, phone) VALUES ('{name}', '{phone}');"
        db.commit(query)

        for i in range(1, 3):
            reset_entries(i)
        load_data(2)
    else:
        messagebox.showwarning(general[27], "Nombre invalido.")
        return


def reset_entries(x):
    match x:
        case 1:
            name_entry.delete(0, "")
            name_entry.insert(0, clients[0])
        case 2:
            phone_entry.delete(0, "")
            phone_entry.insert(0, clients[1])


def keep_used():
    if name_entry.get().strip() == "":
        reset_entries(1)
    if phone_entry.get().strip() == "":
        reset_entries(2)


def clear_entry(event, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, tk.END)


def center_window(window, width=1360, height=550):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2) + 37
    window.geometry(f"{width}x{height}+{x}+{y}")

window = tk.Tk()
window.attributes("-topmost", True)
window.overrideredirect(True)
center_window(window, 1360, 550)

style = ttk.Style(window)
theme_path = rf"{init_path}\forest-dark.tcl"
window.tk.call(general[15], theme_path)
style.theme_use(general[16])

frame = ttk.Frame(window)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text=clients[5])
widgets_frame.grid(row=0, column=0, padx=20, pady=10)

delete_frame = ttk.LabelFrame(frame)
delete_frame.grid(row=0, column=0, padx=10, pady=10, sticky="s")

vcmd = (window.register(only_numbers_input), "%P")

entries = [
    (name_entry := ttk.Entry(widgets_frame), clients[0]),
    (phone_entry := ttk.Entry(widgets_frame, validate="none", validatecommand=vcmd), clients[1]),
]

for i, (entry, default_text) in enumerate(entries):
    entry.insert(0, default_text)
    entry.bind(general[21], lambda e, entry=entry, dt=default_text: clear_entry(e, entry, dt))
    entry.grid(row=i, column=0, padx=5, pady=(0, 5), sticky=general[22])
    entry.bind(general[23], lambda e: keep_used())

separator = ttk.Separator(widgets_frame)
separator.grid(row=4, column=0, padx=10, pady=10, sticky=general[22])

button = ttk.Button(widgets_frame, text=general[24], command=lambda: insert_row())
button.grid(row=9, column=0, padx=5, pady=(0, 5), sticky=general[26])

button_close = ttk.Button(widgets_frame, text=general[25], command=close)
button_close.grid(row=10, column=0, padx=5, pady=(0, 5), sticky=general[26])

button_delete = ttk.Button(delete_frame, text="Eliminar", command=lambda: delete_row())
button_delete.grid(row=0, column=0, padx=10, pady=10)

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

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)

treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side=general[17], fill=general[18])

treeview = ttk.Treeview(treeFrame, show=general[19], yscrollcommand=treeScroll.set, columns=cols, height=23)
for col, width in zip(cols, [300, 300, 300]):
    treeview.column(col, width=width)

treeview.pack()
treeScroll.config(command=treeview.yview)

window.bind(general[14], lambda e: button_close.invoke())
treeview.bind("<Double-1>", on_double_click)
phone_entry.bind("<FocusIn>", on_focus_in)
phone_entry.bind("<FocusOut>", on_focus_out)

load_data(1)
window.mainloop()
