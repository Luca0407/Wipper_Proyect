import tkinter as tk
from tkinter import ttk







def on_double_click(event):
    """ Función que permite editar una celda al hacer doble clic """
    # Obtener el índice del item seleccionado
    item_id = tree.focus()
    
    # Obtener coordenadas del clic
    col = tree.identify_column(event.x)  # Columna en formato #n
    col_index = int(col[1:]) - 1  # Convertir a índice de lista (0 basado)

    if item_id and col_index >= 0:
        x, y, width, height = tree.bbox(item_id, col_index)
        
        # Crear Entry y posicionarlo en la celda seleccionada
        entry = tk.Entry(root)
        entry.place(x=x+tree.winfo_x(), y=y+tree.winfo_y(), width=width, height=height)
        
        # Insertar texto actual en el Entry
        entry.insert(0, tree.item(item_id, "values")[col_index])
        entry.focus()

        def save_edit(event):
            """ Guarda el texto ingresado en la celda """
            new_text = entry.get()
            values = list(tree.item(item_id, "values"))
            values[col_index] = new_text
            tree.item(item_id, values=values)
            entry.destroy()  # Elimina el Entry después de guardar

        # Guardar cambios al presionar "Enter"
        entry.bind("<Return>", save_edit)
        entry.bind("<FocusOut>", lambda e: entry.destroy())  # Cierra si pierde foco









# Crear ventana principal
root = tk.Tk()
root.title("Treeview Editable con Forest Theme")
root.geometry("500x300")

# Aplicar el tema Forest-ttk-theme (asegúrate de que esté instalado)
style = ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")  # Cambia la ruta si es necesario
style.theme_use("forest-dark")

# Crear Treeview
columns = ("Nombre", "Edad", "Ciudad")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

# Insertar datos de ejemplo
tree.insert("", "end", values=("Juan", "25", "Madrid"))
tree.insert("", "end", values=("Ana", "30", "Barcelona"))

tree.pack(expand=True, fill="both")

# Evento de doble clic
tree.bind("<Double-1>", on_double_click)

root.mainloop()
