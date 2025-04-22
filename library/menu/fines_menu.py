from datetime import date, datetime
from library.fines.fine import Fine
from library.helpers.fine_status import Fine_Status
from library.loans.loan import Loan


def handle_fines_management():
    while True:
        print("\n======= GESTIÓN DE MULTAS =======\n")
        print("1. Consultar multa")
        print("2. Generar multa")
        print("3. Levantar multa")
        print("4. Volver al menú principal\n")

        try:
            option = int(input("Seleccione una opción: "))

            if option == 1:
                search_fine()
            elif option == 2:
                generate_fine()
            elif option == 3:
                lift_fine()
            elif option == 4:
                print("\nVolviendo al menú principal...")
                break
            else:
                print("\nOpción inválida. Por favor, intente nuevamente.")

        except ValueError:
            print("\nError: Por favor ingrese un número válido.")


def search_fine():
    print("\n====== CONSULTA DE MULTAS ======\n")
    print("1. Ver todas las multas")
    print("2. Ver multas activas")
    print("3. Ver multas inactivas")
    print("4. Buscar multa por ID")
    print("5. Buscar multas por ID de lector")
    print("6. Volver\n")

    try:
        option = int(input("Seleccione una opción: "))

        if option == 1:
            fines = Fine.get_all_fines()
            display_fines(fines, "LISTADO DE TODAS LAS MULTAS")

        elif option == 2:
            fines = Fine.get_active_fines()
            display_fines(fines, "LISTADO DE MULTAS ACTIVAS")

        elif option == 3:
            fines = Fine.get_inactive_fines()
            display_fines(fines, "LISTADO DE MULTAS INACTIVAS")

        elif option == 4:
            fine_id = input("\nIngrese el ID de la multa: ").strip()
            fine = Fine.get_fine_by_id(fine_id)
            if fine:
                print("\n=== MULTA ENCONTRADA ===\n")
                print(fine)
            else:
                print("\nNo se encontró ninguna multa con ese ID.")

        elif option == 5:
            reader_id = input("\nIngrese el ID del lector: ").strip()
            fines = Fine.get_fines_by_reader_id(reader_id)
            display_fines(fines, f"MULTAS DEL LECTOR {reader_id}")

        elif option == 6:
            return
        else:
            print("\nOpción inválida. Por favor, intente nuevamente.")

    except ValueError:
        print("\nError: Por favor ingrese un número válido.")


def generate_fine():
    print("\n====== GENERAR MULTA ======\n")

    # Obtener todos los préstamos
    loans = Loan.get_active_loans()
    fines_generated = 0

    for loan in loans:
        # Verificar si ya existe una multa para este préstamo
        existing_fine = next(
            (
                fine
                for fine in Fine.get_all_fines()
                if fine.loan.loan_id == loan.loan_id
            ),
            None,
        )

        if existing_fine:
            continue

        # Verificar si el préstamo está retrasado
        real_delivery_date = date.today()
        delay_days = (real_delivery_date - loan.estimated_return_date).days

        if delay_days > 0:
            # Generar la multa
            fine = Fine.generate_fine(loan, real_delivery_date)
            fines_generated += 1
            print(f"\nMulta generada para el préstamo {loan.loan_id}:")
            print(fine)

    if fines_generated == 0:
        print("\nNo se encontraron préstamos retrasados sin multa.")
    else:
        print(f"\nSe generaron {fines_generated} multas nuevas.")


def lift_fine():
    print("\n====== LEVANTAR MULTA ======\n")

    fine_id = input("Ingrese el ID de la multa a levantar: ").strip()
    while not fine_id:
        print("El ID de la multa no puede estar vacío.")
        fine_id = input("Ingrese el ID de la multa a levantar: ").strip()

    fine = Fine.get_fine_by_id(fine_id)
    if not fine:
        print("\nNo se encontró ninguna multa con ese ID.")
        return

    if fine.status != Fine_Status.ACTIVE:
        print("\nLa multa no está activa, no se puede levantar.")
        return

    # Intentamos levantar la multa
    if Fine.lift_fine(fine_id):
        print("\n¡Multa levantada exitosamente!")
    else:
        print(
            "\nNo se pudo levantar la multa. Verifique que haya cumplido el período de penalización."
        )


def display_fines(fines, title):
    if not fines:
        print("\nNo hay multas para mostrar.")
        return

    print(f"\n=== {title} ===\n")
    for fine in fines:
        print("-" * 50)
        print(fine)
    print("-" * 50)
