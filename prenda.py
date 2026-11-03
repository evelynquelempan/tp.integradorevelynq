
class Prenda:
    def __init__(self, codigo, nombre, categoria, talle, precio, stock):

        # Validaciones de los datos de texto
        if not isinstance(codigo, str) or not codigo.strip(): 
            raise ValueError("El código no puede estar vacío")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if not isinstance(categoria, str) or not categoria.strip():
            raise ValueError("La categoría no puede estar vacía")

        if not isinstance(talle, str) or not talle.strip():
            raise ValueError("El talle no puede estar vacío")

        # Atributos encapsulados
        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._talle = talle
        self.precio = precio
        self.stock = stock


#Property permite definir métodos que se comportan como atributos, 
# lo que permite controlar el acceso a los datos y aplicar validaciones al establecer valores. 
    # Propiedad código
    @property
    def codigo(self):
        return self._codigo

    # Propiedad nombre
    @property
    def nombre(self):
        return self._nombre

    # Propiedad categoría
    @property
    def categoria(self):
        return self._categoria

    # Propiedad talle
    @property
    def talle(self):
        return self._talle

    # Propiedad precio
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if isinstance(nuevo_precio, bool) or not isinstance(nuevo_precio, (int, float)):
            raise ValueError("El precio debe ser un número")

        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")

        self._precio = nuevo_precio

    # Propiedad stock
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock):
        if isinstance(nuevo_stock, bool) or not isinstance(nuevo_stock, int):
            raise ValueError("El stock debe ser un número entero")

        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo")

        self._stock = nuevo_stock

    # Indica si la prenda tiene stock disponible
    def disponible(self):
        return self._stock > 0

    # Representación de la prenda para mostrar en consola
    def __str__(self):
        return (
            f"Código: {self._codigo} | "
            f"Prenda: {self._nombre} | "
            f"Categoría: {self._categoria} | "
            f"Talle: {self._talle} | "
            f"Precio: ${self._precio} | "
            f"Stock: {self._stock}"
        )
