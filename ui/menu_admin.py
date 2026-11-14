
from modelos.prenda import Prenda
from estructuras.arbol_categorias import explorar_categorias
from ui.busquedas_ui import talles_disponibles_ui


# ==================== MENÚ ADMINISTRADOR ====================

def mostrar_menu_admin():
    print("\n========== MENÚ ADMINISTRADOR ==========")
    print("1. Listar prendas")
    print("2. Explorar por categorías")
    print("3. Listar prendas ordenadas por código")
    print("4. Buscar por código")
    print("5. Buscar por nombre")
    print("6. Insertar una prenda")
    print("7. Modificar una prenda")
    print("8. Eliminar una prenda")
    print("9. Comparar búsqueda (Lista vs Árbol)")
    print("10. Consultar talles disponibles de una prenda")
    print("11. Ver historial de búsquedas recientes")
    print("0. Cerrar sesión")
    print("========================================")


def menu_admin(catalogo, sincronizar_todo, registrar_busqueda,
               obtener_arboles, obtener_historial):

    while True:
        mostrar_menu_admin()
        opcion = input("Elegí una opción: ").strip()

        # Obtenemos los árboles actualizados
        arbol, arbol_cat = obtener_arboles()

        if opcion == "1":
            print(f"\nPrendas cargadas: {len(catalogo.prendas)}")
            for prenda in catalogo.prendas:
                print(prenda)

        elif opcion == "2":
            explorar_categorias(arbol_cat)

        elif opcion == "3":
            print("\n--- PRENDAS ORDENADAS POR CÓDIGO (INORDEN) ---")
            for prenda in arbol.inorden():
                print(prenda)

        elif opcion == "4":
            print("\n--- BUSCAR PRENDA POR CÓDIGO ---")
            codigo_buscado = input("Ingresá el código de la prenda: ").strip()

            registrar_busqueda(f"Búsqueda por código: '{codigo_buscado}'")

            prenda, comparaciones = catalogo.buscar_por_codigo(
                catalogo.prendas, codigo_buscado
            )

            if prenda:
                print("Prenda encontrada:")
                print(prenda)
            else:
                print("No se encuentra la prenda con ese código.")

            print(f"Comparaciones realizadas en la lista: {comparaciones}")

        elif opcion == "5":
            print("\n--- BUSCAR PRENDA POR NOMBRE ---")
            nombre_buscado = input("Ingresá el nombre de la prenda: ").strip()

            registrar_busqueda(f"Búsqueda por nombre: '{nombre_buscado}'")

            encontradas, comparaciones = catalogo.buscar_por_nombre(
                catalogo.prendas, nombre_buscado
            )

            if encontradas:
                print(f"Se encontraron {len(encontradas)} prendas con ese nombre:")
                for prenda in encontradas:
                    print(prenda)
            else:
                print("No se encontraron prendas con ese nombre.")

            print(f"Comparaciones realizadas: {comparaciones}")

        elif opcion == "6":
            print("\n--- INSERTAR NUEVA PRENDA ---")

            try:
                codigo = input("Ingresá el código: ").strip()
                nombre = input("Ingresá el nombre: ").strip()
                categoria = input("Ingresá la categoría: ").strip()
                talle = input("Ingresá el talle: ").strip()
                precio = float(input("Ingresá el precio: "))
                stock = int(input("Ingresá el stock: "))

                nueva_prenda = Prenda(
                    codigo, nombre, categoria, talle, precio, stock
                )

                if catalogo.insertar_prenda(catalogo.prendas, nueva_prenda):
                    sincronizar_todo()

            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "7":
            print("\n--- MODIFICAR PRENDA ---")
            codigo_buscado = input(
                "Ingresá el código de la prenda que querés modificar: "
            ).strip()

            if catalogo.modificar_prenda(catalogo.prendas, codigo_buscado):
                sincronizar_todo()

        elif opcion == "8":
            print("\n--- ELIMINAR PRENDA ---")
            codigo_buscado = input(
                "Ingresá el código de la prenda que querés eliminar: "
            ).strip()

            if catalogo.eliminar_prenda(catalogo.prendas, codigo_buscado):
                sincronizar_todo()

        elif opcion == "9":
            print("\n--- COMPARACIÓN DE BÚSQUEDAS ---")
            codigo_prueba = input(
                "Ingresá un código para comparar (ej: P010): "
            ).strip()

            # Búsqueda secuencial en la lista
            prenda, comp_lista = catalogo.buscar_por_codigo(
                catalogo.prendas, codigo_prueba
            )

            # Búsqueda en el árbol binario
            prenda_arbol, comp_arbol = arbol.buscar(codigo_prueba)

            print("Código buscado:", codigo_prueba)
            print("Comparaciones en la lista:", comp_lista)
            print("Comparaciones en el árbol:", comp_arbol)

        elif opcion == "10":
            talles_disponibles_ui(catalogo, catalogo.prendas)

        elif opcion == "11":
            print("\n--- HISTORIAL DE ÚLTIMAS BÚSQUEDAS (COLA FIFO) ---")

            historial = obtener_historial()

            if not historial:
                print("Todavía no se realizaron búsquedas en esta sesión.")
            else:
                for i, busqueda in enumerate(historial, 1):
                    print(f"{i}. {busqueda}")

        elif opcion == "0":
            print("\nCerrando sesión de administrador...")
            break

        else:
            print("Opción incorrecta. Por favor, elegí una opción válida.")
