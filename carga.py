# Nombre del archivo
nombre_archivo = "mi_archivo.txt"

# Contenido del archivo
contenido = "Este es el contenido de mi archivo."

with open(nombre_archivo, 'r') as archivo:
    # Iterar sobre cada línea del archivo
    for linea in archivo:
        if linea.strip() == "linea 2.":
            continue
        # Imprimir cada línea (o realizar alguna operación con ella)
        else:
            print(linea.strip())
