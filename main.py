from prenda import Prenda
from arbol_busqueda import ArbolBusqueda
from arbol_categorias import construir_arbol_categorias, explorar_categorias
from busquedas_ui import talles_disponibles_ui
from persistencia import cargar_prendas, guardar_prendas
import catalogo

# CARGA DE DATOS Y ÁRBOLES 
#  Cargamos las prendas desde JSON 
catalogo.prendas = cargar_prendas(prendas_iniciales=catalogo.prendas)

arbol = ArbolBusqueda()
arbol_cat = None

def sincronizar_todo():
    #Actualiza el árbol BST, el árbol de categorías y guarda en datos.json
    global arbol, arbol_cat
    
    # Reconstruye el BST
    arbol = ArbolBusqueda()
    for prenda in catalogo.prendas:
        arbol.insertar(prenda)

    # Reconstruye el árbol de categorías
    arbol_cat = construir_arbol_categorias(catalogo.prendas)

    # Guarda los cambios en el archivo JSON
    guardar_prendas(catalogo.prendas)

# Sincronización inicial al abrir el programa
sincronizar_todo()

# HISTORIAL DE BÚSQUEDAS,COLA  ===================
cola_historial = []
MAX_HISTORIAL = 5

def registrar_busqueda(texto):
    #Encola una búsqueda y si supera el máximo, en este caso es 5,  saca la más antigua (FIFO)
    cola_historial.append(texto)
    if len(cola_historial) > MAX_HISTORIAL:
        cola_historial.pop(0)  # <-- Sale el primero que entró (FIFO)


# ==================== MENÚ PRINCIPAL ====================

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
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
    print("0. Salir")
    print("====================================")


def menu_principal():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            print(f"\nPrendas cargadas: {len(catalogo.prendas)}")
            for prenda in catalogo.prendas:
                print(prenda)

        elif opcion == "2":
            # Explorar el árbol de categorías: Invierno, Verano, Otros y sus subcategorías
            explorar_categorias(arbol_cat)

        elif opcion == "3":
            # Listar prendas ordenadas por código usando el recorrido inorden del árbol
            print("\n--- PRENDAS ORDENADAS POR CÓDIGO (INORDEN) ---")
            for prenda in arbol.inorden():
                print(prenda)

        elif opcion == "4":
            print("\n--- BUSCAR PRENDA POR CÓDIGO ---")
            codigo_buscado = input("Ingresá el código de la prenda: ").strip()
            registrar_busqueda(f"Búsqueda por código: '{codigo_buscado}'")
            prenda, comparaciones = catalogo.buscar_por_codigo(catalogo.prendas, codigo_buscado)

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
            encontradas, comparaciones = catalogo.buscar_por_nombre(catalogo.prendas, nombre_buscado)

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
            codigo_buscado = input("Ingresá el código de la prenda que querés modificar: ").strip()
            if catalogo.modificar_prenda(catalogo.prendas, codigo_buscado):
                sincronizar_todo()

        elif opcion == "8":
            print("\n--- ELIMINAR PRENDA ---")
            codigo_buscado = input("Ingresá el código de la prenda que querés eliminar: ").strip()
            if catalogo.eliminar_prenda(catalogo.prendas, codigo_buscado):
                sincronizar_todo()

        elif opcion == "9":
            print("\n--- COMPARACIÓN DE BÚSQUEDAS ---")
            codigo_prueba = input("Ingresá un código para comparar (ej: P010): ").strip()

            # Búsqueda en la lista
            prenda, comp_lista = catalogo.buscar_por_codigo(catalogo.prendas, codigo_prueba)

            # Búsqueda en el árbol
            prenda_arbol, comp_arbol = arbol.buscar(codigo_prueba)

            print("Código buscado:", codigo_prueba)
            print("Comparaciones en la lista:", comp_lista)
            print("Comparaciones en el árbol:", comp_arbol)
        
        elif opcion == "10":
            talles_disponibles_ui(catalogo, catalogo.prendas)

        elif opcion == "11":
            print("\n--- HISTORIAL DE ÚLTIMAS BÚSQUEDAS (COLA FIFO) ---")
            if not cola_historial:
                print("Todavía no se realizaron búsquedas en esta sesión.")
            else:
                for i, busqueda in enumerate(cola_historial, 1):
                    print(f"{i}. {busqueda}")

        elif opcion == "0":
            print("Saliendo del menú...")
            break

        else:
            print("Opción incorrecta. Por favor, elegí una opción válida.")


if __name__ == "__main__":
    menu_principal()