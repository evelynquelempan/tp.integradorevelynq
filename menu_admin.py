from prenda import Prenda
from busquedas_ui import buscar_codigo_ui, buscar_nombre_ui


def mostrar_menu_admin():
    print("\n========== MENÚ ADMINISTRADOR ==========")
    print("1. Listar prendas")
    print("2. Insertar una prenda")
    print("3. Buscar por código")
    print("4. Buscar por nombre")
    print("5. Modificar una prenda")
    print("6. Eliminar una prenda")
    print("7. Ver estadísticas")
    print("8. Ver historial de búsquedas")
    print("0. Cerrar sesión")
    print("========================================")


def _pedir_e_insertar(catalogo, prendas):
    print("\n--- INSERTAR NUEVA PRENDA ---")
    try:
        codigo = input("Ingresá el código: ")
        nombre = input("Ingresá el nombre: ")
        categoria = input("Ingresá la categoría: ")
        talle = input("Ingresá el talle: ")
        precio = float(input("Ingresá el precio: "))
        stock = int(input("Ingresá el stock: "))
        nueva = Prenda(codigo, nombre, categoria, talle, precio, stock)
        return catalogo.insertar_prenda(prendas, nueva)
    except ValueError as error:
        print(f"Error: {error}")
        return False


def menu_admin(catalogo, prendas, historial,
               mostrar_estadisticas=None, guardar=None):
    while True:
        mostrar_menu_admin()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            print(f"\nPrendas cargadas: {len(prendas)}")
            for prenda in prendas:
                print(prenda)

        elif opcion == "2":
            if _pedir_e_insertar(catalogo, prendas) and guardar:
                guardar(prendas)

        elif opcion == "3":
            buscar_codigo_ui(catalogo, prendas, historial)

        elif opcion == "4":
            buscar_nombre_ui(catalogo, prendas, historial)

        elif opcion == "5":
            codigo = input("Ingresá el código de la prenda que querés modificar: ")
            catalogo.modificar_prenda(prendas, codigo)
            if guardar:
                guardar(prendas)

        elif opcion == "6":
            codigo = input("Ingresá el código de la prenda que querés eliminar: ")
            catalogo.eliminar_prenda(prendas, codigo)
            if guardar:
                guardar(prendas)

        elif opcion == "7":
            if mostrar_estadisticas:
                mostrar_estadisticas(prendas)
            else:
                print("Estadísticas: función pendiente.")

        elif opcion == "8":
            historial.mostrar()

        elif opcion == "0":
            print("Sesión cerrada.")
            break

        else:
            print("Opción incorrecta. Por favor, elegí una opción válida.")

        input("\nPresioná Enter para volver al menú...")