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

    Módulo: getpath
</h1>
</center>

<br></br>

> ###### Archivo: [getpath.py](/Wipper_Proyect/getpath/getpath.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Este módulo es importante para obtener la dirección en donde se encuentran almacenados los diferentes archivos de los que el software hace uso. Como siempre, lo primero son las librerías que se importan, siendo 3 en este caso:
1. _inspect_
2. _la clase **Path** de pathlib_
3. _subprocess_
<br></br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A continuación, lo que haremos será crear 3 variables y 1 constante, de las cuales 2 variables utilizan **inspect**, y la tercera hace uso de **Path**, y la constante obtiene la dirección de la carpeta inicial del proyecto:
```python
current_frame = inspect.currentframe()
caller_frame = inspect.getouterframes(current_frame, 2)
script_name = Path(caller_frame[-1].filename).stem
OUTPUT_PATH = Path(__file__).parent.parent
```
<br></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**current_frame** devuelve el marco de pila en el que se está ejecutando getpath.py, es decir, nos devuelve la dirección en memoria donde se encuentra el archivo en ejecución, la dirección en disco de este y la linea en donde se este haciendo uso de la variable.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**caller_frame** devuelve una lista con (en este caso) los 2 primeros marcos de pila del archivo. Nos devuelve casi los mismos datos que en el caso de current_frame, pero con una determinada cantidad pilas externas y con toda la información dentro de una lista.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**script_name** devuelve el nombre (.filename) del último elemento de _caller_frame_ (es decir, el archivo actualmente en ejecucíon) sin su extensión (debido al uso de .stem) y la convierte en un objeto Path.

<br></br>

## _Función **getPath()**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Esta función obtiene la dirección en donde se encuentran todos los recursos (imágenes) que cada módulo utiliza individualmente. Realiza un **match ...  case** con _script_name_, lo que permite obtener una determinada dirección según sea el módulo que se esté ejecutando en el momento. Por ultimo, la función retorna la dirección como un objeto **Path** (el cual se usa en la ya antes vista función [_relative_to_assets()_](01_Login.md/#acceso-a-directorios)).
```python
def getPath():
    match script_name:
        case "Login":
            assets_path = OUTPUT_PATH / 'Login_Screen' / 'build' / 'assets' / 'frame0'

        case "Register":
            assets_path = OUTPUT_PATH / 'Register_Screen' / 'build' / 'assets' / 'frame0'

        case "Menu":
            assets_path = OUTPUT_PATH / 'Menu_Screen' / 'build' / 'assets' / 'frame0'

        case "Clients":
            assets_path = OUTPUT_PATH
        
        case "Products":
            assets_path = OUTPUT_PATH

        case "Commerce":
            assets_path = OUTPUT_PATH / 'Commerce_Screen' / 'build' / 'assets' / 'frame0'

    return assets_path
```
<br></br>

## _Funcion **vxl(screen)**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Esta función recibe como argumento un string el cual determina qué módulo debe ejecutarse. Toma una lista con los nombres de cada módulo y, si el argumento dado coincide con algún nombre, obtiene su dirección y lo abre usando **subprocess.Popen**.
<br></br>

<br></br>

###### [Anterior](02_Login.md) | [Siguiente](04_users.md)