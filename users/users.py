from tkinter import Tk, messagebox


TXT_NAME = "userpass.txt"

def getMail(entry):
    with open(TXT_NAME, 'a') as file:
        file.write("\nentry")

def getUser(entry):
    with open(TXT_NAME, 'a') as file:
        file.write("\nentry")
        username = entry
        
def getPass(entry):
    with open(TXT_NAME, 'a') as file:
        file.write("\nentry")
        passwd = entry

def register(entry1, entry2, entry3):
    getMail(entry1)
    getUser(entry2)
    getPass(entry3)
    messagebox.showinfo("Registro exitoso", "Cuenta registrada con exito.")
    Tk().destroy()
