import sqlite3
import random
from colorama import Back, Fore, Style, init
init()

conexion = sqlite3.connect("gestor.db")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS gestor(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cuenta TEXT NOT NULL,
        usuario TEXT NOT NULL,
        contrasena TEXT NULL
    )
''')
conexion.commit()

# CREAR NUEVA CONTRASEÑA

def nueva_contrasena(diccionario_datos, user, account, password):

    """
    Registra credenciales en la base de datos y sincroniza el diccionario local.
    
    Parámetros:
        diccionario_datos (dict): Diccionario de trabajo en memoria.
        user (str): Nombre de usuario o mail.
        account (str): Nombre del sitio o aplicación.
        password (str): Contraseña a guardar.
    """

    if account == "" or user == "" or password == "":
        print("No ingresaste ningun dato..." + Fore.YELLOW + Style.RESET_ALL)
        return False
    
    try:
        cursor.execute('INSERT INTO gestor(usuario, cuenta, contrasena)VALUES(?,?,?)', (user, account, password))
        id_generado = cursor.lastrowid
        conexion.commit()
    
        diccionario_datos[account] = {
            "id" : id_generado,
            "usuario" : user,
            "contrasena" : password
        }
        
        print(Fore.GREEN + "¡Guardado con éxito en el sistema!" + Style.RESET_ALL)
        
    except sqlite3.Error as e:
        conexion.rollback()
        print(Fore.RED + f"Error al guardar en la base de datos: {e}" + Style.RESET_ALL)

    
    return True
    
# EDITAR CONTRASEÑA
        
def editar_contrasena(diccionario_datos, cuenta_a_editar):
    
    """
    Actualiza el usuario y clave de un registro existente en la DB y el diccionario.
    
    Parámetros:
        diccionario_datos (dict): Diccionario de sincronización.
        cuenta_a_editar (str): Nombre de la cuenta que se desea modificar.
    """

    datos_actuales = diccionario_datos.get(cuenta_a_editar)

    if datos_actuales:

        print("Registro encontrado. Ingrese los nuevos datos." + Back.GREEN + Fore.WHITE + Style.RESET_ALL)

        nuevo_user = input("Ingrese los nuevos datos de usuario: ").strip().title()
        nuevo_pass = input("Ingrese la nueva contraseña: ").strip()
        
        try:
            cursor.execute('UPDATE gestor SET usuario = ?, contrasena = ? WHERE cuenta = ?', (nuevo_user, nuevo_pass, cuenta_a_editar))
            diccionario_datos[cuenta_a_editar] = {"usuario" : nuevo_user, "contrasena" : nuevo_pass}
            conexion.commit()
            
        except sqlite3.Error as e:
            conexion.rollback()
            print(Fore.RED + f"Error al editar en la base de datos: {e}" + Style.RESET_ALL)
        
    else:
        print("La cuenta ingresada no existe" + Back.RED + Fore.WHITE + Style.RESET_ALL)

# ELIMINAR CONTRASEÑA
    
def eliminar_contrasena(diccionario_datos, cuenta_a_eliminar):
    
    """
    Borra una credencial del sistema tras doble confirmación del usuario.
    
    Parámetros:
        diccionario_datos (dict): Diccionario de sincronización.
        cuenta_a_eliminar (str): Nombre de la cuenta a dar de baja.
    """

    confirmar_eliminacion = input("Confirma que desea eliminar esta cuenta? Esta accion no se puede revertir Si/No ").strip().lower()
    
    if confirmar_eliminacion == "si":
        segunda_confirmacion = input("Realmente esta seguro? Si/No").strip().lower()
        
        if segunda_confirmacion == "si":
            
            try:
                cursor.execute('DELETE FROM gestor WHERE cuenta = ?', (cuenta_a_eliminar,))
                conexion.commit()
                
                if cuenta_a_eliminar in diccionario_datos:
                    diccionario_datos.pop(cuenta_a_eliminar)
                    print("¡Credencial eliminada con éxito!" + Back.GREEN + Fore.WHITE + Style.RESET_ALL)
                else:
                    print(f"Error: La cuenta '{cuenta_a_eliminar}' no se encontró en el sistema." + Back.RED + Fore.WHITE + Style.RESET_ALL)
            except sqlite3.Error as e:
                conexion.rollback()
                print(Fore.RED + f"Error al eliminar un registro en la base de datos: {e}" + Style.RESET_ALL)

            print(f"Registro eliminado...")
    else:
        print(f"No se elimino el registro.")

# CARGAR DATOS

def cargar_datos():
    """
    Consulta la tabla 'gestor' y reconstruye el diccionario en memoria.
    
    Retorna:
        dict: Diccionario sincronizado con los datos persistentes del disco.
    """
    try:
        cursor.execute('SELECT * FROM gestor')
        filas = cursor.fetchall()
    except sqlite3.Error as e:
        conexion.rollback()
        print(Fore.RED + f"Error al cargar los registros de la base de datos: {e}" + Style.RESET_ALL)
        return {}
        

    diccionario_cargado = {}
    for f in filas:
        diccionario_cargado[f[1]] = {
            "id" : f,
            "usuario" : f[2],
            "contrasena" : f[3]
        }
    return diccionario_cargado
    
# VER CONTRASEÑA
    
def ver_contrasena(diccionario_datos):
    
    """
    Muestra en pantalla todas las credenciales cargadas de forma ordenada.
    
    Parámetros:
    diccionario_datos (dict): El diccionario que contiene la información.
    """
    
    if not diccionario_datos:
        print(Fore.RED + "No hay credenciales guardadas." + Style.RESET_ALL)
        return
    
    for cuenta, datos in diccionario_datos.items():
        print(f"Cuenta: {cuenta} | Usuario: {datos['usuario']} | Contraseña: {datos['contrasena']}" + {Fore.YELLOW} + {Style.RESET_ALL})

# BUSCAR CONTRASEÑA

def buscar_contrasena(diccionario_datos, cuenta_buscada):
    
    """
    Realiza una consulta filtrada en la base de datos para hallar una cuenta específica.
    
    Parámetros:
        cuenta_buscada (str): Nombre de la cuenta a localizar.
    """

    cursor.execute('SELECT * FROM gestor WHERE cuenta = ?', (cuenta_buscada,))
    cuenta_encontrada = cursor.fetchone()
    
    if cuenta_encontrada:
        print(f"Cuenta encontrada - Usuario: {cuenta_encontrada[2]} | Contraseña: {cuenta_encontrada[3]}")
    else: 
        print("Registro no encontrado.")

# GENERAR SUGERENCIA

def generar_sugerencia():
    
    """
    Genera una cadena aleatoria de caracteres para proponer como contraseña segura.
    
    Retorna:
        str: Una contraseña sugerida de alta complejidad.
    """

    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "1234567890"
    simbolos_y_signos = "!@#$%^&*()_+=-{ }[ ]';/.?<>,\|"
    
    todos = mayusculas + minusculas + numeros + simbolos_y_signos

    while True:
        solicitud = input("¿Cuántos caracteres desea para su contraseña? ")
        if solicitud.isdigit():
            longitud_numero = int(solicitud)
            break
        print("ERROR: Debes ingresar solo números. Intenta de nuevo.")

    if longitud_numero < 8:
        print(f"Contraseña muy insegura{Fore.RED + Style.RESET_ALL}")
    elif longitud_numero <= 12:
        print(f"Contraseña insegura{Fore.RED + Style.RESET_ALL}")
    else:
        print(f"Contraseña segura{Fore.GREEN + Style.RESET_ALL}")
        
    clave = "".join(random.choice(todos) for _ in range(longitud_numero))
    return clave

conexion.close()