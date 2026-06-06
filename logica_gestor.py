from colorama import Back, Fore, Style, init
init()

"""
diccionario_datos (dict): El diccionario que aloja los pares clave-valor con las cuentas y sus claves de forma segura.
cuenta_a_editar (str): El nombre de la cuenta (clave) que el usuario desea localizar para modificar sus datos.

"""

# CREAR NUEVA CONTRASEÑA

def nueva_contrasena(diccionario_datos, user, account, password):
    
    """
    PROPÓSITO
    
    Esta funcion es la encargada de crear ujna nueva contraseña.
    
    
    ¿COMO ES SU FUNCIONAMIENTO?
    
    Hace uso de la cuenta del sitio web como clave unica en el dicionario, esto permite que el sistema asocie el nombre del sitio web con sus credenciales sin tener que buscar en una lista de registros.
    
    
    VALIDACIÓN:
    
    Se incluye un (if) inicial para asegurar que no se guarden campos vacios lo que hace al programa mas robusto.
    
    """
        
    if account == "" or user == "" or password == "":
        print("No ingresaste ningun dato..." + Fore.YELLOW + Style.RESET_ALL)
        return False
    
    diccionario_datos[account] = {
        "usuario" : user,
        "contrasena" : password
    }
    return True
    
# EDITAR CONTRASEÑA
        
def editar_contrasena(diccionario_datos, cuenta_a_editar):
    
    """
    PROPÓSITO
    
    Actualiza el usuario o la clave de una cuenta ya existente.
    
    
    ¿COMO ES SU FUNCIONAMIENTO?
    
    .get() -> Usamos este metodo para intentar recuperar los datos. si la cuenta no existe no devolverá None en lugar de un error.
    Lógica condicional -> if datos_actuales: actúa como un interruptor. Si hay datos pide la nueva información si no avisa con un error. 
    
    
    REASIGNACIÓN:
    
    Al final se sobreescribe el "casillero" de la cuenta cion el nuevo dato.
    
    """

    datos_actuales = diccionario_datos.get(cuenta_a_editar)
    
    if datos_actuales:
        
        print("Registro encontrado. Ingrese los nuevos datos." + Back.GREEN + Fore.WHITE + Style.RESET_ALL)
        nuevo_user = input("Ingrese los nuevos datos de usuario: ").strip().title()
        nuevo_pass = input("Ingrese la nueva contraseña: ").strip()
        
        diccionario_datos[cuenta_a_editar] = {"usuario" : nuevo_user, "contrasena" : nuevo_pass}
    else:
        print("La cuenta ingresada no existe" + Back.RED + Fore.WHITE + Style.RESET_ALL)
        
# ELIMINAR CONTRASEÑA
    
def eliminar_contrasena(diccionario_datos, cuenta_a_eliminar):
    
    """
    PROPÓSITO
    
    Eliminar una credencial especifica del sistema.
    
    
    ¿COMO ES SU FUNCIONAMIENTO?
    
    Empleamos el operador (in) para verificar si la cuenta existe.
    .pop() -> Es el encargado de eliminarla de la memoria de forma instantanea esto eliminando la necesidad de recorrer toda la base de datos una por una.
    
    """
        
    if cuenta_a_eliminar in diccionario_datos:
        diccionario_datos.pop(cuenta_a_eliminar)
        print("¡Credencial eliminada con éxito!" + Back.GREEN + Fore.WHITE + Style.RESET_ALL)
    else:
        print(f"Error: La cuenta '{cuenta_a_eliminar}' no se encontró en el sistema." + Back.RED + Fore.WHITE + Style.RESET_ALL)
    
# VER CONTRASEÑA
    
def ver_contrasena(diccionario_datos):
    
    """
    PROPÓSITO
    
    Muestra las cedenciales guardadas de forma ordenada.
    
    
    ¿COMO ES SU FUNCIONAMIENTO?
    
    .items() -> Es el encargado de desempaquetar el diccionario en dos variables "cuenta (la llave)" y "datos (el valor / mini-diccionario)"
    
    ACCESO:
    
    Internamente en el bucle, entramnos a las llaves "usuario" y "contraseña" para imprimir la informacion final.
    
    """
    
    for cuenta, datos in diccionario_datos.items():
        print(f"Cuenta: {cuenta} | Usuario: {datos['usuario']} | Contraseña: {datos['contrasena']}" + Fore.YELLOW + Style.RESET_ALL)
        
        
# BUSCAR CONTRASEÑA

def buscar_contrasena(diccionario_datos, cuenta_buscada):
    
    encontrado = False

    resultado = diccionario_datos.get(cuenta_buscada)

    if resultado:
        print(f"Usuario: {resultado['usuario']}" + Fore.YELLOW + Style.RESET_ALL)
    else:
        print("No se encontró el registro." + Back.RED + Fore.WHITE + Style.RESET_ALL)
        
    if encontrado == False:
        print("No se encontraron registros asociados a tu busqueda" + Back.RED + Fore.WHITE + Style.RESET_ALL)