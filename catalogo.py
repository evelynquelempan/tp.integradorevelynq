from prenda import Prenda

# ======================= LISTA DE PRENDAS =======================

prendas = [
    Prenda("P016", "Vestido lino", "Vestidos", "S", 28000, 3),      # <-- Raíz en el medio
    Prenda("P008", "Buzo oversize", "Buzos", "M", 38000, 5),
    Prenda("P025", "Top basico morley", "Tops", "S", 9500, 9),
    Prenda("P004", "Jean wide-leg", "Pantalones", "38", 30000, 5),
    Prenda("P012", "Campera de jean", "Camperas", "L", 45000, 3),
    Prenda("P020", "Camisa blanca", "Camisas", "M", 19500, 5),
    Prenda("P028", "Sweater lana", "Sweaters", "S", 37000, 2),
    Prenda("P001", "Remera basica blanca", "Remeras", "S", 8500, 10),
    Prenda("P002", "Remera basica negra", "Remeras", "M", 8500, 8),
    Prenda("P003", "Remera basica marron", "Remeras", "L", 8500, 6),
    Prenda("P005", "Jean recto", "Pantalones", "40", 30000, 7),
    Prenda("P006", "Jean mom", "Pantalones", "42", 25000, 4),
    Prenda("P007", "Buzo canguro", "Buzos", "S", 32000, 5),
    Prenda("P009", "Buzo premium", "Buzos", "L", 40000, 2),
    Prenda("P010", "Campera de jean", "Camperas", "S", 45000, 4),
    Prenda("P011", "Campera de jean", "Camperas", "M", 45000, 6),
    Prenda("P013", "Pollera de jean", "Polleras", "S", 18000, 5),
    Prenda("P014", "Pollera de jean", "Polleras", "M", 18000, 4),
    Prenda("P015", "Pollera de jean", "Polleras", "L", 18000, 2),
    Prenda("P017", "Vestido lino", "Vestidos", "M", 28000, 6),
    Prenda("P018", "Vestido lino", "Vestidos", "L", 28000, 5),
    Prenda("P019", "Camisa blanca", "Camisas", "S", 19500, 7),
    Prenda("P021", "Camisa blanca", "Camisas", "L", 19500, 3),
    Prenda("P022", "Short lino", "Shorts", "S", 15000, 8),
    Prenda("P023", "Short lino", "Shorts", "M", 15000, 6),
    Prenda("P024", "Short lino", "Shorts", "L", 15000, 4),
    Prenda("P026", "Top basico morley", "Tops", "M", 9500, 7),
    Prenda("P027", "Top basico morley", "Tops", "L", 9500, 5),
    Prenda("P029", "Sweater lana", "Sweaters", "M", 37000, 4),
    Prenda("P030", "Sweater lana", "Sweaters", "L", 37000, 3),
]



# ================= BUSCAR POR CODIGO =================

def buscar_por_codigo(prendas, cod_buscado):
    comparaciones = 0
    for prenda in prendas:
        comparaciones += 1
        if prenda.codigo.lower() == cod_buscado.lower():
            return prenda, comparaciones
    return None, comparaciones


# ================= BUSCAR POR NOMBRE =================

def buscar_por_nombre(prendas, nombre_buscado):
    encontradas = []
    comparaciones = 0
    for prenda in prendas:
        comparaciones += 1

        if nombre_buscado.lower() in prenda.nombre.lower():
            encontradas.append(prenda)
    return encontradas, comparaciones


# ================= INSERTAR PRENDA =================

def insertar_prenda(prendas, nueva_prenda):
    for prenda in prendas:
        if prenda.codigo.lower() == nueva_prenda.codigo.lower():
            print("Ya existe una prenda con ese código.")
            return False

    prendas.append(nueva_prenda)
    print("Prenda agregada correctamente.")
    return True


# ================= MODIFICAR PRENDA =================

def modificar_prenda(prendas, codigo_buscado):
    prenda, comparaciones = buscar_por_codigo(prendas, codigo_buscado)

    if prenda is None:
        print("No se encontró una prenda con ese código.")
        print(f"Comparaciones realizadas: {comparaciones}")
        return False

    print("Prenda encontrada:")
    print(prenda)

    try:
        nuevo_precio = float(input("Ingresá el nuevo precio: "))
        nuevo_stock = int(input("Ingresá el nuevo stock: "))

        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")

        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo")

        prenda.precio = nuevo_precio
        prenda.stock = nuevo_stock
        print("Prenda modificada correctamente.")
        return True

    except ValueError as error:
        print(f"Error: {error}")
        return False


# ================= ELIMINAR PRENDA =================

def eliminar_prenda(prendas, codigo_buscado):
    prenda, comparaciones = buscar_por_codigo(prendas, codigo_buscado)

    if prenda is None:
        print("No se encontró una prenda con ese código.")
        return False

    prendas.remove(prenda)
    print("Prenda eliminada correctamente.")
    print(f"Comparaciones realizadas: {comparaciones}")
    return True