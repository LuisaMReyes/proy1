from datetime import date
from library.items.book import Book
from library.menu.articles_menu import handle_articles_management
from library.menu.author_menu import handle_authors_management
from library.menu.book_menu import handle_books_management
from library.menu.category_menu import handle_categories_management
from library.menu.copies_menu import handle_copies_management
from library.menu.loan_menu import handle_loans_management
from library.menu.reader_menu import handle_readers_management
from library.menu.thesis_menu import handle_thesis_management


def display_menu():
    while True:
        print("\n======= SISTEMA DE GESTIÓN DE BIBLIOTECA =======\n")
        print("1. Gestión de libros")
        print("2. Gestión de artículos científicos")
        print("3. Gestión de tesis")
        print("4. Gestión de categorías")
        print("5. Gestión de copias de libros")
        print("6. Gestión de autores")
        print("7. Gestión de lectores")
        print("8. Gestión de préstamos")
        print("9. Gestión de multas")
        print("0. Salir\n")

        try:
            option = int(input("Seleccione una opción: "))

            if option == 0:
                print("\nGracias por usar el sistema. ¡Hasta pronto!")
                break
            elif option == 1:
                handle_books_management()
            elif option == 2:
                handle_articles_management()
            elif option == 3:
                handle_thesis_management()
            elif option == 4:
                handle_categories_management()
            elif option == 5:
                handle_copies_management()
            elif option == 6:
                handle_authors_management()
            elif option == 7:
                handle_readers_management()
            elif option == 8:
                handle_loans_management()
            elif option == 9:
                handle_fines_management()
            else:
                print("\nOpción inválida. Por favor, intente nuevamente.")

        except ValueError:
            print("\nError: Por favor ingrese un número válido.")


def handle_fines_management():
    print("\nGestión de multas - En desarrollo...")
