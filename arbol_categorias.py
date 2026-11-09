# Clase del Nodo del Árbol
class NodoCategoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []  # Lista de hijos (otros NodoCategoria)
        self.elementos = []      # Prendas que pertenecen a esta categoría

    def agregar_subcategoria(self, nodo):
        self.subcategorias.append(nodo)

    def agregar_elemento(self, prenda):
        self.elementos.append(prenda)


# 2. Función para armar el árbol a partir de la lista de prendas
def construir_arbol_categorias(lista_prendas):
    # Raíz del árbol
    raiz = NodoCategoria("Indumentaria")

    # Estructura que diseñó tu compañero
    estructura = {
        "Invierno": ["Camperas", "Buzos", "Sweaters"],
        "Verano": ["Remeras", "Shorts", "Tops", "Polleras"],
        "Otros": ["Camisas", "Vestidos"]
    }

    # Armamos los nodos del árbol
    for nombre_padre, lista_hijos in estructura.items():
        nodo_padre = NodoCategoria(nombre_padre)

        for nombre_hijo in lista_hijos:
            nodo_hijo = NodoCategoria(nombre_hijo)

            # Colgamos las prendas que pertenecen a esta subcategoría
            for p in lista_prendas:
                if p.categoria.lower() == nombre_hijo.lower():
                    nodo_hijo.agregar_elemento(p)

            # Agregamos el hijo al nodo padre (Invierno, Verano, etc.)
            nodo_padre.agregar_subcategoria(nodo_hijo)

        # Agregamos el padre a la raíz (Indumentaria)
        raiz.agregar_subcategoria(nodo_padre)

    return raiz


# 3. Menú de navegación interactivo
def explorar_categorias(nodo_actual):
    while True:
        # Si llegamos a una categoría hoja que tiene prendas, las mostramos
        if nodo_actual.elementos:
            print(f"\n--- Prendas en '{nodo_actual.nombre}' ({len(nodo_actual.elementos)}) ---")
            for p in nodo_actual.elementos:
                print(f"• {p.nombre} | Talle: {p.talle} | Precio: ${p.precio} | Stock: {p.stock}")
            return

        # Si tiene subcategorías, mostramos el menú para seguir bajando
        print(f"\n--- Explorar: {nodo_actual.nombre} ---")
        for i, sub in enumerate(nodo_actual.subcategorias, 1):
            print(f"{i}. {sub.nombre}")
        print("0. Volver")

        try:
            opcion = int(input("Elegí una opción: "))
            if opcion == 0:
                break
            elif 1 <= opcion <= len(nodo_actual.subcategorias):
                # Bajamos recursivamente al nodo elegido
                explorar_categorias(nodo_actual.subcategorias[opcion - 1])
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor, ingresá un número.")