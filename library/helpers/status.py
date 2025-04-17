from enum import Enum


class Status(Enum):
    AVAILABLE = "Disponible"
    BORROWED = "Prestado"
    IN_LIBRARY = "En biblioteca"
    UNDER_REVIEW = "En revisión"
    UNDER_REPAIR = "En reparación"
    UNAVAILABLE = "No disponible"
