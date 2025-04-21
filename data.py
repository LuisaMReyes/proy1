from datetime import date
from library.people.author import Author
from library.categories.category import Category

def load_initial_data():
    # Crear categorías
    Category.create_category(
        name="Ficción",
        description="Libros de ficción, incluyendo novelas y cuentos"
    )
    
    Category.create_category(
        name="No Ficción",
        description="Libros basados en hechos reales y conocimiento"
    )

    # Crear autores
    Author.create(
        author_id="AU001",
        name="Jorge Luis Borges",
        nationality="Argentina",
        birth_date=date(1899, 8, 24)
    )

    Author.create(
        author_id="AU002",
        name="Gabriel García Márquez",
        nationality="Colombia",
        birth_date=date(1927, 3, 6)
    )

    Author.create(
        author_id="AU003",
        name="Isabel Allende",
        nationality="Chile",
        birth_date=date(1942, 8, 2)
    )
