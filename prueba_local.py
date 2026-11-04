#Esto es para poder probar el inicio de sesion y el menu de administrador y cliente sin tener que pasar por el menu principal.

# usuario: cliente contra: cliente123
# admin: admin contra: admin123

#Problemas encontrados:

# 1: - No se puede iniciar sesion sin antes salir del menu principal de MAIN y dará errror al intentar ingresar ya que el menu principal tiene un bucle. 
#  Esto hace que no se pueda probar el inicio de sesion de admin y el menu de administrador y cliente sin tener que pasar por el menu principal. 

#Explicacion de Calude: Te lo explico claro porque el problema de fondo es este: el menú de main.py está dentro de un while True suelto, no es una función, y Python no tiene forma de llamar a un bloque suelto desde otro archivo sin ejecutarlo entero (o sin copiarlo).

#Solución 1: agregar al final de main.py
#  if __name__ == "__main__":
#    menu_principal()
#  y poner el menu dentro de una funcion menu_principal() para que se pueda llamar desde otro archivo y no se ejecute al importar main.py

#Solucion 2: si no toco main.py, debo crear un menu nuevo para admin sin utilizar el menu de main.py. 


# 3: En el menu principal de MAIN, al buscar una prenda debe coincidir el nombre exacto. Al buscar por una palabra parcial, por ejemplo "Jean" no figuran. 

#Solución: Cambiar         if prenda.nombre.lower() == nombre_buscado.lower():     por        if nombre_buscado.lower() in prenda.nombre.lower(): en la funcion buscar_prenda_por_nombre(nombre_buscado, prendas) de main.py




import main as catalogo   
from autenticacion import iniciar_sesion
from menu_admin import menu_admin
from menu_cliente import menu_cliente


def mostrar_menu_inicio():
    print("\n========== TIENDA DE ROPA ==========")
    print("1. Iniciar sesión")
    print("0. Salir")
    print("====================================")


def main():
    
    while True:
        mostrar_menu_inicio()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            usuario = iniciar_sesion()

            if usuario is None:
                print("Saliendo del sistema...")
                break

            if usuario.es_administrador():
                menu_admin(catalogo, catalogo.prendas)
            else:
                menu_cliente(catalogo, catalogo.prendas)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción incorrecta. Por favor, elegí una opción válida.")


if __name__ == "__main__":
    main()