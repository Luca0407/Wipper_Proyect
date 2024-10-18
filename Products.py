# --- Librerías y Módulos ---
import tkinter as tk
from tkinter import ttk, messagebox
from getpath import getpath as gp
import sqlite3
from strings import strings as txt
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 



# --- x ---
connect = sqlite3.connect(txt.general()[13])
cursor = connect.cursor()
init_path = gp.getPath()
cols = (txt.general()[20], txt.products()[0], txt.products()[1], txt.products()[2])


def close():
    root.destroy()
    connect.close()


def load_data(x):
    query_map = {1: txt.queries()[4], 2: txt.queries()[5]}
    cursor.execute(query_map.get(x))
    db_data = cursor.fetchall()

    if x == 1:
        for col_marca in cols:
            treeview.heading(col_marca, text=col_marca, anchor=tk.CENTER)
            treeview.column(col_marca, anchor=tk.CENTER)

    for value_tuple in db_data:
        treeview.insert('', tk.END, values=value_tuple)


def insert_row():
    columns, values = [], []
    brand, model, cost = brand_entry.get(), model_entry.get(), cost_entry.get()

    if brand not in cols:
        columns.append(txt.products()[3])
        values.append(brand.strip().capitalize())

    if model not in cols:
        columns.append(txt.products()[4])
        values.append(model.upper().strip())

    try:
        if cost not in cols:
            columns.append(txt.products()[5])
            values.append(float(cost))
    except ValueError:
        messagebox.showerror(txt.general()[28], txt.products()[8])
        return

    product_name = f"{brand} {model}"
    cursor.execute(txt.queries()[6])
    product_data = cursor.fetchall()
    if any(entry[0] == product_name for entry in product_data):
        messagebox.showwarning(txt.general()[27], txt.products()[7])
        return

    query = f"INSERT INTO products ({', '.join(columns)}) VALUES ({', '.join(['?'] * len(values))})"
    cursor.execute(query, values)
    connect.commit()
    for i in range(1, 4):
        reset_entries(i)
    load_data(2)


def reset_entries(x):
    match x:
        case 1:
            brand_entry.delete(0, "")
            brand_entry.insert(0, txt.products()[0])
            
        case 2:
            model_entry.delete(0, "")
            model_entry.insert(0, txt.products()[1])
        
        case 3:
            cost_entry.delete(0, "")
            cost_entry.insert(0, txt.products()[2])


def keep_used():
    if brand_entry.get().strip() == "":
        reset_entries(1)
    if model_entry.get().strip() == "":
        reset_entries(2)
    if cost_entry.get().strip() == "":
        reset_entries(3)


def clear_entry(event, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, tk.END)


def center_window(window, width, height):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2) + 37
    window.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.overrideredirect(True)
center_window(root, 1360, 550)

style = ttk.Style(root)
theme_path = rf"{init_path}\forest-dark.tcl"
root.tk.call(txt.general()[15], theme_path)
style.theme_use(txt.general()[16])

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text=txt.products()[6])
widgets_frame.grid(row=0, column=0, padx=20, pady=10)

entries = [
    (brand_entry := ttk.Entry(widgets_frame), txt.products()[0]),
    (model_entry := ttk.Entry(widgets_frame), txt.products()[1]),
    (cost_entry := ttk.Entry(widgets_frame), txt.products()[2])
]

for i, (entry, default_text) in enumerate(entries):
    entry.insert(0, default_text)
    entry.bind(txt.general()[21], lambda e, entry=entry, dt=default_text: clear_entry(e, entry, dt))
    entry.grid(row=i, column=0, padx=5, pady=(0, 5), sticky=txt.general()[22])
    entry.bind(txt.general()[23], lambda e: keep_used())

separator = ttk.Separator(widgets_frame)
separator.grid(row=3, column=0, padx=10, pady=10, sticky=txt.general()[22])

button = ttk.Button(widgets_frame, text=txt.general()[24], command=insert_row)
button.grid(row=4, column=0, padx=5, pady=(0, 5), sticky=txt.general()[26])

button_close = ttk.Button(widgets_frame, text=txt.general()[25], command=close)
button_close.grid(row=5, column=0, padx=5, pady=(0, 5), sticky=txt.general()[26])

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)

treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side=txt.general()[17], fill=txt.general()[18])

treeview = ttk.Treeview(treeFrame, show=txt.general()[19], yscrollcommand=treeScroll.set, columns=cols, height=23)
for col, width in zip(cols, [50, 292, 296, 292]):
    treeview.column(col, width=width)

treeview.pack()
treeScroll.config(command=treeview.yview)

root.bind(txt.general()[5], lambda e: button.invoke())
root.bind(txt.general()[14], lambda e: button_close.invoke())

load_data(1)
root.mainloop()
