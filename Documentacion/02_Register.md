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

    Pantalla de registro
</h1>
</center>

<br></br>

> ###### Archivo: [Register.py](/Register.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yendo directo al grano, el archivo importa exactamente los mismos módulos y librerías vistas en el [archivo anterior](Login.md/#archivo-loginpy). También usa el mismo método de [acceso a directorios](Login.md/#acceso-a-directorios) de Login.py para obtener los recursos y accesos necesarios.

<br></br>

## _Registro de usuarios_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Crea la función _user_signup()_ la cual llama a la función _check_ del módulo **users** para comprobar si los datos ingresados en los campos _user_input_ y _mail_input_ ya se encuentran registrados; devolviendo un valor booleano según el caso. En caso de ser **True**, se mostrará una ventana de error, mencionando que los datos escritos ya se encuentran registrados en otro usuario. Caso contrario, se llama a la función _register_ (también de **users**) y se cargan los datos escritos en _user_input_, _password_input_ y _mail_input_. Se muestra un mensaje mencionando que el usuario se registró exitosamente y se cierra la ventana a la vez que se vuelve a la pantalla de inicio de sesión.
```python
def user_signup():
    if users.check(user_input.get(), mail_input.get()) is False:
        users.register(user_input.get(), password_input.get(), mail_input.get())
        messagebox.showinfo("Registro exitoso", "Cuenta registrada con exito.")
        window.destroy()
        gp.vxl("Login")
    else:
        messagebox.showerror("ERROR","Este usuario ya se encuentra registrado.")
```

<br></br>

## _Configuración de ventana_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;La configuración de la ventana de registro es exactamente la misma a la vista en la [ventana de login](Login.md/#configuración-de-ventana), por lo que pasaremos al siguiente punto.
<br></br>

## _Entradas de texto_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Las entradas de texto de esta ventana también son exactamente las mismas que las de la [ventana anterior](Login.md/#entradas-de-texto), con la diferencia de que ahora hay una 3ra entrada para ingresar un mail.
<br></br>

## _Botones_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;En cuanto a los botones, esta pantalla solo cuenta con 2: uno para cerrar la ventana y otro para registrar el usuario. Siguen exactamente la misma estructura que los [botones vistos anteriormente](Login.md/#botones), por lo que solo se va a mencionar el comando de cada uno:
* El _boton exit_ usa window.destroy() para terminar la ejecución de la ventana.
* El _boton sign_up_ llama a la función [user_signup()](Register.md/#registro-de-usuarios) vista anteriormente y ejecuta sus comandos.
<br></br>

## _Textos_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Siguen la misma estructura que los [anteriormente vistos](Login.md/#textos), con la diferencia de que son 3 en este caso: uno para cada entrada de texto.
<br></br>

## _Adicional_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Adicionalmente, cuenta con el mismo comando de la tecla **enter** usada en la [pantalla anterior](Login.md/#adicional), asi como _window.resizable(_) y _window.mainloop()_

<br></br>

<br></br>

###### [Anterior](01_Login.md) | [Siguiente](03_getpath.md)