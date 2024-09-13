<head>
    <style>
        body {
            text-align: justify;
        }
    </style>
</head>

<body>
<center>
    <h1>
    <br></br>

    Documentación Wipper Proyect 2024
</h1>
</center>

<br></br>

## **_Equipo de desarrollo_**

<br></br>

#### **Diseñador:** Segovia, Alejandro Agustín 🗿 | Lucca, Estela Belén 🤓

<br></br>

#### **Programadores:** Elizondo, Luca Maximiliano 🤑 | Galarza, Gonzalo Agustín 💀

<br></br>

#### **Cliente:** Elizondo, Hector René 🐸 (Wipper Insumos)

<br></br>

#### **Profesor de Practicas Profesionalizantes II:** Paszco, Gustavo Ariel

<br></br>

<br></br>

<br></br>

<center>
    <h1>
        Pantalla de inicio de sesión (Login.py)
    </h1>
</center>

<br></br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para su funcionamiento se utilizan las siguientes librerías y los siguientes módulos:
* pathlib (módulo Path)
* tkinter (módulos Tk, Canvas, Entry, Button, PhotoImage, messagebox)
* getpath (módulo propio)
* users (módulo propio)
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Respecto a los módulos propios, sus funcionamientos se verán más adelante en el documento. La primera acción inicializar la variable _**window**_, a la cual se le asigna el valor _Tk()_ (esto es algo que se repetirá para los demás modulos del software).

<br></br>

## _Acceso a directorios_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lo siguiente a realizar es obtener la ubicación de las imágenes necesarias para la pantalla de inicio de sesión.

```python
init_path = gp.getPath()
ASSETS_PATH = init_path / 'Login_Screen' / 'build' / 'assets' / 'frame0'
```
<br></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;La variable _init_path_ obtiene la ubicación en la cual se ecuentra alojado el archivo _**login.py**_. Luego, desde dicha ruta, la constante _ASSETS_PATH_ accede hasta la carpeta _'frame0'_ con el fin de obtener las 6 imágenes que componen la pantalla:
1. _exit.png_
2. _forgot_pass.png_
3. _input.png_
4. _login.png_
5. _logo.png_
6. _sign_up.png_
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Por ultimo (respecto al acceso a directorios), definimos la función _relative_to_assets()_, la cual busca un archivo específico y nos brinda su dirección exacta.

```python
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
```
<br></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;La función toma un argumento _path_ de tipo string e indica (mediante **-> Path**) que espera como retorno un valor del tipo Path. El valor que retorna es un archivo dentro de _ASSETS_PATH_ y lo transforma al tipo _Path_.

<br></br>

## _Gestión de usuarios_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;En esta parte tenemos 2 funciones: **new_user()** y **check_login()**. La primera cierra la pantalla de login y nos redirecciona a la pantalla de registro.

```python
def new_user():
    window.destroy()
    gp.register_screen()
```
<br></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;La segunda función usa la función _login_ del módulo **users** y comprueba si los datos ingresados (usuario y contraseña) se encuentran registrados en la base de datos (determinado por el booleano que el modulo retorna). En caso de estar registrado, muestra mediante _messagebox.showinfo_ el mensaje de bienvenida. Caso contrario, usa _messagebox.showerror_ y muestra un mensaje de error.
```python
def check_login():
    if users.login(user_input.get(), pass_input.get()) is True:
        messagebox.showinfo("Ingreso exitoso", "Bienvenido al gestor de Wipper.")
        window.destroy()
        gp.wipper_menu()
    else:
        messagebox.showerror("Ingreso incorrecto", "Usuario o contraseña incorrectos.")
```
<br></br>

## _Configuración de ventana_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;La ventana tiene una resolución de 300x480 y se utiliza **window.overrideredirect(True)** para eliminar los decorados y la barra superior que normalmente _tkinter_ incluye. Lo siguiente que se realiza es la medida en pixeles de la pantalla que este ejecutando el código, para así centrar la ventana en la pantalla usando **window.geometry**.

```python
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
```
<br></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lo siguiente que se realiza es crear un objeto Canvas, que es el area de interfaz gráfica donde se va a mostrar nuestra ventana. Dicho Canvas se posiciona en la dirección por defecto (_x=0, y=0_) y utiliza ciertos parametros para su correcta construcción:
* _**window:**_ es la ventana donde se colocará el Canvas.
* _**bg:**_ define mediante código hexadecimal el color del fondo (_background_).
* _**height:**_ establece la altura del Canvas en píxeles.
* _**width:**_ establece el ancho del Canvas en píxeles.
* _**bd:**_ controla el grosor del borde del Canvas (_border width_).
* _**highlightthickness:**_ resalta los widgets cuando estos son enfocados.

```python
canvas = Canvas(
    window,
    bg = "#191919",
    height = 480,
    width = 300,
    bd = 0,
    highlightthickness = 0)

canvas.place(x = 0, y = 0)
```
<br></br>

## _Entradas de texto_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;La estructura para la creación de ambas entradas de texto es practicamente la mísma, con contadas variaciones entre sí. Se crea un objeto **PhotoImage** el cual pide un archivo como argumento y llama a la función '_relative_to_assets()_' para obtener una imagen en específico. Luego se crea una imagen con el objeto **Canvas** en la cual se fija una posición especifica dentro de la ventana y se carga la imagen anteriormente creada. Lo tercero que se hace es crear un objeto con el módulo **Entry**, el cúal toma ciertos parámetros:
* _**bd**_
* _**bg**_
* _**fg:**_ define el color del texto que se escribirá dentro del widget (foreground).
* _**highlightthickness**_
* _**font:**_ define la tipografía que se usará para el texto dentro del widget.
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Por último, se utiliza el método _place()_, el cual posiciona la imagen y le asigna medidas específicas.
```python
userpass_image = PhotoImage(
    file=relative_to_assets("input.png"))

canvas.create_image(
    150.0,
    204.0,
    image=userpass_image)

user_input = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular", 12))

user_input.place(
    x=46.0,
    y=184.0,
    width=208.0,
    height=38.0)
```

<br></br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;En cuanto a la entrada para la contraseña, el código es muy similar. Se crea una imagen usando el mismo **PhotoImage** que la entrada del usuario. Se crea un objeto **Entry** con los mismos parámetros, pero con uno adicional: _show_, el cual mostrara un solo determinado caracter por cáda caracter que se escriba en la entrada. Por último, se posiciona y asignan las mismas medidas con _place()_.
```python
pass_input = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat Regular",11),
    show="●")
```
<br></br>

## _Logo en pantalla_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Similar a las entradas de texto vistas anteriormente, el logo requiere de crear un objeto con PhotoImage y luego crear la instancia de la imágen con Canvas.
```python
logo_image = PhotoImage(
    file=relative_to_assets("logo.png"))

logo = canvas.create_image(
    150.0,
    82.0,
    image=logo_image)
```
<br></br>

## _Botones_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;La creación de botones es muy similar a lo anterior visto, por lo que para evitar más redundancias en este documento, a continuación se muestra la estructura básica de cada botón, independientemente de cualquier argumento que estos pudieran tener:
* Se crea un objeto con el módulo PhotoImage.
* Se crea un objeto con el módulo Button.
* Se posicióna y asignan medidas con place().
</body>