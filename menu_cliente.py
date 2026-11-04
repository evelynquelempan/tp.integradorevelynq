from busquedas_ui import (buscar_codigo_ui, buscar_nombre_ui,
                          talles_disponibles_ui)


def mostrar_menu_cliente():
    print("\n========== MENÚ CLIENTE ==========")
    print("1. Explorar por categorías")
    print("2. Ver todas las prendas (precio y stock)")
    print("3. Buscar por código")
    print("4. Buscar por nombre")
    print("5. Ver talles disponibles de una prenda")
    print("6. Ver mis últimas búsquedas")
    print("0. Cerrar sesión")
    print("==================================")


def menu_cliente(catalogo, prendas, historial, explorar_categorias=None):
    while True:
        mostrar_menu_cliente()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            if explorar_categorias:
                explorar_categorias(prendas)
            else:
                print("Explorar por categorías: función pendiente.")

        elif opcion == "2":
            for prenda in prendas:
                print(prenda)

        elif opcion == "3":
            buscar_codigo_ui(catalogo, prendas, historial)

        elif opcion == "4":
            buscar_nombre_ui(catalogo, prendas, historial)

        elif opcion == "5":
            talles_disponibles_ui(catalogo, prendas, historial)

        elif opcion == "6":
            historial.mostrar()

        elif opcion == "0":
            print("Sesión cerrada.")
            break

        else:
            print("Opción incorrecta. Por favor, elegí una opción válida.")

        input("\nPresioná Enter para volver al menú...")