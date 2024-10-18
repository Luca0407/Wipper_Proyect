def general():
    general_strings = ["#191919", "input.png", "#D9D9D9", "#000716", "Montserrat Regular",
                        '<Return>', "●", "exit.png", "sign_up.png", "nw",
                        "Usuario", "#FFFFFF",  "Contraseña", 'wipper.db', '<Escape>',
                        'source',  "forest-dark",  "right", "y",  "headings",
                        "ID", "<FocusIn>", "ew", "<FocusOut>", "Agregar",
                        "Cerrar", "nsew", "Advertencia", "ERROR"]
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
                
                "SELECT concat(brand, ' ', model) FROM products;"  # 6 verificación en products.
                ]
    return every_query

def login():
    login_strings = ["Menu", "Register", "Ingreso incorrecto", "Usuario o contraseña incorrectos.", "logo.png",
                    "login.png", "forgot_pass.png", "forgot_pass_button clicked"]
    return login_strings

def register():
    register_strings = ["Registro exitoso", "Cuenta registrada con exito.", "Login", "Este usuario ya se encuentra registrado.", "flat",
                        "Correo"]
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