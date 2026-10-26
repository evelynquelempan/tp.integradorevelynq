class Prenda:
    def __init__(self, codigo, nombre, categoria, talle, precio, stock):
        if not codigo or not codigo.strip():
            raise ValueError("El código no puede estar vacío")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not categoria or not categoria.strip():
            raise ValueError("La categoría no puede estar vacía")
        if not talle or not talle.strip():
            raise ValueError("El talle no puede estar vacío")

        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._talle = talle
        self.precio = precio
        self.stock = stock

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def talle(self):
        return self._talle

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = nuevo_precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock):
        if not isinstance(nuevo_stock, int) or isinstance(nuevo_stock, bool):
            raise ValueError("El stock debe ser un número entero")
        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = nuevo_stock

    def disponible(self):
        return self._stock > 0

    def __str__(self):
        return (
            f"Código: {self._codigo} | "
            f"Prenda: {self._nombre} | "
            f"Categoría: {self._categoria} | "
            f"Talle: {self._talle} | "
            f"Precio: ${self._precio} | "
            f"Stock: {self._stock}"
        )