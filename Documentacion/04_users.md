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

    Módulo: users
</h1>
</center>

<br></br>

> ###### Archivo: [users.py](/users/users.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;El módulo users es de los que más hacen uso de la base de datos del proyecto. Empezamos justamente importando la librería integrada en python; **sqlite3**. Lo siguiente es crear una conexión con nuestra base de datos y un cursor, el cual nos permite ejecutar querys y almacenar los datos obtenidos en variables (mediante fetchs).
```python
import sqlite3

connect = sqlite3.connect('wipper.db')
cursor = connect.cursor()
```

<br></br>

## _Función **register(entry1, entry2, entry3)**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Crearemos _register_ como nuestra primera función, la cual se mencionó en el [módulo de registro](02_Register.md/#registro-de-usuarios). Esta función realiza algo bastante sencillo: inserta en la tabla user los 3 valores que la función usa como argumento, y un _0_ como cuarto elemento, el cual pertenece al campo _"active"_ que se explicará más adelante. Luego realiza un commit mediante la conexión, para así realizar la inserción de los datos en la base de datos.
```python
def register(entry1, entry2, entry3):
    cursor.execute("""INSERT INTO users ('name', 'passwd', 'mail', 'active')
    VALUES (?, ?, ?, ?)""", (entry1, entry2, entry3, 0))
    connect.commit()
```

<br></br>

## _Función **check(entry1, entry2)**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Como segunda función tenemos check, la cual también se menciono en el [módulo de registro](02_Register.md/#registro-de-usuarios) y, a diferencia de la anterior, esta es un poco más _"compleja"_. La función obtiene todos los mails y nombres de usuario de la base de datos, a los cuales almacena en una lista de tuplas (haciendo uso de fetchall()). Lo siguiente que se hace es crear una tupla con los 2 argumentos que la función usa y, mediante una iteración de bucle for, se recorren todas las tuplas obtenidas de la base de datos para comprobar si alguna coincide con la tupla creada con los argumentos de la función.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;En caso de que ambas tuplas coincidan, se determina que el usuario ingresado ya se encuentra registrado en la base de datos, por lo que el chequeo retornará el booleno True. En caso de iterar en todas las tuplas y que ninguna concida con la otra, el chequeo retornará el booleano False, determinando que el usuario que se quiere registrar no se encuentra registrado en la base de datos.
```python
def check(entry1, entry2):
    user = cursor.execute("SELECT name, mail FROM users")
    users_reg = user.fetchall()
    user_data = (entry1, entry2)
    for entry in users_reg:
        if entry == user_data:
            return True

    else:
        return False
```

<br></br>

## _Función **login(entry1, entry2)**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;De esta función se ha visto su uso en el [módulo de login](01_Login.md/#gestión-de-usuarios), en la segunda función para gestión de usuarios. Su funcionamiento es similar al de la función anterior: obtiene todas las contraseñas y nombres de usuario almacenados en la base de datos, las guarda en una lista de tuplas, crea otra tupla aparte usando los 2 argumentos de la función, y mediante una iteración comprueba si alguna de las tuplas de la lista coincide con la tupla de argumentos.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;En caso de que sí, se actualiza el valor del campo active de ese usuario a 1, se hace un commit del cambio y se retorna el booleano True. En caso de que ninguna tupla de la lista coincida, se retorna el booleano False.

<br></br>

## _Función **current_user()**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Esta función obtiene el nombre de usuario del usuario que tenga como valor 1 en el campo _"active"_ y lo retorna. El "[0]" en el retorno del nombre de usuario tiene como función el eliminar los elementos de tupla con los que cuenta el dato, es decir, en vez de recibir _"('Luca',)"_, recibiríamos solamente _"Luca"_.
```python
def current_user():
    cursor.execute("SELECT name FROM users WHERE active = 1")
    username = cursor.fetchone()
    return username[0]
```

<br></br>

## _Función **logout(name)**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Por último, la función logout nos permite pasar ese valor 1 de active a 0 en caso de que el usuario cierre la sesión de su cuenta.
```python
def logout(name):
    cursor.execute(f"UPDATE users SET active = 0 WHERE name = '{name}'")
    connect.commit()
```

<br></br>

## _Campo **active**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;El campo _active_ se encuentra en la tabla users y tiene como fin el determinar qué usuario se encuentra actualmente utilizando el software. Esto se hace ya que en la pantalla de Menu, en la esquina inferior izquierda, podemos ver el nombre de usuario del usuario que este trabajando en alguno de los menús. Cambiará su valor entre 0 y 1 dependiendo de si el usuario cuenta o no con una sesión activa en el software, siendo 0 una sesión cerrada, y 1 una sesión activa.

<br></br>

<br></br>

###### [Anterior](03_getpath.md) | [Siguiente](05_Menu.md)