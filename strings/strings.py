def general():
    general_strings = ["#191919", "input.png", "#D9D9D9", "#000716", "Montserrat Regular",
                        '<Return>', "●", "exit.png", "sign_up.png", "nw",
                        "Usuario", "#FFFFFF",  "Contraseña", 'wipper.db', '<Escape>',
                        'source',  "forest-dark",  "right", "y",  "headings",
                        "ID", "<FocusIn>", "ew", "<FocusOut>", "Agregar",
                        "Cerrar", "nsew", "Advertencia", "ERROR", "Menu",
                        "Login", "flat"]
    return general_strings


def queries():
    every_query = ["""SELECT ID_Services, concat('(', clients.ID_Clients, ') - ', clients.owner_name), concat(products.brand, ' ',
                    products.model), service_name, quantity, sum(products.initial_cost * quantity + aditional_cost ), entry_date,
                    left_date, done
                FROM services
                JOIN clients ON
                    services.ID_Clients = clients.ID_Clients
                JOIN products ON
                    services.ID_Products = products.ID_Products
                GROUP BY ID_Services;""",  # 0 listado en records.
                
                "SELECT * FROM clients;",  # 1 listado en clients.
                
                "SELECT * FROM clients ORDER BY ID_Clients DESC LIMIT 1;",  # 2 actualización de listado en clients.
                
                "SELECT phone FROM clients;",  # 3 verificación en clients.
                
                "SELECT ID_Products, brand, model, initial_cost FROM products;",  # 4 listado en products.
                
                """SELECT ID_Products, brand, model, initial_cost
                    FROM products ORDER BY ID_Products DESC LIMIT 1;""",  # 5 actualización de listado en products.
                
                "SELECT concat(brand, ' ', model) FROM products;",  # 6 verificación en products.
                
                """SELECT ID_Services, concat('(', clients.ID_Clients, ') - ', clients.owner_name), concat(products.brand, ' ',
                    products.model), service_name, quantity, sum(products.initial_cost * quantity + aditional_cost ), entry_date,
                    left_date, done
                FROM services
                JOIN clients ON
                    services.ID_Clients = clients.ID_Clients
                JOIN products ON
                    services.ID_Products = products.ID_Products
                GROUP BY ID_Services
                ORDER BY ID_Services
                DESC
                LIMIT 1;"""  # 7 actualización de listado en records.
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
    records_strings = ["Servicio", "Cliente", "Producto", "Nombre del Servicio", "Cantidad",
                        "Precio Final", "Fecha de Ingreso", "Fecha de Egreso", "Hecho", "Comandos",
                        "ns", "Modificar", "Borrar"]
    return records_strings


def clients():
    clients_strings = ["Nombre", "Apellido", "Teléfono", 'owner_name', 'owner_surname',
                        'phone', "Este cliente ya se encuentra registrado", "Datos del Cliente", "El número no puede contener letras."]
    return clients_strings


def products():
    products_strings = ["Marca", "Modelo", "Costo Inicial", 'brand', 'model',
                        'initial_cost', "Datos del Producto", "Este producto ya se encuentra registrado", "El costo debe ser un número."]
    return products_strings

def menu():
    menu_strings = ['%H:%M', '%d/%m/%Y', "clients.png", "clients_clicked.png", "records.png",
                    "records_clicked.png", "products.png", "products_clicked.png", "ridge", "background.png",
                    "watermark.png", "title_bar.png", "menu_bar.png", "status_bar.png", "logo_icon.png",
                    "user_icon.png", "date_icon.png", "time_icon.png", "minimize.png","close.png",
                    "logout.png", "Records", "commerce.png", "No disponible", "Esta funcionalidad solo es accesible en la versión completa.",
                    "Clients", "Products", "F2: Abrir Clientes\n\nF3: Abrir Productos\n\nF4: Abrir Registros\n\nF5: Modo Claro/Oscuro", "#555454", "Montserrat Bold",
                    "Teclas Rápidas", "v0.8.3.1", "Wipper Insumos", "Montserrat Medium", "<Button-1>",
                    "<B1-Motion>", "<F2>", "<F3>", "<F4>"]
    return menu_strings