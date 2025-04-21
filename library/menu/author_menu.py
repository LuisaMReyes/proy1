from datetime import datetime
from library.people.author import Author


def handle_authors_management():
    while True:
        print("\n=== GESTIÓN DE AUTORES ===\n")
        print("1. Registrar autor")
        print("2. Buscar autor")
        print("3. Modificar autor")
        print("4. Volver al menú principal\n")

        try:
            option = int(input("Seleccione una opción: "))

            if option == 1:
                create_author()
            elif option == 2:
                search_author()
            elif option == 3:
                modify_author()
            elif option == 4:
                break
            else:
                print("\nOpción inválida. Por favor, intente nuevamente.")

        except ValueError:
            print("\nError: Por favor ingrese un número válido.")


def create_author():
    print("\n--- Registro de Autor ---")
    author_id = input("Ingrese el ID del autor: ")
    name = input("Ingrese el nombre del autor: ")
    nationality = input("Ingrese la nacionalidad del autor: ")
    
    while True:
        try:
            birth_date_str = input("Ingrese la fecha de nacimiento (DD-MM-YYYY): ")
            birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Formato de fecha inválido. Use DD-MM-YYYY")
    
    if Author.create(author_id, name, nationality, birth_date):
        print("\n¡Autor registrado exitosamente!")
    else:
        print("\nError: Ya existe un autor con ese ID.")


def search_author():
    print("\n====== BUSCAR AUTOR ======\n")
    print("1. Buscar por ID")
    print("2. Ver todos los autores")

    try:
        option = int(input("\nSeleccione una opción: "))

        if option == 1:
            author_id = input("\nIngrese el ID del autor: ")
            author = Author.get_author_by_id(author_id)

            if author:
                print("\nAutor encontrado:")
                print("-" * 50)
                print(author)
                print("-" * 50)
            else:
                print(f"\nNo se encontró ningún autor con ID {author_id}")

        elif option == 2:
            authors = Author.get_authors()
            if not authors:
                print("\nNo hay autores registrados.")
                return

            print("\nLista de todos los autores:")

            for author in authors:

                print("-" * 50)
                print(author)
            print("-" * 50)
        else:
            print("\nOpción inválida.")

    except ValueError:
        print("\nError: Por favor ingrese un número válido.")


def modify_author():
    print("\n--- Modificación de Autor ---")
    author_id = input("Ingrese el ID del autor a modificar: ")
    
    author = Author.get_author_by_id(author_id)
    if not author:
        print("\nNo se encontró ningún autor con ese ID.")
        return

    print("\nDeje en blanco los campos que no desea modificar:")
    
    name = input(f"Nuevo nombre ({author.name}): ").strip()
    nationality = input(f"Nueva nacionalidad ({author.nationality}): ").strip()
    
    birth_date = None
    birth_date_str = input(f"Nueva fecha de nacimiento ({author.birth_date}) [DD-MM-YYYY]: ").strip()
    if birth_date_str:
        try:
            birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y").date()
        except ValueError:
            print("Formato de fecha inválido. No se actualizará la fecha.")
    
    if Author.patch_author(
        author_id,
        name if name else None,
        nationality if nationality else None,
        birth_date
    ):
        print("\n¡Autor modificado exitosamente!")
    else:
        print("\nError al modificar el autor.")
