<head>
    <style>
        body {
            text-align: justify;
        }
    </style>
</head>

<br></br>

<center>
    <h1>

    Menú Principal
</h1>
</center>

<br></br>

> ###### Archivo: [Menu.py](/Menu.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;El menú principal es una de las pantallas más importantes del proyecto; es donde prácticamente la mitad de las tareas que el software puede realizar se hacen. Como siempre,empezamos importando las librerías y módulos necesarios para su correcto funcionamiento:
* **pathlib** (módulo Path)
* **tkinter** (módulos Tk, Canvas, Button, PhotoImage)
* **getpath** (módulo propio)
* **users** (módulo propio)
* **time** (módulo strftime)
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Como siempre, creamos una variable window que tenga de valor Tk(), y creamos una constante PATH que recibe como valor [gp.getPath()](03_getpath.md/#función-getpath). Lo nuevo que incluye esta pantalla es que crearemos una variable username, la cual usará la función [current_user()](04_users.md/#función-current_user) del módulo users. Por ultimo, creamos la funcion [relative_to_assets()](01_Login.md/#acceso-a-directorios), ya mencionada varias veces anteriormente.

<br></br>

## _Movimiento de la ventana_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Son 2 las funciones que componen el movimiento de la ventana, ya que una comprueba que el movimiento sea posible (a la vez que le asigna un margen superior de 30px para agarrar la ventana), y la otra mueve la ventana cuando el cursor se mantiene con el click presionado.
```python
def start_move(event):
    if event.y <= 30:
        window.x = event.x
        window.y = event.y
    else:
        window.x = None
        window.y = None

def do_move(event):
    if window.x is not None and window.y is not None:
        deltax = event.x - window.x
        deltay = event.y - window.y
        x = window.winfo_x() + deltax
        y = window.winfo_y() + deltay
        window.geometry(f"+{x}+{y}")
```
<br></br>

## _Fecha y Hora_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;La ventana de menú contiene una barra de estado, la cual muestra, ademas del nombre del usuario activo, la fecha y la hora que el dispositivo tiene configurada. 

<br></br>

<br></br>

###### [Anterior](04_users.md) | [Siguiente](06_Clients.md)
