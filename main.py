# main.py
from prenda import Prenda
from arbol_busqueda import ArbolBusqueda
import catalogo

# ==================== CONFIGURACIÓN DEL ÁRBOL ====================

arbol = ArbolBusqueda()

def actualizar_arbol():
    global arbol
    arbol = ArbolBusqueda()
    for prenda in catalogo.prendas:
        arbol.insertar(prenda)

# Cargamos el árbol con las 30 prendas de la lista
actualizar_arbol()


# ==================== MENÚ PRINCIPAL ====================

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Listar prendas")
    print("2. Insertar una prenda")
    print("3. Buscar por código")
    print("4. Buscar por nombre")
    print("5. Modificar una prenda")
    print("6. Eliminar una prenda")
    print("7. Buscar por código (árbol)")
    print("8. Comparar búsqueda (Lista vs Árbol)")
    print("0. Salir")
    print("====================================")


def menu_principal():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            print(f"\nPrendas cargadas: {len(catalogo.prendas)}")
            for prenda in catalogo.prendas:
                print(prenda)

        elif opcion == "2":
            print("\n--- INSERTAR NUEVA PRENDA ---")
            try:
                codigo = input("Ingresá el código: ")
                nombre = input("Ingresá el nombre: ")
                categoria = input("Ingresá la categoría: ")
                talle = input("Ingresá el talle: ")
                precio = float(input("Ingresá el precio: "))
                stock = int(input("Ingresá el stock: "))

                nueva_prenda = Prenda(
                    codigo, nombre, categoria, talle, precio, stock
                )

                if catalogo.insertar_prenda(catalogo.prendas, nueva_prenda):
                    actualizar_arbol()

            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "3":
            print("\n--- BUSCAR PRENDA POR CÓDIGO ---")
            codigo_buscado = input("Ingresá el código de la prenda: ")
            prenda, comparaciones = catalogo.buscar_por_codigo(catalogo.prendas, codigo_buscado)

            if prenda:
                print("Prenda encontrada:")
                print(prenda)
            else:
                print("No se encuentra la prenda con ese código.")

            print(f"Comparaciones realizadas: {comparaciones}")

        elif opcion == "4":
            print("\n--- BUSCAR PRENDA POR NOMBRE ---")
            nombre_buscado = input("Ingresá el nombre de la prenda: ")
            encontradas, comparaciones = catalogo.buscar_por_nombre(catalogo.prendas, nombre_buscado)

            if encontradas:
                print(f"Se encontraron {len(encontradas)} prendas con ese nombre:")
                for prenda in encontradas:
                    print(prenda)
            else:
                print("No se encontraron prendas con ese nombre.")

            print(f"Comparaciones realizadas: {comparaciones}")

        elif opcion == "5":
            print("\n--- MODIFICAR PRENDA ---")
            codigo_buscado = input("Ingresá el código de la prenda que querés modificar: ")
            if catalogo.modificar_prenda(catalogo.prendas, codigo_buscado):
                actualizar_arbol()

        elif opcion == "6":
            print("\n--- ELIMINAR PRENDA ---")
            codigo_buscado = input("Ingresá el código de la prenda que querés eliminar: ")
            if catalogo.eliminar_prenda(catalogo.prendas, codigo_buscado):
                actualizar_arbol()

        elif opcion == "7":
            print("\n--- BUSCAR PRENDA EN EL ÁRBOL ---")
            codigo_buscado = input("Ingresá el código de la prenda: ")
            prenda, comparaciones = arbol.buscar(codigo_buscado)

            if prenda:
                print("Prenda encontrada:")
                print(prenda)
            else:
                print("No se encontró una prenda con ese código.")

            print(f"Comparaciones realizadas en el árbol: {comparaciones}")

        elif opcion == "8":
            print("\n--- COMPARACIÓN DE BÚSQUEDAS ---")
            codigo_prueba = input("Ingresá un código para comparar (ej: P010): ")

            # Búsqueda en la lista
            _, comp_lista = catalogo.buscar_por_codigo(catalogo.prendas, codigo_prueba)

            # Búsqueda en el árbol
            _, comp_arbol = arbol.buscar(codigo_prueba)

            print("Código buscado:", codigo_prueba)
            print("Comparaciones en la lista:", comp_lista)
            print("Comparaciones en el árbol:", comp_arbol)

        elif opcion == "0":
            print("Saliendo del menú...")
            break

        else:
            print("Opción incorrecta. Por favor, elegí una opción válida.")


if __name__ == "__main__":
    menu_principal()