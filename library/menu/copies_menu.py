from datetime import datetime
from library.copies.copies import Copies
from library.helpers.copy_status import Copy_status
from library.items.book import Book


def find_book_by_isbn(show_all_option=True):
    """
    Función auxiliar para buscar un libro por isbn con la opción de mostrar todos los libros.

    Args:
        show_all_option (bool): Si es True, muestra la opción de listar todos los libros

    Returns:
        Book or None: Retorna el libro encontrado o None si no se encuentra o se cancela
    """
    if show_all_option:
        print("\n1. Ver listado de libros")
        print("2. Buscar por isbn")
        print("3. Volver\n")

        try:
            option = int(input("Seleccione una opción: "))

            if option == 1:
                print("\n====== LISTADO DE LIBROS ======\n")
                books = Book.get_books()
                if not books:
                    print("No hay libros registrados en el sistema.")
                    return None

                print("\nLibros disponibles:")
                print("-" * 50)
                for book in books:
                    print(f"isbn: {book.isbn}")
                    print(f"Título: {book.title}")
                    print("-" * 50)

                isbn = input("\nIngrese el isbn del libro deseado: ").strip()

            elif option == 2:
                isbn = input("\nIngrese el isbn del libro: ").strip()

            elif option == 3:
                return None

            else:
                print("\nOpción inválida.")
                return None

        except ValueError:
            print("\nError: Por favor ingrese un número válido.")
            return None
    else:
        isbn = input("\nIngrese el isbn del libro: ").strip()

    while not isbn:
        print("El isbn no puede estar vacío.")
        isbn = input("Ingrese el isbn del libro: ").strip()

    book = Book.get_book_by_isbn(isbn)
    if not book:
        print("\nNo se encontró ningún libro con ese isbn.")
        return None

    return book


def handle_copies_management():
    while True:
        print("\n======= GESTIÓN DE COPIAS DE LIBROS =======\n")
        print("1. Registrar copia de libro")
        print("2. Consultar copia")
        print("3. Eliminar copia")
        print("4. Volver al menú principal\n")

        try:
            option = int(input("Seleccione una opción: "))

            if option == 1:
                register_copy()
            elif option == 2:
                search_copy()
            elif option == 3:
                delete_copy()
            elif option == 4:
                print("\nVolviendo al menú principal...")
                break
            else:
                print("\nOpción inválida. Por favor, intente nuevamente.")

        except ValueError:
            print("\nError: Por favor ingrese un número válido.")


def register_copy():
    print("\n====== REGISTRO DE COPIA ======\n")
    try:
        # Buscamos el libro
        book = find_book_by_isbn()
        if not book:

            return

        print("\nLibro encontrado:")
        print(book)

        # Datos de la copia
        copy_code = input("\nIngrese el código de la copia: ").strip()
        while not copy_code:
            print("El código de la copia no puede estar vacío.")
            copy_code = input("Ingrese el código de la copia: ").strip()

        # Por defecto, una copia nueva se registra como disponible
        status = Copy_status.IN_LIBRARY

        # Registramos la copia
        if Copies.register(copy_ID=copy_code, isbn=book.isbn, status=status):
            print("\n¡Copia registrada exitosamente!")
            print("\nDatos de la copia:")
            print("-" * 50)
            copy = Copies.get_copy_by_id(copy_code)
            if copy:
                print(copy)
        else:
            print("\nError: No se pudo registrar la copia. El código ya existe.")

    except Exception as e:
        print(f"\nError al registrar la copia: {str(e)}")


def search_copy():
    print("\n====== BÚSQUEDA DE COPIAS ======\n")
    print("1. Ver todas las copias de un libro")
    print("2. Buscar copia por código")
    print("3. Volver\n")

    try:
        option = int(input("Seleccione una opción: "))

        if option == 1:
            book = find_book_by_isbn()
            if not book:
                return

            # Buscamos las copias del libro
            copies = Copies.get_copy_by_isbn(book.isbn)
            if copies:
                print("\nLibro encontrado:")
                print("-" * 50)
                print(book)
                print("\nCopias disponibles:")
                print("-" * 50)
                for copy in copies:
                    print(copy)
                    print("-" * 50)
            else:
                print("\nNo hay copias registradas para este libro.")

        elif option == 2:
            copy_code = input("\nIngrese el código de la copia: ").strip()
            while not copy_code:
                print("El código no puede estar vacío.")
                copy_code = input("Ingrese el código de la copia: ").strip()

            copy = Copies.get_copy_by_id(copy_code)
            if copy:
                print("\nCopia encontrada:")
                print("-" * 50)
                print(copy)
                print("-" * 50)

                # Mostramos también la información del libro
                book = Book.get_book_by_isbn(copy.isbn)
                if book:
                    print("Información del libro:")
                    print("-" * 50)
                    print(book)
                    print("-" * 50)
            else:
                print(f"\nNo se encontró ninguna copia con el código {copy_code}")

        elif option == 3:
            return
        else:
            print("\nOpción inválida. Por favor, intente nuevamente.")

    except ValueError:
        print("\nError: Por favor ingrese un número válido.")


def delete_copy():
    print("\n====== ELIMINAR COPIA ======\n")
    try:
        copy_code = input("Ingrese el código de la copia a eliminar: ").strip()
        while not copy_code:
            print("El código no puede estar vacío.")
            copy_code = input("Ingrese el código de la copia a eliminar: ").strip()

        # Verificamos si la copia existe y mostramos sus datos
        copy = Copies.get_copy_by_id(copy_code)
        if not copy:
            print(f"\nNo se encontró ninguna copia con el código {copy_code}")
            return

        print("\nCopia encontrada:")
        print("-" * 50)
        print(copy)
        print("-" * 50)

        # Mostramos también la información del libro asociado
        book = Book.get_book_by_isbn(copy.isbn)
        if book:
            print("Información del libro asociado:")
            print("-" * 50)
            print(book)
            print("-" * 50)

        # Confirmación de eliminación
        confirm = input("\n¿Está seguro que desea eliminar esta copia? (s/n): ").lower()
        if confirm == "s":
            if Copies.delete_copy(copy_code):
                print("\n¡Copia eliminada exitosamente!")
            else:
                print("\nError: No se pudo eliminar la copia.")
        else:
            print("\nOperación cancelada.")

    except Exception as e:
        print(f"\nError al eliminar la copia: {str(e)}")
