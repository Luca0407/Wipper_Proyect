import tkinter as tk
from tkinter import ttk

def on_double_click(event):
    """Permite editar una celda con un OptionMenu al hacer doble clic"""
    item_id = treeview.focus()  # Obtener el ID del ítem seleccionado
    col = treeview.identify_column(event.x)  # Columna en formato #n
    col_index = int(col[1:]) - 1  # Convertir a índice (0 basado)

    if not item_id or col_index < 0:
        return  # Evita errores si no hay selección válida

    bbox = treeview.bbox(item_id, col_index)
    if not bbox:
        return  # Evita errores si bbox es None

    x, y, width, height = bbox

    # Obtener el valor actual de la celda
    current_value = treeview.item(item_id, "values")[col_index]
    
    # Opciones del OptionMenu (puedes personalizar estas opciones)
    options = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]
    
    # Crear una variable de control para el OptionMenu
    var = tk.StringVar()
    var.set(current_value)
    
    # Crear OptionMenu y posicionarlo sobre la celda seleccionada
    option_menu = tk.OptionMenu(treeview, var, *options, command=lambda value: save_edit(value, item_id, col_index, option_menu))
    option_menu.place(x=x + treeview.winfo_x(), y=y + treeview.winfo_y(), width=width, height=height)
    option_menu.focus()
    
    # Destruir OptionMenu si pierde el foco
    option_menu.bind("<FocusOut>", lambda e: option_menu.destroy())

def save_edit(value, item_id, col_index, option_menu):
    """Guarda el valor seleccionado en la celda"""
    values = list(treeview.item(item_id, "values"))
    values[col_index] = value
    treeview.item(item_id, values=values)
    option_menu.destroy()  # Eliminar OptionMenu después de guardar

# Ejemplo de interfaz con Treeview
root = tk.Tk()
treeview = ttk.Treeview(root, columns=("A", "B", "C"), show="headings")
for col in ("A", "B", "C"):
    treeview.heading(col, text=col)
    treeview.column(col, width=100)

treeview.insert("", "end", values=("Opción 1", "Opción 2", "Opción 3"))
treeview.pack()

treeview.bind("<Double-1>", on_double_click)

root.mainloop()
