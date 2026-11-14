# Grupo 9 - TP INTEGRADOR DE ESTRUCTURAS DE DATOS: Tienda de Ropa. 


## Descripción

Sistema de consola desarrollado para gestionar el catálogo y el stock de una tienda de ropa.

Este proyecto corresponde al Trabajo Práctico Integrador de la materia **Estructuras de Datos**, de la Tecnicatura Universitaria.

El sistema permite administrar las prendas del catálogo, realizar búsquedas, explorar categorías, consultar talles disponibles y gestionar usuarios con diferentes permisos de acceso.

## Integrantes

- Evelyn Quelempan
- Ulises Palacios
- Ricardo Estrada
- Marilyn Tufillaro

## Estructuras de datos y funcionalidades implementadas

El proyecto implementa las siguientes estructuras de datos y conceptos:

- **Programación Orientada a Objetos y Encapsulamiento:** clase `Prenda`, con atributos privados, propiedades `@property` y validaciones.
- **Lista:** catálogo de prendas con 30 registros iniciales y operaciones de inserción, búsqueda secuencial por código y nombre, modificación y eliminación.
- **Árbol General (N-ario):** organización jerárquica de categorías que permite explorar el catálogo por niveles.
- **Árbol Binario de Búsqueda (BST):** permite insertar y buscar prendas por código, además de listar los elementos ordenados mediante recorrido inorden.
- **Cola (FIFO):** historial de las últimas 5 búsquedas realizadas. Al superar esa capacidad, se elimina la búsqueda más antigua.
- **Persistencia en JSON:** carga automática de los datos al iniciar el programa y guardado de los cambios realizados en el catálogo.

### Funcionalidades del sistema

**Administrador:**
- Listar prendas.
- Explorar por categorías.
- Listar prendas ordenadas por código.
- Buscar prendas por código o nombre.
- Insertar nuevas prendas.
- Modificar prendas existentes.
- Eliminar prendas.
- Comparar la cantidad de comparaciones entre la búsqueda en lista y en árbol.
- Consultar talles disponibles.
- Consultar el historial de búsquedas.

**Cliente:**
- Explorar el catálogo por categorías.
- Consultar todas las prendas, sus precios y stock.
- Buscar prendas por código o nombre.
- Consultar talles disponibles.

## Estructura del proyecto

```text
tp integrador/
│
├── main.py
│
├── datos/
│   ├── __init__.py
│   ├── catalogo.py
│   └── datos.json
│
├── estructuras/
│   ├── __init__.py
│   ├── arbol_busqueda.py
│   └── arbol_categorias.py
│
├── modelos/
│   ├── __init__.py
│   ├── prenda.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── autenticacion.py
│   └── persistencia.py
│
├── ui/
│   ├── __init__.py
│   ├── busquedas_ui.py
│   ├── menu_admin.py
│   └── menu_cliente.py
│
├── .gitignore
└── README.md
```

## Cómo ejecutar el proyecto

### 1. Requisitos previos

- Tener Python instalado.
- Tener Git instalado (opcional, si se desea clonar el repositorio).

### 2. Descargar el proyecto

Clonar el repositorio desde una terminal:

```bash
git clone https://github.com/evelynquelempan/tp.integradorevelynq.git
```

### 3. Abrir la carpeta del proyecto

Ingresar a la carpeta principal del proyecto:

```bash
cd tp.integradorevelynq
```

Abrirla con Visual Studio Code o utilizar la terminal desde esa ubicación.

### 4. Ejecutar el programa

Desde la carpeta principal, ejecutar:

```bash
python main.py
```

En algunos equipos puede ser necesario utilizar:

```bash
py main.py
```

### 5. Iniciar sesión

El sistema cuenta con dos usuarios de prueba:

| Usuario | Contraseña | Rol |
|---|---|---|
| admin | admin123 | Administrador |
| cliente | cliente123 | Cliente |

Según el rol seleccionado, se mostrará el menú correspondiente.

## Persistencia de datos

Los datos del catálogo se almacenan en el archivo `datos/datos.json`.

Al iniciar el programa, se cargan los datos guardados. Cada vez que el administrador realiza una operación que modifica el catálogo, los cambios se guardan automáticamente para conservarlos entre ejecuciones.

---

**Trabajo Práctico Integrador - Estructuras de Datos**  
**Grupo 9**

