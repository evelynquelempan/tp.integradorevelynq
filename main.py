
from estructuras.arbol_busqueda import ArbolBusqueda
from estructuras.arbol_categorias import (construir_arbol_categorias, explorar_categorias )
from servicios.persistencia import cargar_prendas, guardar_prendas
from servicios.autenticacion import iniciar_sesion
from ui.menu_admin import menu_admin
from ui.menu_cliente import menu_cliente
import datos.catalogo as catalogo


# CARGA DE DATOSv

catalogo.prendas = cargar_prendas(
    prendas_iniciales=catalogo.prendas
)

arbol = ArbolBusqueda()
arbol_cat = None



# SINCRONIZACIÓN DE ESTRUCTURAS ===================

def sincronizar_todo():
    global arbol, arbol_cat

    # Reconstruir el árbol binario de búsqueda
    arbol = ArbolBusqueda()

    for prenda in catalogo.prendas:
        arbol.insertar(prenda)

    # Reconstruir el árbol de categorías
    arbol_cat = construir_arbol_categorias(catalogo.prendas)

    # Guardar los cambios en el archivo JSON
    guardar_prendas(catalogo.prendas)


def obtener_arboles():
    return arbol, arbol_cat


# Construir los árboles al iniciar el programa
sincronizar_todo()


# HISTORIAL DE BÚSQUEDAS (COLA FIFO)

cola_historial = []
MAX_HISTORIAL = 5


def registrar_busqueda(texto):
    cola_historial.append(texto)

    if len(cola_historial) > MAX_HISTORIAL:
        cola_historial.pop(0)


def obtener_historial():
    return cola_historial



# INICIO Y DISTRIBUCIÓN DE MENÚS  ===========

def main():
    print("\n========== TIENDA DE ROPA ==========")

    while True:
        usuario = iniciar_sesion()

        # Si no se pudo iniciar sesión, finalizar
        if usuario is None:
            print("Programa finalizado.")
            break

        # Menú según el rol del usuario
        if usuario.es_administrador():
            menu_admin(
                catalogo,
                sincronizar_todo,
                registrar_busqueda,
                obtener_arboles,
                obtener_historial
            )

        else:
            menu_cliente(
                catalogo,
                catalogo.prendas,
                arbol_cat
            )

        print("\nVolviendo al inicio de sesión...")


if __name__ == "__main__":
    main()
