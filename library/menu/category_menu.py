from library.categories.category import Category


def handle_categories_management():
    while True:
        print("\n======= GESTIÓN DE CATEGORÍAS =======\n")
        print("1. Crear categoría")
        print("2. Buscar categoría")
        print("3. Modificar categoría")
        print("4. Eliminar categoría")
        print("5. Asignar subcategoría")
        print("6. Volver al menú principal\n")

        try:
            option = int(input("Seleccione una opción: "))

            if option == 1:
                create_category()
            elif option == 2:
                search_category()
            elif option == 3:
                modify_category()
            elif option == 4:
                delete_category()
            elif option == 5:
                assign_subcategory()
            elif option == 6:
                break
            else:
                print("\nOpción inválida. Por favor, intente nuevamente.")

        except ValueError:
            print("\nError: Por favor ingrese un número válido.")


def create_category():
    print("\n====== CREAR CATEGORÍA ======\n")
    try:
        name = input("Ingrese el nombre de la categoría: ").strip()
        while not name:
            print("El nombre no puede estar vacío.")
            name = input("Ingrese el nombre de la categoría: ").strip()

        description = input("Ingrese la descripción de la categoría: ").strip()
        while not description:
            print("La descripción no puede estar vacía.")
            description = input("Ingrese la descripción de la categoría: ").strip()

        parent_id_str = input(
            "Ingrese el ID de la categoría padre (Enter si no tiene): "
        ).strip()
        parent_id = int(parent_id_str) if parent_id_str else None

        if parent_id and not Category.get_category_by_id(parent_id):
            print(f"\nError: No existe una categoría con el ID {parent_id}")
            return

        category = Category.create_category(
            name=name, description=description, parent_id=parent_id
        )
        print(f"\n¡Categoría '{name}' creada exitosamente con ID {category.id}!")

    except ValueError:
        print("\nError: El ID de la categoría padre debe ser un número.")
    except Exception as e:
        print(f"\nError al crear la categoría: {str(e)}")


def search_category():
    print("\n====== BUSCAR CATEGORÍA ======\n")
    print("1. Buscar por ID")
    print("2. Ver todas las categorías")

    try:
        option = int(input("\nSeleccione una opción: "))

        if option == 1:
            try:
                category_id = int(input("\nIngrese el ID de la categoría: "))
                category = Category.get_category_by_id(category_id)

                if category:
                    print("\nCategoría encontrada:")
                    print("-" * 50)
                    print(category)
                    if category.subcategories:
                        print("\nSubcategorías:")
                        for sub in category.subcategories:
                            print(f"- {sub.name} (ID: {sub.id})")
                else:
                    print(f"\nNo se encontró ninguna categoría con ID {category_id}")

            except ValueError:
                print("\nError: El ID debe ser un número.")

        elif option == 2:
            categories = Category.get_all_categories()
            if not categories:
                print("\nNo hay categorías registradas.")
                return

            print("\nLista de todas las categorías:")
            print("-" * 50)
            for category in categories:
                print(f"\nID: {category.id}")
                print(f"Nombre: {category.name}")
                print(f"Descripción: {category.description}")
                if category.subcategories:
                    print("Subcategorías:")
                    for sub in category.subcategories:
                        print(f"  - {sub.name} (ID: {sub.id})")
                print("-" * 50)
        else:
            print("\nOpción inválida.")

    except ValueError:
        print("\nError: Por favor ingrese un número válido.")


def modify_category():
    print("\n====== MODIFICAR CATEGORÍA ======\n")
    try:
        category_id = int(input("Ingrese el ID de la categoría a modificar: "))
        category = Category.get_category_by_id(category_id)

        if not category:
            print(f"\nNo se encontró ninguna categoría con ID {category_id}")
            return

        print(f"\nCategoría actual:\n{category}")

        print("\nDeje en blanco los campos que no desea modificar\n")

        new_name = input("Nuevo nombre: ").strip()
        new_description = input("Nueva descripción: ").strip()

        if not new_name and not new_description:
            print("\nNo se realizaron modificaciones.")
            return

        success = Category.patch_category(
            category_id,
            name=new_name if new_name else None,
            description=new_description if new_description else None,
        )

        if success:
            print("\n¡Categoría modificada exitosamente!")
        else:
            print("\nError al modificar la categoría.")

    except ValueError:
        print("\nError: El ID debe ser un número.")
    except Exception as e:
        print(f"\nError al modificar la categoría: {str(e)}")


def delete_category():
    print("\n====== ELIMINAR CATEGORÍA ======\n")
    try:
        category_id = int(input("Ingrese el ID de la categoría a eliminar: "))
        category = Category.get_category_by_id(category_id)

        if not category:
            print(f"\nNo se encontró ninguna categoría con ID {category_id}")
            return

        print(f"\nCategoría a eliminar:\n{category}")

        if category.subcategories:
            print(
                "\n¡ADVERTENCIA! Esta categoría tiene subcategorías que también serán eliminadas."
            )

        confirm = input(
            "\n¿Está seguro que desea eliminar esta categoría? (s/N): "
        ).lower()

        if confirm != "s":
            print("\nOperación cancelada.")
            return

        success = Category.delete_category(category_id)

        if success:
            print("\n¡Categoría eliminada exitosamente!")
        else:
            print("\nError al eliminar la categoría.")

    except ValueError:
        print("\nError: El ID debe ser un número.")
    except Exception as e:
        print(f"\nError al eliminar la categoría: {str(e)}")


def select_categories() -> list[Category]:
    """Muestra un menú para seleccionar categorías y retorna la lista de categorías seleccionadas."""
    categories = []
    while True:
        print("\n=== MENU DE CATEGORÍAS ===")
        print("1. Adicionar categoría con ID")
        print("2. Ver categorías")
        print("3. Terminar de ingresar datos\n")

        option = input("Seleccione una opción: ").strip()

        if option == "1":
            try:
                category_id = int(input("\nIngrese el ID de la categoría: ").strip())
                category = Category.get_category_by_id(category_id)
            except ValueError:
                print("\nError: El ID debe ser un número.")
                continue
            if category:
                if category not in categories:  # Evita duplicados
                    categories.append(category)
                    print(f"\nCategoría agregada exitosamente:")
                    print(category)
                else:
                    print("\nEsta categoría ya fue agregada al libro.")
            else:
                print("\nNo se encontró ninguna categoría con ese ID.")

        elif option == "2":
            print("\nListado de categorías disponibles:")
            search_category()
            
        elif option == "3" or option.strip() == "":
            break
        else:
            print("\nOpción inválida. Por favor, intente nuevamente.")

    return categories


def assign_subcategory():
    print("\n====== ASIGNAR SUBCATEGORÍA ======\n")
    try:
        parent_id = int(input("Ingrese el ID de la categoría padre: "))
        parent = Category.get_category_by_id(parent_id)

        if not parent:
            print(f"\nNo se encontró ninguna categoría con ID {parent_id}")
            return

        subcategory_id = int(
            input("Ingrese el ID de la categoría que desea asignar como subcategoría: ")
        )
        subcategory = Category.get_category_by_id(subcategory_id)

        if not subcategory:
            print(f"\nNo se encontró ninguna categoría con ID {subcategory_id}")
            return

        if parent_id == subcategory_id:
            print("\nError: Una categoría no puede ser subcategoría de sí misma.")
            return

        if subcategory in parent.subcategories:
            print("\nEsta categoría ya es una subcategoría de la categoría padre.")
            return

        parent.add_subcategory(subcategory)
        subcategory.parent_id = parent_id

        print("\n¡Subcategoría asignada exitosamente!")

    except ValueError:
        print("\nError: Los IDs deben ser números.")
    except Exception as e:
        print(f"\nError al asignar la subcategoría: {str(e)}")
