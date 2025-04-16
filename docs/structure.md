---

## 🗂️ Estructura del Proyecto – Sistema de Gestión de Biblioteca

Este documento describe la organización de carpetas y archivos del proyecto, con el fin de facilitar su comprensión, mantenimiento y escalabilidad.

---

## 📁 Estructura general

```
LibrarySystem/
└── docs/
    └── strucure.md
├── main.py
├── README.md
└── library/
    ├── items/
    ├── people/
    ├── loans/
    ├── copies/
    ├── categories/
    └── utils/
```

---

## 🧩 Descripción de carpetas y archivos

### `main.py`

Archivo principal del sistema. Se encarga de importar las clases necesarias desde el paquete `library/` y gestionar la ejecución del programa.
---

## 📦 Paquete principal: `library/`

Este paquete agrupa todas las clases y funcionalidades del sistema, distribuidas en subpaquetes temáticos para mejorar la legibilidad.

### `items/`

### `people/`

### `loans/`

### `copies/`

### `categories/`
