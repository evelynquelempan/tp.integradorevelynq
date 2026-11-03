from collections import deque


class HistorialBusquedas:
    def __init__(self, maximo=5):
        self._cola = deque()
        self._maximo = maximo

    def registrar(self, tipo, termino):
        if len(self._cola) == self._maximo:
            self._cola.popleft()  # descarta la búsqueda más vieja
        self._cola.append(f"{tipo}: {termino}")

    def mostrar(self):
        if not self._cola:
            print("Todavía no hay búsquedas registradas.")
            return
        print(f"\n--- ÚLTIMAS {len(self._cola)} BÚSQUEDAS ---")
        for i, busqueda in enumerate(reversed(self._cola), start=1):
            print(f"{i}. {busqueda}")