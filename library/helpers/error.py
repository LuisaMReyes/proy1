from enum import Enum


class ErrorType(Enum):
    AUTHOR_ALREADY_EXISTS = "El id del autor ya existe."
    INVALID_DATE = "La fecha es invalida."
    AUTHOR_NOT_FOUND = "El autor no fue encontrado."
    COPY_ALREADY_EXISTS="El id de la copia ya existe"
    COPY_NOT_FOUND="Copia no encontrada"
    NO_COPIES_FOR_BOOK="No hay copia registrada para este libro"


class ErrorManager:
    def __init__(self, error_type: ErrorType):
        self.message = error_type.value
        self.print()

    def print(self):
        RED = "\033[91m"
        RESET = "\033[0m"
        print(f"{RED}Error: {self.message}{RESET}")
