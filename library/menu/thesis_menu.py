from datetime import datetime
from library.helpers.item_status import ItemStatus
from library.items.thesis import Thesis
from library.menu.author_menu import select_authors
from library.menu.category_menu import select_categories


def handle_thesis_management():
    while True:
        print("\n======= GESTIÓN DE TESIS =======\n")
        print("1. Registrar tesis")
        print("2. Buscar tesis")
        print("3. Modificar tesis")
        print("4. Volver al menú principal\n")

        try:
            option = int(input("Seleccione una opción: "))

            if option == 1:
                register_thesis()
            elif option == 2:
                search_thesis()
            elif option == 3:
                modify_thesis()
            elif option == 4:
                print("\nVolviendo al menú principal...")
                break
            else:
                print("\nOpción inválida. Por favor, intente nuevamente.")

        except ValueError:
            print("\nError: Por favor ingrese un número válido.")


def search_thesis():
    print("\n====== BÚSQUEDA DE TESIS ======\n")
    print("1. Ver todas las tesis")
    print("2. Buscar tesis por código")
    print("3. Volver\n")

    try:
        option = int(input("Seleccione una opción: "))

        if option == 1:
            # Mostrar todas las tesis
            theses = Thesis.get_all_theses()
            if len(theses) == 0:
                print("\nNo hay tesis registradas en el sistema.")
                return

            print("\n=== LISTADO DE TESIS ===\n")
            print("\nCódigo | Título | Universidad | Estado")
            print("-" * 70)
            for thesis in theses:
                print(
                    f"{thesis.code} | {thesis.title} | {thesis.academy} | {thesis.status.value}"
                )
            print("-" * 70)

        elif option == 2:
            # Buscar por código
            code = input("\nIngrese el código de la tesis: ").strip()
            while not code:
                print("El código no puede estar vacío.")
                code = input("Ingrese el código de la tesis: ").strip()

            thesis = Thesis.get_thesis_by_code(code)
            if thesis:
                print("\n=== TESIS ENCONTRADA ===\n")
                print(thesis)
            else:
                print("\nNo se encontró ninguna tesis con ese código.")

        elif option == 3:
            return
        else:
            print("\nOpción inválida. Por favor, intente nuevamente.")

    except ValueError:
        print("\nError: Por favor ingrese un número válido.")


def modify_thesis():
    print("\n====== MODIFICAR TESIS ======\n")

    # Primero buscamos la tesis por código
    code = input("Ingrese el código de la tesis a modificar: ").strip()
    while not code:
        print("El código no puede estar vacío.")
        code = input("Ingrese el código de la tesis a modificar: ").strip()

    thesis = Thesis.get_thesis_by_code(code)
    if not thesis:
        print("\nNo se encontró ninguna tesis con ese código.")
        return

    try:
        # Datos básicos de la tesis
        print("\nDeje en blanco los campos que no desea modificar\n")

        title = input(f"Título actual: {thesis.title}\nNuevo título: ").strip()
        academy = input(f"Academia actual: {thesis.academy}\nNueva academia: ").strip()
        field = input(f"Campo actual: {thesis.field}\nNuevo campo de investigación: ").strip()

        # Fecha de investigación
        investi_date = thesis.investi_date
        investi_date_str = input(
            f"Nueva fecha de investigación ({thesis.investi_date}) [DD-MM-YYYY]: "
        ).strip()
        if investi_date_str:
            try:
                investi_date = datetime.strptime(
                    investi_date_str, "%d-%m-%Y"
                ).date()
            except ValueError:
                print("Formato de fecha inválido. No se actualizará la fecha de investigación.")

        # Fecha de publicación
        publication_date = thesis.publication_date
        publication_date_str = input(
            f"Nueva fecha de publicación ({thesis.publication_date}) [DD-MM-YYYY]: "
        ).strip()
        if publication_date_str:
            try:
                publication_date = datetime.strptime(
                    publication_date_str, "%d-%m-%Y"
                ).date()
            except ValueError:
                print("Formato de fecha inválido. No se actualizará la fecha de publicación.")

        # Número de páginas
        page_number = thesis.page_number
        pages_str = input(f"Número de páginas actual: {thesis.page_number}\nNuevo número de páginas: ").strip()
        if pages_str:
            try:
                page_number = int(pages_str)
                if page_number <= 0:
                    print("El número de páginas debe ser mayor que 0. No se actualizará.")
                    page_number = thesis.page_number
            except ValueError:
                print("Por favor ingrese un número válido. No se actualizará.")

        # Lista de autores
        print("\nSeleccione los nuevos autores:")
        authors = select_authors()

        # Categorías
        print("\nSeleccione las nuevas categorías:")
        categories = select_categories()

        # Estado
        status = thesis.status
        modify_status = input("\n¿Desea modificar el estado de la tesis? (s/n): ").lower()
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

        # Actualizamos la tesis
        thesis.update_thesis(
            new_title=title if title else None,
            new_academy=academy if academy else None,
            new_investi_date=investi_date,
            new_publication_date=publication_date,
            new_field=field if field else None,
            new_page_number=page_number,
            new_authors=authors,
            new_status=status,
            new_categories=categories
        )

        print("\n¡Tesis modificada exitosamente!")
        print("\nDatos actualizados de la tesis:")
        print("-" * 50)
        print(thesis)

    except Exception as e:
        print(f"\nError al modificar la tesis: {str(e)}")



def register_thesis():
    print("\n====== REGISTRO DE TESIS ======\n")
    try:
        # Datos básicos de la tesis
        title = input("Ingrese el título de la tesis: ").strip()
        while not title:
            print("El título no puede estar vacío.")
            title = input("Ingrese el título de la tesis: ").strip()

        academy = input("Ingrese la academia: ").strip()
        while not academy:
            print("La academia no puede estar vacía.")
            academy = input("Ingrese la academia: ").strip()

        field = input("Ingrese el campo de investigación: ").strip()
        while not field:
            print("El campo de investigación no puede estar vacío.")
            field = input("Ingrese el campo de investigación: ").strip()

        # Fecha de investigación
        while True:
            try:
                date_str = input(
                    "Ingrese la fecha de investigación (DD-MM-YYYY): "
                ).strip()
                investi_date = datetime.strptime(date_str, "%d-%m-%Y").date()
                break
            except ValueError:
                print(
                    "Fecha inválida. Por favor, ingrese la fecha en formato DD-MM-YYYY"
                )

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

        # Lista de autores
        print("\nSeleccione los autores:")
        authors = select_authors()

        while not authors:
            print("\nDebe ingresar al menos un autor.")
            authors = select_authors()


        # Número de páginas
        while True:
            page_str = input("Ingrese el número de páginas: ").strip()
            try:
                page_number = int(page_str)
                if page_number > 0:
                    break
                print("El número de páginas debe ser mayor que 0.")
            except ValueError:
                print("Por favor ingrese un número válido.")

        # Estado por defecto al registrar
        status = ItemStatus.AVAILABLE

        # Categorías
        print("\nSeleccione las categorías:")
        categories = select_categories()

        # Creamos la tesis
        Thesis.register(
            title=title,
            authors=authors,
            academy=academy,
            investi_date=investi_date,
            publication_date=publication_date,
            field=field,
            page_number=page_number,
            status=status,
            categories=categories
        )

        print("\n¡Tesis registrada exitosamente!")
        print("-" * 50)

    except Exception as e:
        print(f"\nError al registrar la tesis: {str(e)}")
