from ui.busquedas_ui import (buscar_codigo_ui, buscar_nombre_ui, talles_disponibles_ui)
from estructuras.arbol_categorias import explorar_categorias


def mostrar_menu_cliente():
    print("\n========== MENÚ CLIENTE ==========")
    print("1. Explorar por categorías")
    print("2. Ver todas las prendas (precio y stock)")
    print("3. Buscar por código")
    print("4. Buscar por nombre")
    print("5. Ver talles disponibles de una prenda")
    print("0. Cerrar sesión")
    print("==================================")


def menu_cliente(catalogo, prendas, arbol_cat):
    while True:
        mostrar_menu_cliente()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            explorar_categorias(arbol_cat)
            

        elif opcion == "2":
            for prenda in prendas:
                print(prenda)

        elif opcion == "3":
            buscar_codigo_ui(catalogo, prendas)

        elif opcion == "4":
            buscar_nombre_ui(catalogo, prendas)

        elif opcion == "5":
            talles_disponibles_ui(catalogo, prendas)

        elif opcion == "0":
            print("Sesión cerrada.")
            break

        else:
            print("Opción incorrecta. Por favor, elegí una opción válida.")

        input("\nPresioná Enter para volver al menú...")