from library.people.reader import Reader
from library.helpers.reader_status import ReaderStatus
from datetime import datetime

def handle_readers_management():
    while True:
        print("\n======= GESTIÓN DE LECTORES =======\n")
        print("1. Registrar lector")
        print("2. Buscar lector")
        print("3. Modificar lector")
        print("4. Habilitar lector")
        print("5. Inhabilitar lector")
        print("6. Consultar préstamos del lector")
        print("7. Consultar multas del lector")
        print("8. Volver al menú principal\n")

        try:
            option = int(input("Seleccione una opción: "))

            if option == 1:
                register_reader()
            elif option == 2:
                search_reader()
            elif option == 3:
                modify_reader()
            elif option == 4:
                change_reader_status(ReaderStatus.NORMAL)
            elif option == 5:
                change_reader_status(ReaderStatus.INACTIVE)
            elif option == 6:
                check_reader_loans()
            elif option == 7:
                check_reader_fines()
            elif option == 8:
                print("\nVolviendo al menú principal...")
                break
            else:
                print("\nOpción inválida. Por favor, intente nuevamente.")

        except ValueError:
            print("\nError: Por favor ingrese un número válido.")

def register_reader():
    print("\n====== REGISTRO DE LECTOR ======\n")
    try:
        reader_id = input("Ingrese el ID del lector: ").strip()
        while not reader_id:
            print("El ID no puede estar vacío.")
            reader_id = input("Ingrese el ID del lector: ").strip()

        name = input("Ingrese el nombre del lector: ").strip()
        while not name:
            print("El nombre no puede estar vacío.")
            name = input("Ingrese el nombre del lector: ").strip()

        phone = input("Ingrese el teléfono del lector: ").strip()
        while not phone:
            print("El teléfono no puede estar vacío.")
            phone = input("Ingrese el teléfono del lector: ").strip()

        address = input("Ingrese la dirección del lector: ").strip()
        while not address:
            print("La dirección no puede estar vacía.")
            address = input("Ingrese la dirección del lector: ").strip()

        if Reader.create(reader_id, name, phone, address, ReaderStatus.NORMAL):
            print("\n¡Lector registrado exitosamente!")
        else:
            print("\nError: El ID ya existe en el sistema.")

    except Exception as e:
        print(f"\nError al registrar el lector: {str(e)}")

def search_reader():
    print("\n====== BÚSQUEDA DE LECTORES ======\n")
    print("1. Ver todos los lectores")
    print("2. Buscar lector por ID")
    print("3. Volver\n")

    try:
        option = int(input("Seleccione una opción: "))

        if option == 1:
            readers = Reader.get_all()
            if not readers:
                print("\nNo hay lectores registrados en el sistema.")
                return

            print("\n=== LISTADO DE LECTORES ===\n")
            print("\nID | Nombre | Teléfono | Estado")
            print("-" * 70)
            for r in readers:
                print(f"{r.reader_id} | {r.name} | {r.phone} | {r.status.value}")
            print("-" * 70)

        elif option == 2:
            reader_id = input("\nIngrese el ID del lector: ").strip()
            while not reader_id:
                print("El ID no puede estar vacío.")
                reader_id = input("Ingrese el ID del lector: ").strip()

            found_reader = Reader.get_by_id(reader_id)
            if found_reader:
                print("\n=== LECTOR ENCONTRADO ===\n")
                print(f"ID: {found_reader.reader_id}")
                print(f"Nombre: {found_reader.name}")
                print(f"Teléfono: {found_reader.phone}")
                print(f"Dirección: {found_reader.address}")
                print(f"Estado: {found_reader.status.value}")
            else:
                print("\nNo se encontró ningún lector con ese ID.")

    except ValueError:
        print("\nError: Por favor ingrese un número válido.")

def modify_reader():
    print("\n====== MODIFICAR LECTOR ======\n")
    reader_id = input("Ingrese el ID del lector a modificar: ").strip()
    while not reader_id:
        print("El ID no puede estar vacío.")
        reader_id = input("Ingrese el ID del lector a modificar: ").strip()

    found_reader = Reader.get_by_id(reader_id)
    
    if not found_reader:
        print("\nNo se encontró ningún lector con ese ID.")
        return

    print("\nDeje en blanco los campos que no desea modificar\n")
    
    name = input(f"Nombre actual: {found_reader.name}\nNuevo nombre: ").strip()
    phone = input(f"Teléfono actual: {found_reader.phone}\nNuevo teléfono: ").strip()
    address = input(f"Dirección actual: {found_reader.address}\nNueva dirección: ").strip()

    if found_reader.modify(reader_id, name, phone, address):
        print("\n¡Lector modificado exitosamente!")
    else:
        print("\nError al modificar el lector.")

def change_reader_status(new_status: ReaderStatus):
    action = "Habilitar" if new_status == ReaderStatus.NORMAL else "Inhabilitar"
    print(f"\n====== {action.upper()} LECTOR ======\n")
    
    reader_id = input("Ingrese el ID del lector: ").strip()
    while not reader_id:
        print("El ID no puede estar vacío.")
        reader_id = input("Ingrese el ID del lector: ").strip()

    if Reader.set_status(reader_id, new_status):
        print(f"\n¡Lector {action.lower()}do exitosamente!")
    else:
        print(f"\nError al {action.lower()} el lector.")

def check_reader_loans():
    print("\n====== CONSULTAR PRÉSTAMOS DEL LECTOR ======\n")
    
    reader_id = input("Ingrese el ID del lector: ").strip()
    while not reader_id:
        print("El ID no puede estar vacío.")
        reader_id = input("Ingrese el ID del lector: ").strip()

    found_reader = Reader.get_by_id(reader_id)
    
    if not found_reader:
        print("\nNo se encontró ningún lector con ese ID.")
        return

    active_loans = Reader.get_active_loans(reader_id)
    if not active_loans:
        print("\nEl lector no tiene préstamos activos.")
        return

    print("\n=== PRÉSTAMOS ACTIVOS ===\n")
    print("ID Préstamo | Tipo | ID Producto | Fecha Préstamo | Fecha Devolución")
    print("-" * 70)
    for loan in active_loans:
        print(f"{loan.loan_id} | {loan.product_type.value} | {loan.product_id} | "
              f"{loan.loan_date} | {loan.estimated_return_date}")
    print("-" * 70)

def check_reader_fines():
    print("\n====== CONSULTAR MULTAS DEL LECTOR ======\n")
    
    reader_id = input("Ingrese el ID del lector: ").strip()
    while not reader_id:
        print("El ID no puede estar vacío.")
        reader_id = input("Ingrese el ID del lector: ").strip()

    found_reader = Reader.get_by_id(reader_id)
    
    if not found_reader:
        print("\nNo se encontró ningún lector con ese ID.")
        return

    fines = Reader.get_fines(reader_id)
    if not fines:
        print("\nEl lector no tiene multas activas.")
        return

    print("\n=== MULTAS ACTIVAS ===\n")
    for fine in fines:
        print(fine)

