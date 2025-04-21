from datetime import date
from library.items.book import Book


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
            if not Book._books:  # Accedemos a la lista interna de libros
                print("\nNo hay libros registrados en el sistema.")
                return

            print("\n=== LISTADO DE LIBROS ===\n")
            Book.get_books()

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

    print("\nLibro encontrado:")
    print("-" * 50)
    print(book)
    print("-" * 50)

    try:
        # Datos básicos del libro
        print("\nDeje en blanco los campos que no desea modificar\n")

        title = input(f"Título actual: {book.title}\nNuevo título: ").strip()
        genre = input(f"Género actual: {book.genre}\nNuevo género: ").strip()
        edition = input(f"Edición actual: {book.edition}\nNueva edición: ").strip()

        # Fecha de publicación
        publication_date = None
        modify_date = input(
            f"Fecha de publicación actual: {book.publication_date.strftime('%d/%m/%Y')}\n¿Desea modificar la fecha? (s/n): "
        ).lower()
        if modify_date == "s":
            while True:
                try:
                    year = int(input("Ingrese el nuevo año de publicación (YYYY): "))
                    month = int(input("Ingrese el nuevo mes de publicación (1-12): "))
                    day = int(input("Ingrese el nuevo día de publicación (1-31): "))
                    publication_date = date(year, month, day)
                    break
                except ValueError:
                    print("Fecha inválida. Por favor, intente nuevamente.")

        publisher = input(
            f"Editorial actual: {book.publisher}\nNueva editorial: "
        ).strip()
        language = input(f"Idioma actual: {book.language}\nNuevo idioma: ").strip()

        # Lista de autores
        authors = None
        modify_authors = input("\n¿Desea modificar los autores? (s/n): ").lower()
        if modify_authors == "s":
            authors = []
            while True:
                author_name = input(
                    "Ingrese el nombre del autor (o presione Enter para terminar): "
                ).strip()
                if not author_name:
                    if not authors:
                        print("Debe ingresar al menos un autor.")
                        continue
                    break
                authors.append(Author(author_name))

        # Categorías
        categories = None
        modify_categories = input("\n¿Desea modificar las categorías? (s/n): ").lower()
        if modify_categories == "s":
            categories = []
            while True:
                category_name = input(
                    "Ingrese una categoría (o presione Enter para terminar): "
                ).strip()
                if not category_name:
                    break
                categories.append(Category(category_name))

        # Estado
        status = None
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
                year = int(input("Ingrese el año de publicación (YYYY): "))
                month = int(input("Ingrese el mes de publicación (1-12): "))
                day = int(input("Ingrese el día de publicación (1-31): "))
                publication_date = date(year, month, day)
                break
            except ValueError:
                print("Fecha inválida. Por favor, intente nuevamente.")

        publisher = input("Ingrese la editorial: ").strip()
        while not publisher:
            print("La editorial no puede estar vacía.")
            publisher = input("Ingrese la editorial: ").strip()

        # Lista de autores
        authors = []
        while True:
            author_name = input(
                "Ingrese el nombre del autor (o presione Enter para terminar): "
            ).strip()
            if not author_name:
                if not authors:
                    print("Debe ingresar al menos un autor.")
                    continue
                break
            # TODO: Implementar autor
            authors.append(Author(author_name))

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

        # TODO: Implementar categories
        # Categorías (opcional)
        categories = []
        while True:
            category_name = input(
                "Ingrese una categoría (o presione Enter para terminar): "
            ).strip()
            if not category_name:
                break
            categories.append(Category(category_name))

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
