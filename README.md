# Grupo 9 - TP INTEGRADOR DE ESTRUCTURAS DE DATOS: Tienda de Ropa. 

## Descripción

Sistema de consola para gestionar un catálogo y stock de una tienda de ropa. 
Desarrollado como Trabajo Práctico de la materia **Estructuras de Datos** de la Tecnicatura Universitaria.

## Integrantes

| Evelyn Quelempan      |
| Ulises Palacios       | 
| Ricardo Estrada       | 
| Marilyn Tufillaro     | 


El programa implementa **desde cero** las siguientes estructuras de datos:
 - Modelo de Dominio con POO y Encapsulamiento: Clase **Prenda** con atributos privados, propiedades **@property** y validaciones de tipos y rangos.
 - Estructura Lineal (Lista): Catálogo base con 30 prendas de prueba iniciales y operaciones de inserción, búsqueda secuencial por código y nombre con conteo de comparaciones, modificación y eliminación. 
 - Árbol General (n-ario): Jerarquía de categorías (Indumentaria → Temporada → Tipo de prenda) implementado con 
 **NodoCategoria** para explorar el catálogo por niveles de navegación.
 - Árbol Binario de Búsqueda (BST): Implementado con NodoBST para búsqueda eficiente por código de prenda  y recorrido Inorden para listar los elementos ordenados automáticamente.
 - Cola (FIFO): Historial de las últimas búsquedas del usuario con capacidad máxima declarada , descartando la más antigua.
 - Persistencia en JSON: Carga y guardado automático del catálogo completo en datos.json al iniciar y tras cada modificación.
 - Funcionalidad propia del tema: Consulta de talles disponibles con stock agrupados por prenda.

## Estructura del proyecto 

├── main.py               # Menú principal y orquestación del sistema
├── prenda.py             # Clase Prenda con encapsulamiento y setters validados
├── catalogo.py           # Datos iniciales (30 prendas) y operaciones CRUD en lista
├── arbol_busqueda.py     # Árbol Binario de Búsqueda (BST) y recorrido inorden
├── arbol_categorias.py   # Árbol General (N-ario) para navegación por categorías
├── persistencia.py       # Carga y guardado en archivo datos.json
├── busquedas_ui.py       # Consulta de talles disponibles y búsquedas auxiliares
├── usuario.py            # Clase Usuario con roles (administrador / cliente)
├── autenticacion.py      # Módulo de login y validación de credenciales
├── menu_cliente.py       # Menú con permisos de solo lectura para clientes
├── datos.json            # Base de datos persistente en formato JSON
├── .gitignore            # Archivos ignorados por Git (__pycache__, temporales)
└── README.md             # Documentación del proyecto

## Cómo ejecutar

```bash
# Desde la carpeta tp.integradorevelynq

python main.py
```