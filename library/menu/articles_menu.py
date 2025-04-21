from datetime import datetime
from library.helpers.item_status import ItemStatus
from library.items.article import Article
from library.menu.author_menu import select_authors
from library.menu.category_menu import select_categories


def handle_articles_management():
    while True:
        print("\n======= GESTIÓN DE ARTÍCULOS =======\n")
        print("1. Registrar artículo")
        print("2. Buscar artículo")
        print("3. Modificar artículo")
        print("4. Volver al menú principal\n")

        try:
            option = int(input("Seleccione una opción: "))

            if option == 1:
                register_article()
            elif option == 2:
                search_article()
            elif option == 3:
                modify_article()
            elif option == 4:
                print("\nVolviendo al menú principal...")
                break
            else:
                print("\nOpción inválida. Por favor, intente nuevamente.")

        except ValueError:
            print("\nError: Por favor ingrese un número válido.")


def search_article():
    print("\n====== BÚSQUEDA DE ARTÍCULOS ======\n")
    print("1. Ver todos los artículos")
    print("2. Buscar artículo por doi")
    print("3. Volver\n")

    try:
        option = int(input("Seleccione una opción: "))

        if option == 1:
            # Mostrar todos los artículos
            articles = Article.get_all_articles()
            if len(articles) == 0:
                print("\nNo hay artículos registrados en el sistema.")
                return

            print("\n=== LISTADO DE ARTÍCULOS ===\n")
            print("\ndoi | Título | Revista | Estado")
            print("-" * 70)
            for article in articles:
                print(
                    f"{article.doi} | {article.title} | {article.journal} | {article.status.value}"
                )
            print("-" * 70)

        elif option == 2:
            # Buscar por doi
            doi = input("\nIngrese el doi del artículo: ").strip()
            while not doi:
                print("El doi no puede estar vacío.")
                doi = input("Ingrese el doi del artículo: ").strip()

            article = Article.get_article_by_doi(doi)
            if article:
                print("\n=== ARTÍCULO ENCONTRADO ===\n")
                print(article)
            else:
                print("\nNo se encontró ningún artículo con ese doi.")

        elif option == 3:
            return
        else:
            print("\nOpción inválida. Por favor, intente nuevamente.")

    except ValueError:
        print("\nError: Por favor ingrese un número válido.")


def modify_article():
    print("\n====== MODIFICAR ARTÍCULO ======\n")

    # Primero buscamos el artículo por doi
    doi = input("Ingrese el doi del artículo a modificar: ").strip()
    while not doi:
        print("El doi no puede estar vacío.")
        doi = input("Ingrese el doi del artículo a modificar: ").strip()

    article = Article.get_article_by_doi(doi)
    if not article:
        print("\nNo se encontró ningún artículo con ese doi.")
        return

    try:
        # Datos básicos del artículo
        print("\nDeje en blanco los campos que no desea modificar\n")

        title = input(f"Título actual: {article.title}\nNuevo título: ").strip()
        journal = input(f"Revista actual: {article.journal}\nNueva revista: ").strip()
        publisher_name = input(f"Editorial actual: {article.publisher_name}\nNueva editorial: ").strip()
        periodicity = input(f"Periodicidad actual: {article.periodicity}\nNueva periodicidad: ").strip()
        volume = input(f"Volumen actual: {article.volume}\nNuevo volumen: ").strip()
        field = input(f"Campo de estudio actual: {article.field}\nNuevo campo: ").strip()

        # Fecha de publicación
        publication_date = article.publication_date
        publication_date_str = input(
            f"Nueva fecha de publicación ({article.publication_date}) [DD-MM-YYYY]: "
        ).strip()
        if publication_date_str:
            try:
                publication_date = datetime.strptime(
                    publication_date_str, "%d-%m-%Y"
                ).date()
            except ValueError:
                print("Formato de fecha inválido. No se actualizará la fecha.")

        # Lista de autores
        authors = select_authors()

        while not authors:
            print("\nDebe ingresar al menos un autor.")
            authors = select_authors()

        # Categorías
        categories = select_categories()

        # Estado
        status: ItemStatus = ItemStatus.AVAILABLE
        modify_status = input(
            "\n¿Desea modificar el estado del artículo? (s/n): "
        ).lower()
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

        # Actualizamos el artículo
        article.update_article(
            new_title=title,
            new_journal=journal,
            new_publication_date=publication_date,
            new_authors=authors,
            new_status=status,
            new_categories=categories,
            new_publisher_name=publisher_name,
            new_periodicity=periodicity,
            new_volume=volume,
            new_field=field,
        )

        print("\n¡Artículo modificado exitosamente!")
        print("\nDatos actualizados del artículo:")
        print("-" * 50)
        print(article)

    except Exception as e:
        print(f"\nError al modificar el artículo: {str(e)}")


def register_article():
    print("\n====== REGISTRO DE ARTÍCULO ======\n")
    try:
        # Datos básicos del artículo
        title = input("Ingrese el título del artículo: ").strip()
        while not title:
            print("El título no puede estar vacío.")
            title = input("Ingrese el título del artículo: ").strip()

        journal = input("Ingrese la revista: ").strip()
        while not journal:
            print("La revista no puede estar vacía.")
            journal = input("Ingrese la revista: ").strip()

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
        authors = select_authors()

        while not authors:
            print("\nDebe ingresar al menos un autor.")
            authors = select_authors()

        doi = input("Ingrese el doi del artículo: ").strip()
        while not doi:
            print("El doi no puede estar vacío.")
            doi = input("Ingrese el doi del artículo: ").strip()

        # Editorial
        publisher_name = input("Ingrese el nombre de la editorial: ").strip()
        while not publisher_name:
            print("La editorial no puede estar vacía.")
            publisher_name = input("Ingrese el nombre de la editorial: ").strip()

        # Periodicidad
        periodicity = input("Ingrese la periodicidad de la revista (ej: Mensual, Trimestral): ").strip()
        while not periodicity:
            print("La periodicidad no puede estar vacía.")
            periodicity = input("Ingrese la periodicidad de la revista: ").strip()

        # Volumen
        volume = input("Ingrese el volumen del artículo: ").strip()
        while not volume:
            print("El volumen no puede estar vacío.")
            volume = input("Ingrese el volumen del artículo: ").strip()

        # Campo de estudio
        field = input("Ingrese el campo de estudio: ").strip()
        while not field:
            print("El campo de estudio no puede estar vacío.")
            field = input("Ingrese el campo de estudio: ").strip()

        # Estado por defecto al registrar
        status = ItemStatus.AVAILABLE

        # Categorías
        categories = select_categories()

        # Registramos el artículo
        if Article.create(
            title=title,
            journal=journal,
            publication_date=publication_date,
            authors=authors,
            doi=doi,
            status=status,
            categories=categories,
            publisher_name=publisher_name,
            periodicity=periodicity,
            volume=volume,
            field=field,
        ):
            print("\n¡Artículo registrado exitosamente!")
        else:
            print("\nError: El doi ya existe en el sistema.")

    except Exception as e:
        print(f"\nError al registrar el artículo: {str(e)}")
