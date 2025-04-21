from datetime import date, datetime
from library.categories.category import Category
from library.helpers.item_status import ItemStatus
from library.items.book import Book
from library.menu.author_menu import select_authors
from library.menu.category_menu import search_category, select_categories
from library.people.author import Author


def handle_books_management():
    while True:
        print("\n======= GESTIÓN DE LIBROS =======\n")
        print("1. Registrar libro")
        print("2. Buscar libro")
        print("3. Modificar libro")
        print("4. Inhabilitar libro")
        print("5. Volver al menú principal\n")

        try:
            option = int(input("Seleccione una opción: "))

            if option == 1:
                register_book()
            elif option == 2:
                search_book()
            elif option == 3:
                modify_book()
            elif option == 4:
                disable_book()
            elif option == 5:
                print("\nVolviendo al menú principal...")
                break
            else:
                print("\nOpción inválida. Por favor, intente nuevamente.")

        except ValueError:
            print("\nError: Por favor ingrese un número válido.")


def search_book():
    print("\n====== BÚSQUEDA DE LIBROS ======\n")
    print("1. Ver todos los libros")
    print("2. Buscar libro por ISBN")
    print("3. Volver\n")

    try:
        option = int(input("Seleccione una opción: "))

        if option == 1:
            # Mostrar todos los libros
            books = Book.get_books()
            if len(books) == 0:  # Verificamos si la lista de libros está vacía
                print("\nNo hay libros registrados en el sistema.")
                return

            print("\n=== LISTADO DE LIBROS ===\n")
            print("\nISBN | Título | Género | Estado")
            print("-" * 70)
            for book in books:
                print(
                    f"{book.ISBN} | {book.title} | {book.genre} | {book.status.value}"
                )
            print("-" * 70)

        elif option == 2:
            # Buscar por ISBN
            isbn = input("\nIngrese el ISBN del libro: ").strip()
            while not isbn:
                print("El ISBN no puede estar vacío.")
                isbn = input("Ingrese el ISBN del libro: ").strip()

            book = Book.get_book_by_ISBN(isbn)
            if book:
                print("\n=== LIBRO ENCONTRADO ===\n")
                print(book)
            else:
                print("\nNo se encontró ningún libro con ese ISBN.")

        elif option == 3:
            return
        else:
            print("\nOpción inválida. Por favor, intente nuevamente.")

    except ValueError:
        print("\nError: Por favor ingrese un número válido.")


def modify_book():
    print("\n====== MODIFICAR LIBRO ======\n")

    # Primero buscamos el libro por ISBN
    isbn = input("Ingrese el ISBN del libro a modificar: ").strip()
    while not isbn:
        print("El ISBN no puede estar vacío.")
        isbn = input("Ingrese el ISBN del libro a modificar: ").strip()

    book = Book.get_book_by_ISBN(isbn)
    if not book:
        print("\nNo se encontró ningún libro con ese ISBN.")
        return

    try:
        # Datos básicos del libro
        print("\nDeje en blanco los campos que no desea modificar\n")

        title = input(f"Título actual: {book.title}\nNuevo título: ").strip()
        genre = input(f"Género actual: {book.genre}\nNuevo género: ").strip()
        edition = input(f"Edición actual: {book.edition}\nNueva edición: ").strip()

        # Fecha de publicación
        publication_date = book.publication_date
        publication_date_str = input(
            f"Nueva fecha de nacimiento ({book.publication_date}) [DD-MM-YYYY]: "
        ).strip()
        if publication_date_str:
            try:
                publication_date = datetime.strptime(
                    publication_date_str, "%d-%m-%Y"
                ).date()
            except ValueError:
                print("Formato de fecha inválido. No se actualizará la fecha.")

        publisher = input(
            f"Editorial actual: {book.publisher}\nNueva editorial: "
        ).strip()

        language = input(f"Idioma actual: {book.language}\nNuevo idioma: ").strip()

        # Lista de autores
        authors = select_authors()

        while not authors:
            print("\nDebe ingresar al menos un autor.")
            authors = select_authors()

        # Categorías
        categories = select_categories()

        # Estado
        status: ItemStatus = ItemStatus.AVAILABLE
        modify_status = input("\n¿Desea modificar el estado del libro? (s/n): ").lower()
        if modify_status == "s":
            print("\nEstados disponibles:")
            for i, status_option in enumerate(ItemStatus):
                print(f"{i+1}. {status_option.value}")

            while True:
                try:
                    status_option = int(input("\nSeleccione el nuevo estado: ")) - 1
                    if 0 <= status_option < len(ItemStatus):
                        status = list(ItemStatus)[status_option]
                        break
                    print("Opción inválida.")
                except ValueError:
                    print("Por favor ingrese un número válido.")

        # Actualizamos el libro
        book.update_book(
            new_title=title,
            new_genre=genre,
            new_edition=edition,
            new_publication_date=publication_date,
            new_publisher=publisher,
            new_authors=authors,
            new_language=language,
            new_status=status,
            new_categories=categories,
        )

        print("\n¡Libro modificado exitosamente!")
        print("\nDatos actualizados del libro:")
        print("-" * 50)
        print(book)

    except Exception as e:
        print(f"\nError al modificar el libro: {str(e)}")


def disable_book():
    print("\nInhabilitar libro - En desarrollo...")


def register_book():
    print("\n====== REGISTRO DE LIBRO ======\n")
    try:
        # Datos básicos del libro
        title = input("Ingrese el título del libro: ").strip()
        while not title:
            print("El título no puede estar vacío.")
            title = input("Ingrese el título del libro: ").strip()

        genre = input("Ingrese el género del libro: ").strip()
        while not genre:
            print("El género no puede estar vacío.")
            genre = input("Ingrese el género del libro: ").strip()

        edition = input("Ingrese la edición del libro: ").strip()
        while not edition:
            print("La edición no puede estar vacía.")
            edition = input("Ingrese la edición del libro: ").strip()

        # Fecha de publicación
        while True:
            try:
                date_str = input(
                    "Ingrese la fecha de publicación (DD-MM-YYYY): "
                ).strip()
                publication_date = datetime.strptime(date_str, "%d-%m-%Y").date()
                break
            except ValueError:
                print(
                    "Fecha inválida. Por favor, ingrese la fecha en formato DD-MM-YYYY"
                )

        publisher = input("Ingrese la editorial: ").strip()
        while not publisher:
            print("La editorial no puede estar vacía.")
            publisher = input("Ingrese la editorial: ").strip()

        # Lista de autores
        authors = select_authors()

        ISBN = input("Ingrese el ISBN del libro: ").strip()
        while not ISBN:
            print("El ISBN no puede estar vacío.")
            ISBN = input("Ingrese el ISBN del libro: ").strip()

        language = input("Ingrese el idioma del libro: ").strip()
        while not language:
            print("El idioma no puede estar vacío.")
            language = input("Ingrese el idioma del libro: ").strip()

        # Estado por defecto al registrar
        status = ItemStatus.AVAILABLE

        categories = select_categories()

        # Registramos el libro
        if Book.register(
            genre=genre,
            title=title,
            edition=edition,
            publication_date=publication_date,
            publisher=publisher,
            authors=authors,
            ISBN=ISBN,
            language=language,
            status=status,
            categories=categories,
        ):
            print("\n¡Libro registrado exitosamente!")
        else:
            print("\nError: El ISBN ya existe en el sistema.")

    except Exception as e:
        print(f"\nError al registrar el libro: {str(e)}")
