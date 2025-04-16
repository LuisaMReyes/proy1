# 📚 Sistema de Gestión de Biblioteca

Este proyecto consiste en el desarrollo de un sistema de información para la gestión de una biblioteca, implementado en Python usando el paradigma de Programación Orientada a Objetos (POO). Es un trabajo académico desarrollado para el curso de Programación IV – Programación Orientada a Objetos, de la Universidad Tecnológica de Pereira.

---

## 🧩 Descripción General

El sistema permite administrar los distintos productos bibliográficos de una biblioteca (libros, tesis, artículos científicos), así como la información relacionada con lectores, autores, préstamos, multas, copias de libros y categorías temáticas.

Se ha desarrollado bajo los siguientes principios:

- Uso de clases organizadas en módulos independientes dentro de un paquete.
- Relaciones simples entre clases (sin herencia ni composición compleja).
- Organización modular para garantizar claridad y mantenibilidad del código.

---

## 🗂️ Funcionalidades principales

### Productos bibliográficos
- Registrar, buscar, modificar y eliminar tesis y artículos científicos.
- Registrar, buscar y modificar libros (no se eliminan, solo se inhabilitan).
- Asignación de categorías a todos los productos.

### Libros y copias
- Control de copias físicas de libros con estados (prestada, en biblioteca, en reparación, etc.).
- Registro automático de al menos una copia al registrar un libro.

### Categorías
- Gestión de categorías y subcategorías con nombre, ID y descripción.
- Búsqueda, creación, modificación y eliminación de categorías.

### Autores
- Registro y actualización de autores.
- Asociación de uno o varios autores por libro.
- Creación automática si no existen al registrar un libro.

### Lectores
- Registro, modificación, búsqueda, habilitación e inhabilitación.
- Control de estado del lector (normal, sancionado, suspendido, inactivo).
- Consulta de préstamos activos y multas asociadas.

### Préstamos
- Registro de préstamos de copias (libros, artículos o tesis).
- Cálculo de fechas de entrega.
- Cancelación o finalización de préstamos.
- Límite de hasta 3 préstamos simultáneos por lector.

### Multas
- Cálculo automático por retraso en entrega.
- Asociación 1:1 con préstamo.
- Control de estado (activa/inactiva) y tiempo de sanción.

---

## 🧑‍💻 Integrantes del equipo

- **Cristhian Giraldo** - 1092455532
- **Luisa Reyes** - 
