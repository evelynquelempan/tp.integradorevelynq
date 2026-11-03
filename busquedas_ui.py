

def buscar_codigo_ui(catalogo, prendas, historial):
    print("\n--- BUSCAR PRENDA POR CÓDIGO ---")
    codigo = input("Ingresá el código de la prenda: ")
    prenda, comparaciones = catalogo.buscar_por_codigo(prendas, codigo)
    historial.registrar("Código", codigo)

    if prenda:
        print("Prenda encontrada:")
        print(prenda)
    else:
        print("No se encuentra la prenda con ese código.")
    print(f"Comparaciones realizadas: {comparaciones}")


def buscar_nombre_ui(catalogo, prendas, historial):
    print("\n--- BUSCAR PRENDA POR NOMBRE ---")
    nombre = input("Ingresá el nombre de la prenda: ")
    encontradas, comparaciones = catalogo.buscar_por_nombre(prendas, nombre)
    historial.registrar("Nombre", nombre)

    if encontradas:
        print(f"Se encontraron {len(encontradas)} prendas con ese nombre:")
        for prenda in encontradas:
            print(prenda)
    else:
        print("No se encontraron prendas con ese nombre.")
    print(f"Comparaciones realizadas: {comparaciones}")


def talles_disponibles_ui(catalogo, prendas, historial):
    print("\n--- TALLES DISPONIBLES ---")
    nombre = input("Ingresá el nombre de la prenda: ")
    encontradas, comparaciones = catalogo.buscar_por_nombre(prendas, nombre)
    historial.registrar("Talles", nombre)

    if not encontradas:
        print("No se encontraron prendas con ese nombre.")
    else:
        con_stock = [p for p in encontradas if p.disponible()]
        if con_stock:
            detalle = ", ".join(f"{p.talle} (stock {p.stock})" for p in con_stock)
            print(f"{encontradas[0].nombre}: {detalle}")
        else:
            print(f"{encontradas[0].nombre}: sin stock en ningún talle")
    print(f"Comparaciones realizadas: {comparaciones}")