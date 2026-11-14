
# Clase que representa cada nodo del árbol binario de búsqueda
class NodoBST:

    # Constructor: recibe la clave y el elemento que se van a guardar
    def __init__(self, clave, elemento):
        self.clave = clave          # Código de la prenda, utilizado para ordenar
        self.elemento = elemento    # Objeto completo de tipo Prenda
        self.izquierda = None       # Referencia al hijo izquierdo
        self.derecha = None         # Referencia al hijo derecho

    # Método para insertar un nuevo nodo en el árbol
    def insertar(self, clave, elemento):

        # Si la clave nueva es menor que la del nodo actual
        if clave < self.clave:

            # Si el lugar izquierdo está vacío, creamos el nuevo nodo
            if self.izquierda is None:
                self.izquierda = NodoBST(clave, elemento)

            # Si está ocupado, seguimos buscando lugar por la izquierda
            else:
                self.izquierda.insertar(clave, elemento)

        # Si la clave nueva es mayor que la del nodo actual
        elif clave > self.clave:

            # Si el lugar derecho está vacío, creamos el nuevo nodo
            if self.derecha is None:
                self.derecha = NodoBST(clave, elemento)

            # Si está ocupado, seguimos buscando lugar por la derecha
            else:
                self.derecha.insertar(clave, elemento)

        # Si la clave ya existe, no agregamos otro nodo
        else:
            return

    # Método para buscar una prenda por su código
    def buscar(self, clave, comparaciones=0):

        # Contamos la comparación con el nodo actual
        comparaciones += 1

        # Si encontramos el código, devolvemos la prenda y las comparaciones
        if clave == self.clave:
            return self.elemento, comparaciones

        # Si el código buscado es menor, buscamos por la izquierda
        elif clave < self.clave:
            if self.izquierda is not None:
                return self.izquierda.buscar(clave, comparaciones)

        # Si el código buscado es mayor, buscamos por la derecha
        elif clave > self.clave:
            if self.derecha is not None:
                return self.derecha.buscar(clave, comparaciones)

        # Si no encontramos la prenda, devolvemos None
        return None, comparaciones


# Clase que representa y administra el árbol completo
class ArbolBusqueda:

    # Constructor del árbol
    def __init__(self):
        self.raiz = None  # La raíz comienza vacía

    # Método para insertar una prenda en el árbol
    def insertar(self, elemento):

        # Obtenemos el código de la prenda para utilizarlo como clave
        clave = elemento.codigo

        # Si el árbol está vacío, la prenda se convierte en la raíz
        if self.raiz is None:
            self.raiz = NodoBST(clave, elemento)

        # Si ya existe una raíz, llamamos al método insertar del nodo
        else:
            self.raiz.insertar(clave, elemento)

    # Método para iniciar la búsqueda desde la raíz
    def buscar(self, clave):

        # Si el árbol está vacío, no hay elementos para buscar
        if self.raiz is None:
            return None, 0

        # Iniciamos la búsqueda desde la raíz
        return self.raiz.buscar(clave.upper())

    # Método que devuelve las prendas ordenadas por código
    def inorden(self):

        # Creamos una lista vacía para guardar los resultados
        resultado = []

        # Iniciamos el recorrido desde la raíz
        self._recorrer_inorden(self.raiz, resultado)

        # Devolvemos la lista ordenada
        return resultado

    # Método interno que realiza el recorrido inorden
    def _recorrer_inorden(self, nodo, resultado):

        # Si el nodo existe, continuamos con el recorrido
        if nodo is not None:

            # Primero recorremos el subárbol izquierdo
            self._recorrer_inorden(nodo.izquierda, resultado)

            # Después agregamos el elemento del nodo actual
            resultado.append(nodo.elemento)

            # Finalmente recorremos el subárbol derecho
            self._recorrer_inorden(nodo.derecha, resultado)
