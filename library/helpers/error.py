from enum import Enum


class ErrorType(Enum):
    AUTHOR_ALREADY_EXISTS = "El id del autor ya existe."
    INVALID_DATE = "La fecha es invalida."
    AUTHOR_NOT_FOUND = "El autor no fue encontrado."


class ErrorManager:
    def __init__(self, error_type: ErrorType):
        self.message = error_type.value
        self.print()

    def print(self):
        RED = "\033[91m"
        RESET = "\033[0m"
        print(f"{RED}Error: {self.message}{RESET}")
