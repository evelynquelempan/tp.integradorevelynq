

def buscar_codigo_ui(catalogo, prendas):
    print("\n--- BUSCAR PRENDA POR CÓDIGO ---")
    codigo = input("Ingresá el código de la prenda: ")
    prenda, comparaciones = catalogo.buscar_por_codigo(prendas, codigo)

    if prenda:
        print("Prenda encontrada:")
        print(prenda)
    else:
        print("No se encuentra la prenda con ese código.")
    print(f"Comparaciones realizadas: {comparaciones}")


def buscar_nombre_ui(catalogo, prendas):
    print("\n--- BUSCAR PRENDA POR NOMBRE ---")
    nombre = input("Ingresá el nombre de la prenda: ")
    encontradas, comparaciones = catalogo.buscar_por_nombre(prendas, nombre)

    if encontradas:
        print(f"Se encontraron {len(encontradas)} prendas con ese nombre:")
        for prenda in encontradas:
            print(prenda)
    else:
        print("No se encontraron prendas con ese nombre.")
    print(f"Comparaciones realizadas: {comparaciones}")


def talles_disponibles_ui(catalogo, prendas):
    print("\n--- TALLES DISPONIBLES ---")
    nombre = input("Ingresá el nombre de la prenda: ").strip().lower()

    # Búsqueda parcial: "jean" encuentra "Jean recto", "Jean mom", etc.
    encontradas = [p for p in prendas if nombre in p.nombre.lower()]

    if not encontradas:
        print("No se encontraron prendas con ese nombre.")
        return

    # Agrupa por nombre para mostrar todas las prendas encontradas
    grupos = {}
    for prenda in encontradas:
        grupos.setdefault(prenda.nombre, []).append(prenda)

    for nombre_prenda, lista in grupos.items():
        con_stock = [p for p in lista if p.disponible()]
        if con_stock:
            detalle = ", ".join(f"{p.talle} (stock {p.stock})" for p in con_stock)
            print(f"{nombre_prenda}: {detalle}")
        else:
            print(f"{nombre_prenda}: sin stock en ningún talle")

    print(f"Prendas revisadas: {len(prendas)}")