manager = {}

# CREAR NUEVA CONTRASEÑA

def nueva_contrasena(user, account, password):
        
    if account == "" or user == "" or password == "":
        print("No ingresaste ningun dato...")
        return
    
    nueva_credencial = {
        "usuario" : user,
        "cuenta" : account,
        "contrasena" : password
    }
    
    manager.append(nueva_credencial)
    print("¡Credencial guardada con éxito!")
    
# EDITAR CONTRASEÑA
        
def editar_contrasena(lista_origen, cuenta_a_editar):
    
    encontrado = False

    for credencial in lista_origen:
        if credencial["cuenta"] == cuenta_a_editar:
            print("Registro encontrado. Ingrese los nuevos datos.")
            
            nuevo_account = input("Ingrese el nuevo nombre de la cuenta: ").strip().title()
            nuevo_user = input("Ingrese los nuevos datos de usuario: ").strip().title()
            nuevo_pass = input("Ingrese la nueva contraseña: ").strip()
            
            credencial["usuario"] = nuevo_user
            credencial["contrasena"] = nuevo_pass
            credencial["cuenta"] = nuevo_account
            
            encontrado = True
            break
        
    if encontrado == False:
        print("La cuenta ingresada no existe")
    
# ELIMINAR CONTRASEÑA
    
def eliminar_contrasena(lista_origen, cuenta_a_eliminar):
    
    encontrado = False

    for credencial in lista_origen:
        if credencial["cuenta"] == cuenta_a_eliminar:
            lista_origen.remove(credencial)
            print("¡Credencial eliminada con éxito!")
            encontrado = True
            break
    
    if encontrado == False:
        print("No se encontro ningun registro")
        
    
# VER CONTRASEÑA
    
def ver_contrasena(lista_origen):
    
    if lista_origen:
        print("Se encontraron registros")
        for credencial in lista_origen:
            print(f"Cuenta: {credencial['cuenta']} | Usuario: {credencial['usuario']} | Contraseña: {credencial['contrasena']}")
    else:
        print("No hay contraseñas guardadas en el sistema todavía.")
    
def buscar_contrasena(lista_origen, cuenta_buscada):
    
    encontrado = False

    for credencial in lista_origen:
        
        if credencial["cuenta"] == cuenta_buscada:
            print("\n=== CREDENCIAL ENCONTRADA ===")
            encontrado = True
            print(f"Cuenta: {credencial['cuenta']} | Usuario: {credencial['usuario']} | Contraseña: {credencial['contrasena']}")
        
    if encontrado == False:
        print("No se encontraron registros asociados a tu busqueda")
        
    
print("=====================================")
print("Sistema para gestion de contraseñas")
print("=====================================")

while True:
    
    print()
    print("===========================================")
    print("Seleccione alguna de las opciones del menú")
    print("===========================================")
    print()
    print("1. Nueva contraseña.")
    print("2. Editar contraseña.")
    print("3. Eliminar contraseña.")
    print("4. Ver contraseña.")
    print("5. Buscar contraseña.")
    print("6. Salir del sistema.")
    
    menu = input("Elija una opción")
        
    match menu:
        case "1":
            
            print("======================")
            print("Nueva contraseña.")
            print("======================")
            
            pregunta = input("¿Desea crear una nueva contraseña? (Escriba 'Si' para continuar o 'No' para salir)").strip().title()
            
            if pregunta == "Si":
        
                print("Paso 1: Ingrese el nombre de la cuenta")
                account = input("Ingrese el nombre de la cuenta: ").strip().title()
                
                print("Paso 1: Ingrese el mail del usuario")
                user = input("Ingrese mail o nombre de usuario: ").strip().title()
                
                print("Paso 1: Ingrese la contreaseña del usuario")
                password = input("Ingrese su contraseña: ").strip()
            
                nueva_contrasena(user, account, password)
            else:
                print("Operacion cancelada")
                
        case "2":
            
            print("======================")
            print("Editar contraseña.")
            print("======================")
            
            cuenta_modificar = input("¿Qué datos deseas modificar?: ").strip().title()
            editar_contrasena(manager, cuenta_modificar)
            
        case "3":
            
            print("======================")
            print("Eliminar contraseña.")
            print("======================")
            
            cuenta_borrar = input("¿Qué cuenta desea eliminar?: ").strip().title()
            eliminar_contrasena(manager, cuenta_borrar)
            
        case "4":
            
            print("======================")
            print("Ver contraseña.")
            print("======================")
            
            ver_contrasena(manager)
            
        case "5":
            
            print("======================")
            print("Buscar contraseña.")
            print("======================")
            
            pregunta = input("¿Que cuenta esta buscando?").strip().title()
            
            buscar_contrasena(manager, pregunta)
            
        case "6":
        
            print("Saliendo del sistema...")
            break
            
        case  _:
            print("Opción incorrecta")
            