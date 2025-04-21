from datetime import date, datetime
from typing import List
from library.helpers.item_type import ProductType
from library.loans.loan import Loan
from library.items.book import Book
from library.items.thesis import Thesis
from library.items.article import Article


def handle_loans_management():
    while True:
        print("\n======= GESTIÓN DE PRÉSTAMOS =======\n")
        print("1. Registrar préstamo")
        print("2. Consultar préstamo")
        print("3. Cancelar préstamo")
        print("4. Finalizar préstamo")
        print("5. Volver al menú principal\n")

        try:
            option = int(input("Seleccione una opción: "))

            if option == 1:
                register_loan()
            elif option == 2:
                search_loan()
            elif option == 3:
                cancel_loan()
            elif option == 4:
                finish_loan()
            elif option == 5:
                print("\nVolviendo al menú principal...")
                break
            else:
                print("\nOpción inválida. Por favor, intente nuevamente.")

        except ValueError:
            print("\nError: Por favor ingrese un número válido.")


def register_loan():
    print("\n====== REGISTRO DE PRÉSTAMO ======\n")
    try:
        # Tipo de producto
        print("\nTipos de producto disponibles:")
        print("1. Libro")
        print("2. Tesis")
        print("3. Artículo")

        while True:
            try:
                type_option = int(input("\nSeleccione el tipo de producto: "))
                if type_option == 1:
                    product_type = ProductType.BOOK
                    break
                elif type_option == 2:
                    product_type = ProductType.THESIS
                    break
                elif type_option == 3:
                    product_type = ProductType.ARTICLE
                    break
                else:
                    print("Opción inválida. Por favor, seleccione 1, 2 o 3.")
            except ValueError:
                print("Por favor ingrese un número válido.")

        while True:
            # Preguntamos si el usuario quiere ver los productos disponibles
            view_products = (
                input("\n¿Desea ver los productos disponibles? (s/n/c para cancelar): ")
                .strip()
                .lower()
            )
            while view_products not in ["s", "n", "c"]:
                print(
                    "Opción inválida. Por favor, ingrese 's', 'n' o 'c' para cancelar."
                )
                view_products = (
                    input(
                        "\n¿Desea ver los productos disponibles? (s/n/c para cancelar): "
                    )
                    .strip()
                    .lower()
                )

            if view_products == "c":
                print("\nOperación cancelada.")
                return

            if view_products == "s":
                # Obtenemos todos los productos del tipo seleccionado
                products = get_all_product_by_type(product_type)
                if not products:
                    print("\nNo hay productos disponibles de ese tipo.")
                    return

                print("\n=== PRODUCTOS DISPONIBLES ===\n")
                for product in products:
                    print(product)

            # ID del producto (ISBN para libros, código para artículos/tesis)
            product_id = input("\nIngrese el ID del producto: ").strip()
            while not product_id:
                print("El ID del producto no puede estar vacío.")
                product_id = input("Ingrese el ID del producto: ").strip()

            # Validamos que el producto exista
            if validate_product_exists(product_type, product_id):
                break

            print(
                f"\nError: No existe un {product_type.get_display_name()} con ID: {product_id}"
            )
            print("Por favor, intente nuevamente.")

        # ID del lector
        reader_id = input("Ingrese el ID del lector: ").strip()
        while not reader_id:
            print("El ID del lector no puede estar vacío.")
            reader_id = input("Ingrese el ID del lector: ").strip()

        # Días de préstamo
        while True:
            try:
                days = int(input("Ingrese la cantidad de días del préstamo: "))
                if days > 0:
                    break
                print("La cantidad de días debe ser mayor a 0.")
            except ValueError:
                print("Por favor ingrese un número válido.")

        # Generamos ID único para el préstamo
        loan_id = f"LOAN{Loan.next_id}"
        Loan.next_id += 1

        # Registramos el préstamo
        if Loan.register(
            loan_id=loan_id,
            product_type=product_type,
            product_id=product_id,
            reader_id=reader_id,
            days=days,
            loan_date=date.today(),
        ):
            print("\n¡Préstamo registrado exitosamente!")
            print(f"ID del préstamo: {loan_id}")
        else:
            print("\nError: El ID del préstamo ya existe en el sistema.")

    except Exception as e:
        print(f"\nError al registrar el préstamo: {str(e)}")


def search_loan():
    print("\n====== BÚSQUEDA DE PRÉSTAMOS ======\n")
    print("1. Ver todos los préstamos")
    print("2. Buscar préstamo por ID")
    print("3. Buscar préstamos por lector")
    print("4. Volver\n")

    try:
        option = int(input("Seleccione una opción: "))

        if option == 1:
            # Mostrar todos los préstamos
            loans = Loan.get_all()
            if not loans:
                print("\nNo hay préstamos registrados en el sistema.")
                return

            print("\n=== LISTADO DE PRÉSTAMOS ===\n")
            print_loans(loans)

        elif option == 2:
            # Buscar por ID
            loan_id = input("\nIngrese el ID del préstamo: ").strip()
            while not loan_id:
                print("El ID no puede estar vacío.")
                loan_id = input("Ingrese el ID del préstamo: ").strip()

            loan = Loan.get_by_id(loan_id)
            if loan:
                print("\n=== PRÉSTAMO ENCONTRADO ===\n")
                print_loans([loan])
            else:
                print("\nNo se encontró ningún préstamo con ese ID.")

        elif option == 3:
            # Buscar por lector
            reader_id = input("\nIngrese el ID del lector: ").strip()
            while not reader_id:
                print("El ID del lector no puede estar vacío.")
                reader_id = input("Ingrese el ID del lector: ").strip()

            loans = Loan.get_by_reader_id(reader_id)
            if loans:
                print("\n=== PRÉSTAMOS ENCONTRADOS ===\n")
                print_loans(loans)
            else:
                print("\nNo se encontraron préstamos para ese lector.")

        elif option == 4:
            return
        else:
            print("\nOpción inválida. Por favor, intente nuevamente.")

    except ValueError:
        print("\nError: Por favor ingrese un número válido.")


def cancel_loan():
    print("\n====== CANCELAR PRÉSTAMO ======\n")

    loan_id = input("Ingrese el ID del préstamo a cancelar: ").strip()
    while not loan_id:
        print("El ID no puede estar vacío.")
        loan_id = input("Ingrese el ID del préstamo a cancelar: ").strip()

    if Loan.cancel(loan_id):
        print("\n¡Préstamo cancelado exitosamente!")
    else:
        print("\nNo se encontró ningún préstamo con ese ID.")


def finish_loan():
    print("\n====== FINALIZAR PRÉSTAMO ======\n")

    loan_id = input("Ingrese el ID del préstamo a finalizar: ").strip()
    while not loan_id:
        print("El ID no puede estar vacío.")
        loan_id = input("Ingrese el ID del préstamo a finalizar: ").strip()

    if Loan.cancel(loan_id):
        print("\n¡Préstamo finalizado exitosamente!")
    else:
        print("\nNo se encontró ningún préstamo con ese ID.")


def print_loans(loans: List[Loan]):
    print(
        "ID | Tipo | ID Producto | ID Lector | Días | Fecha Préstamo | Fecha Devolución | Estado"
    )
    print("-" * 100)
    for loan in loans:
        status = "Activo" if loan.active else "Finalizado"
        print(
            f"{loan.loan_id} | {loan.product_type.get_display_name()} | {loan.product_id} | "
            f"{loan.reader_id} | {loan.days} | {loan.loan_date} | "
            f"{loan.estimated_return_date} | {status}"
        )
    print("-" * 100)


def validate_product_exists(product_type: ProductType, product_id: str) -> bool:
    if product_type == ProductType.BOOK:
        return Book.get_book_by_isbn(product_id) != None
    elif product_type == ProductType.THESIS:
        return Thesis.get_thesis_by_code(product_id) != None
    elif product_type == ProductType.ARTICLE:
        return Article.get_article_by_doi(product_id) != None


def get_all_product_by_type(
    product_type: ProductType,
) -> List[Book] | List[Thesis] | List[Article]:
    if product_type == ProductType.BOOK:
        return Book.get_books()
    elif product_type == ProductType.THESIS:
        return Thesis.get_all_theses()
    elif product_type == ProductType.ARTICLE:
        return Article.get_all_articles()
