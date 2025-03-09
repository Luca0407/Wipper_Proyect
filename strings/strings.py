def general():
    general_strings = ["#191919", "input.png", "#D9D9D9", "#000716", "Montserrat Regular",
                        '<Return>', "●", "exit.png", "sign_up.png", "nw",
                        "Usuario", "#FFFFFF",  "Contraseña", 'wipper.db', '<Escape>',
                        'source',  "forest-dark",  "right", "y",  "headings",
                        "ID", "<FocusIn>", "ew", "<FocusOut>", "Agregar",
                        "Cerrar", "nsew", "Advertencia", "ERROR", "Menu",
                        "Login", "flat", "Uno o más campos se encuentran vacíos.", "Contraseña o correo invalido.", "ridge",
                        '%d/%m/%Y', "split.png", "show.png", "hide.png"]
    return general_strings


def queries():
    every_query = ["""SELECT clients.owner_name, product_name, services.service_name,
                r.quantity, sum(products.initial_cost * quantity + services.aditional_cost), r.entry_date, r.left_date,
                r.done, r.ID_Records FROM records r JOIN clients ON
                    r.ID_Clients = clients.ID_Clients
                JOIN products ON
                    r.ID_Products = products.ID_Products
                JOIN services ON
                    r.ID_Services = services.ID_Services
                GROUP BY r.ID_Records
                ORDER BY r.ID_Records;""",  # 0 listado en records.
                
                "SELECT * FROM clients;",  # 1 listado en clients.
                
                "SELECT * FROM clients ORDER BY ID_Clients DESC LIMIT 1;",  # 2 actualización de listado en clients.
                
                "SELECT phone FROM clients;",  # 3 verificación en clients.
                
                "SELECT ID_Products, product_name, initial_cost FROM products;",  # 4 listado en products.
                
                """SELECT ID_Products, product_name, initial_cost
                    FROM products ORDER BY ID_Products DESC LIMIT 1;""",  # 5 actualización de listado en products.
                
                "SELECT concat(brand, ' ', model) FROM products;",  # 6 verificación en products.
                
                """SELECT clients.owner_name, product_name, services.service_name,
                r.quantity, sum(products.initial_cost * quantity + services.aditional_cost), r.entry_date, r.left_date,
                r.done, r.ID_Records FROM records r JOIN clients ON
                    r.ID_Clients = clients.ID_Clients
                JOIN products ON
                    r.ID_Products = products.ID_Products
                JOIN services ON
                    r.ID_Services = services.ID_Services
                GROUP BY r.ID_Records
                ORDER BY r.ID_Records
                DESC
                LIMIT 1;""",  # 7 actualización de listado en records.
                
                "INSERT INTO users ('name', 'passwd', 'mail', 'active') VALUES (?, ?, ?, ?);",  # 8 Insertar nuevo usuario.
                
                "SELECT name, mail FROM users;",  # 9 verificación en users para register.
                
                "SELECT name FROM users WHERE active = 1 LIMIT 1;",  # 10 identifica al usuario activo.
                
                "UPDATE users SET active = 0 WHERE name = ?;",  # 11 desmarca al usuario que estaba activo.
                
                """INSERT INTO records (ID_Services, ID_Clients, ID_Products) VALUES
                ((SELECT ID_Services FROM services WHERE service_name = ?), (SELECT ID_Clients FROM clients WHERE owner_name = ?),
                (SELECT ID_Products FROM products WHERE product_name = ?));""",  # 12 carga una linea en el registro.
                
                "SELECT name, passwd FROM users",  # 13 consulta todos los usuarios.
                
                "INSERT INTO ? (?) VALUES (?) WHERE ? = ?"
    ]
    return every_query


def login():
    login_strings = ["Register", "Ingreso incorrecto", "Usuario o contraseña incorrectos.", "logo.png",
                    "login.png", "forgot_pass.png"]
    return login_strings


def register():
    register_strings = ["Registro exitoso", "Cuenta registrada con exito.", "Este usuario ya se encuentra registrado.", "Correo"]
    return register_strings


def records():
    records_strings = ["Cliente", "Producto", "Nombre del Servicio", "Cantidad", "Precio Final",
                    "Fecha de Ingreso", "Fecha de Egreso", "Hecho", "Comandos", "ns",
                    "Modificar", "Borrar", "Encargo", "readonly", "center",
                    "Éxito", "Registro agregado correctamente.", "Error en la base de datos", "- Seleccione Cliente -", "- Seleccione Producto -",
                    "- Seleccione Servicio -", "Nuevo Servicio", "Encargar"]
    return records_strings


def clients():
    clients_strings = ["Nombre", "Teléfono", 'owner_name', 'phone', "Este cliente ya se encuentra registrado",
                    "Datos del Cliente", "El número no puede contener letras."]
    return clients_strings


def products():
    products_strings = ["Marca", "Modelo", "Costo Inicial", 'brand', 'model',
                        'initial_cost', "Datos del Producto", "Este producto ya se encuentra registrado", "El costo debe ser un número."]
    return products_strings

def menu():
    menu_strings = ['%H:%M', "clients.png", "clients_clicked.png", "records.png", "records_clicked.png",
                    "products.png", "products_clicked.png", "background.png", "watermark.png", "title_bar.png",
                    "menu_bar.png", "status_bar.png", "logo_icon.png", "user_icon.png", "date_icon.png",
                    "time_icon.png", "minimize.png", "close.png", "logout.png", "Records",
                    "commerce.png", "No disponible", "Esta funcionalidad solo es accesible en la versión completa.", "Clients", "Products",
                    "F2: Abrir Clientes\n\nF3: Abrir Productos\n\nF4: Abrir Registros\n\nF5: Modo Claro/Oscuro", "#555454", "Montserrat Bold", "Teclas Rápidas", "v0.9.6",
                    "Wipper Insumos", "Montserrat Medium", "<Button-1>", "<B1-Motion>", "<F2>",
                    "<F3>", "<F4>"]
    return menu_strings