import json
import os
from prenda import Prenda
ARCHIVO_DATOS = "datos.json"
def guardar_prendas(prendas, ruta=ARCHIVO_DATOS):
    datos = []
    for p in prendas:
        datos.append({
            "codigo": p.codigo,
            "nombre": p.nombre,
            "categoria": p.categoria,
            "talle": p.talle,
            "precio": p.precio,
            "stock": p.stock
        })
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar los datos en {ruta}: {e}")
        return False
def cargar_prendas(ruta=ARCHIVO_DATOS, prendas_iniciales=None):
    if not os.path.exists(ruta):
        if prendas_iniciales:
            print(f"Archivo '{ruta}' no encontrado. Creándolo con los datos iniciales...")
            guardar_prendas(prendas_iniciales, ruta)
            return list(prendas_iniciales)
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        prendas_reconstruidas = []
        for item in datos:
            prenda = Prenda(
                codigo=item["codigo"],
                nombre=item["nombre"],
                categoria=item["categoria"],
                talle=item["talle"],
                precio=float(item["precio"]),
                stock=int(item["stock"])
            )
            prendas_reconstruidas.append(prenda)
        return prendas_reconstruidas
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        print(f"Error al leer '{ruta}': {e}")
        return list(prendas_iniciales) if prendas_iniciales else []