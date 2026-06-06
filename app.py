from colorama import Back, Fore, Style, init
from logica_gestor import *
init(autoreset=True)

print(f"{Fore.CYAN}=====================================")
print(f"{Fore.CYAN}Sistema para gestion de contraseñas")
print(f"{Fore.CYAN}======================================{Style.RESET_ALL}")

manager = {}

while True:
    
    print()
    print(f"{Fore.CYAN}===========================================")
    print(f"{Fore.CYAN}Seleccione alguna de las opciones del menú")
    print(f"{Fore.CYAN}==========================================={Style.RESET_ALL}")
    print()
    print(f"{Back.WHITE + Fore.CYAN}1. Nueva contraseña.")
    print(f"{Back.YELLOW + Fore.CYAN}2. Editar contraseña.")
    print(f"{Back.RED + Fore.WHITE}3. Eliminar contraseña.")
    print(f"{Back.GREEN + Fore.WHITE}4. Ver contraseña.")
    print(f"{Back.WHITE + Fore.CYAN}5. Buscar contraseña.")
    print(f"{Back.RED + Fore.WHITE}6. Salir del sistema.")
    
    menu = input("Elija una opción: ")
        
    match menu:
        case "1":
            
            print(f"{Fore.CYAN}======================")
            print(f"{Fore.CYAN}Nueva contraseña.")
            print(f"{Fore.CYAN}======================{Style.RESET_ALL}")
            
            pregunta = input("¿Desea crear una nueva contraseña? (Escriba 'Si' para continuar o 'No' para salir) ").strip().title()
            
            if pregunta == "Si":
        
                print(f"{Fore.GREEN}Paso 1: Ingrese el nombre de la cuenta")
                account = input("Ingrese el nombre de la cuenta: ").strip().title()
                
                print(f"{Fore.GREEN}Paso 2: Ingrese el mail del usuario")
                user = input("Ingrese mail o nombre de usuario: ").strip().title()
                
                print(f"{Fore.GREEN}Paso 3: Ingrese la contreaseña del usuario")
                password = input("Ingrese su contraseña: ").strip()
            
                nueva_contrasena(manager, user, account, password)
            else:
                print(f"{Fore.CYAN}Operacion cancelada")
                
            print(f"{Back.GREEN + Fore.WHITE}Guardado con éxito!{Style.RESET_ALL}")
                
        case "2":
            
            print(f"{Fore.CYAN}======================")
            print(f"{Fore.CYAN}Editar contraseña.")
            print(f"{Fore.CYAN}======================{Style.RESET_ALL}")
            
            cuenta_modificar = input("¿Qué datos deseas modificar?: ").strip().title()
            editar_contrasena(manager, cuenta_modificar)
            
        case "3":
            
            print(f"{Fore.CYAN}======================")
            print(f"{Fore.CYAN}Eliminar contraseña.")
            print(f"{Fore.CYAN}======================{Style.RESET_ALL}")
            
            cuenta_borrar = input("¿Qué cuenta desea eliminar?: ").strip().title()
            eliminar_contrasena(manager, cuenta_borrar)
            
        case "4":
            
            print(f"{Fore.CYAN}======================")
            print(f"{Fore.CYAN}Ver contraseña.")
            print(f"{Fore.CYAN}======================{Style.RESET_ALL}")
            
            ver_contrasena(manager)
            
        case "5":
            
            print(f"{Fore.CYAN}======================")
            print(f"{Fore.CYAN}Buscar contraseña.")
            print(f"{Fore.CYAN}======================{Style.RESET_ALL}")
            
            pregunta = input("¿Que cuenta esta buscando?").strip().title()
            
            buscar_contrasena(manager, pregunta)
            
        case "6":
        
            print(f"{Fore.YELLOW}Saliendo del sistema...")
            break
            
        case  _:
            print(f"{Fore.RED}Opción incorrecta")
            