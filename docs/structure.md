---

## 🗂️ Estructura del Proyecto – Sistema de Gestión de Biblioteca

Este documento describe la organización de carpetas y archivos del proyecto, con el fin de facilitar su comprensión, mantenimiento y escalabilidad.

---

## 📁 Estructura general

```
LibrarySystem/
├── docs/
│   └── structure.md
├── main.py
├── README.md
└── library/
    ├── items/
    │   ├── book.py
    │   ├── thesis.py
    │   └── article.py
    ├── people/
    │   ├── author.py
    │   └── reader.py
    ├── loans/
    │   ├── loan.py
    │
    ├── fines/
    |   ├── fine.py   
    | 
    ├── copies/
    │   └── copies.py
    ├── categories/
    │   └── category.py
    └── helpers/
        ├── error.py
        ├── reader_status.py
        ├── item_status.py
        ├── fine_status.py
        ├── copy_status.py
        └── item_type.py

```

---

## 🧩 Descripción de carpetas y archivos

### `main.py`

Archivo principal del sistema. Se encarga de importar las clases necesarias desde el paquete `library/` y gestionar la ejecución del programa.
---

## 📦 Paquete principal: `library/`

Este paquete agrupa todas las clases y funcionalidades del sistema, distribuidas en subpaquetes temáticos para mejorar la legibilidad.

### `items/`Módulo que maneja los productos de la biblioteca: Libros, Tesis y Artículos.
        ###`items/article`

### `people/`Módulo que gestiona la información de autores y lectores.

### `loans/`Módulo que administra los préstamos de copias.

### `fines/`Módulo que gestiona las multas.

### `copies/`Módulo para registrar, buscar y gestionar las copias de los libros.

### `categories/`Módulo de categorías temáticas para clasificar productos.

### `helpers/` Módulo auxiliar que define tipos enumerados (estados, errores, tipos de productos), control de errores, y estados.

