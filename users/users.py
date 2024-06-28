from tkinter import messagebox


TXT_NAME = "userpass.txt"

def getMail(entry):
    with open(TXT_NAME, 'a') as file:
        file.write(f"\ncorreo: {entry}")

def getUser(entry):
    with open(TXT_NAME, 'a') as file:
        file.write(f"\nusuario: {entry}")
        username = entry
        
def getPass(entry):
    with open(TXT_NAME, 'a') as file:
        file.write(f"\ncontra: {entry}")
        passwd = entry

def register(entry1, entry2, entry3, tk):
    getMail(entry1)
    getUser(entry2)
    getPass(entry3)
    messagebox.showinfo("Registro exitoso", "Cuenta registrada con exito.")
    tk.destroy()
    
    

with open(TXT_NAME, 'r') as file:
    # Iterar sobre cada línea del file
    for linea in file:
        if linea.strip() == "linea 2.":
            continue
        # Imprimir cada línea (o realizar alguna operación con ella)
        else:
            print("1", linea.strip())

with open(TXT_NAME, 'r') as file:
    # Leer todas las líneas del file como una lista
    lineas = file.readlines()
    print(lineas)  