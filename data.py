from datetime import date
from library.fines.fine import Fine
from library.helpers.item_status import ItemStatus
from library.helpers.item_type import ProductType
from library.items.book import Book
from library.loans.loan import Loan
from library.people.author import Author
from library.categories.category import Category


def load_initial_data():
    # Crear categorías
    Category.create_category(
        name="Ficción", description="Libros de ficción, incluyendo novelas y cuentos"
    )

    Category.create_category(
        name="No Ficción", description="Libros basados en hechos reales y conocimiento"
    )

    # Crear autores
    Author.create(
        author_id="AU001",
        name="Jorge Luis Borges",
        nationality="Argentina",
        birth_date=date(1899, 8, 24),
    )

    Author.create(
        author_id="AU002",
        name="Gabriel García Márquez",
        nationality="Colombia",
        birth_date=date(1927, 3, 6),
    )

    Author.create(
        author_id="AU003",
        name="Isabel Allende",
        nationality="Chile",
        birth_date=date(1942, 8, 2),
    )

    gabriel = Author.get_author_by_id("AU002")

    # Crear libros
    Book.register(
        isbn="978-3-16-148410-0",
        title="Cien años de soledad",
        genre="Realismo mágico",
        edition="Primera edición",
        publication_date=date(1967, 5, 30),
        publisher="Editorial Sudamericana",
        authors=[gabriel],
        language="Español",
        status=ItemStatus.AVAILABLE,
    )

    Loan.register(
        loan_id="LN001",
        product_type=ProductType.BOOK,
        product_id="978-3-16-148410-0",
        reader_id="RE001",
        days=14,
        loan_date=date(2023, 10, 1),
    )

    # loan = Loan.get_by_id("LN001")
    #
    # Fine.generate_fine(loan, date(2023, 10, 20))
