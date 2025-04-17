# Este script crea una serie de categorías, autores y artículos para pruebas.
from datetime import date

from library.items.article import Article
from library.helpers.status import Status
from library.categories.category import Category
from library.people.author import Author

# Creación de categorías principales
Category.create_category(
    "Ciencia", "Campos relacionados con la investigación científica"
)
Category.create_category("Tecnología", "Campos relacionados con avances tecnológicos")
Category.create_category(
    "Humanidades", "Campos relacionados con el estudio del ser humano"
)

# Obtenemos las categorías principales
ciencia = Category.get_category_by_id(1)  # Ciencia será el ID 1
tecnologia = Category.get_category_by_id(2)  # Tecnología será el ID 2
humanidades = Category.get_category_by_id(3)  # Humanidades será el ID 3

if any(cat is None for cat in [ciencia, tecnologia, humanidades]):
    raise ValueError("Error al obtener las categorías principales")

# Creación de subcategorías
Category.create_category(
    "Computación", "Ciencias de la computación", parent_id=tecnologia.id
)
computacion = Category.get_category_by_id(4)

Category.create_category(
    "Inteligencia Artificial", "Estudio de la IA", parent_id=computacion.id
)
Category.create_category(
    "Física", "Estudio de la materia y energía", parent_id=ciencia.id
)
Category.create_category(
    "Química", "Estudio de la composición de la materia", parent_id=ciencia.id
)
Category.create_category(
    "Filosofía", "Estudio del conocimiento y la existencia", parent_id=humanidades.id
)

# Obtenemos las subcategorías
ia = Category.get_category_by_id(5)
fisica = Category.get_category_by_id(6)
quimica = Category.get_category_by_id(7)
filosofia = Category.get_category_by_id(8)

if any(cat is None for cat in [computacion, ia, fisica, quimica, filosofia]):
    raise ValueError("Error al obtener las subcategorías")

# Creación de autores notables
Author.create(
    author_id="TUR001",
    name="Alan Turing",
    nationality="UK",
    birth_date=date(1912, 6, 23),
)

Author.create(
    author_id="CUR001",
    name="Marie Curie",
    nationality="Francia",
    birth_date=date(1867, 11, 7),
)

Author.create(
    author_id="ARI001",
    name="Aristóteles",
    nationality="Grecia",
    birth_date=date(384, 1, 1),
)

Author.create(
    author_id="LOV001",
    name="Ada Lovelace",
    nationality="UK",
    birth_date=date(1815, 12, 10),
)

# Creación de artículos
# Obtenemos los objetos Author usando sus IDs
turing_author = Author.get_author_by_id("TUR001")
curie_author = Author.get_author_by_id("CUR001")
aristotle_author = Author.get_author_by_id("ARI001")

# Verificamos que los autores se hayan obtenido correctamente
if turing_author is None:
    raise ValueError("No se pudo encontrar el autor Alan Turing (TUR001)")
if curie_author is None:
    raise ValueError("No se pudo encontrar el autor Marie Curie (CUR001)")
if aristotle_author is None:
    raise ValueError("No se pudo encontrar el autor Aristóteles (ARI001)") 

Article.create(
    doi="10.1234/computing.1950.123",
    title="Computing Machinery and Intelligence",
    publisher_name="Mind Journal",
    publication_date=date(1950, 10, 1),
    journal="Mind",
    periodicity="Trimestral",
    volume="LIX",
    field="Computación",
    status=Status.AVAILABLE,
    authors=[turing_author],
    categories=[computacion, ia, filosofia],
)

Article.create(
    doi="10.1234/radium.1898.456",
    title="Sur une nouvelle substance fortement radio-active",
    publisher_name="French Academy of Sciences",
    publication_date=date(1898, 12, 26),
    journal="Comptes rendus de l'Académie des Sciences",
    periodicity="Semanal",
    volume="127",
    field="Química",
    status=Status.AVAILABLE,
    authors=[curie_author, aristotle_author],
    categories=[ciencia, quimica],
)

print("Categorías y autores creados con éxito.")
