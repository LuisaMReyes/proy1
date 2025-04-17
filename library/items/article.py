from typing import List
from datetime import date
from library.helpers.status import Status
from library.people.author import Author


class Article:
    """
    Clase que representa un artículo científico con sus atributos correspondientes.
    """

    def __init__(
        self,
        doi: str,
        title: str,
        publisher_name: str,
        publication_date: date,
        journal: str,
        periodicity: str,
        volume: str,
        field: str,
        status: Status,
        authors: List[Author],
    ):
        self.doi = doi
        self.title = title
        self.publisher_name = publisher_name
        self.publication_date = publication_date
        self.journal = journal
        self.periodicity = periodicity
        self.volume = volume
        self.field = field
        self.status = status
        self.authors = authors

    def __str__(self) -> str:
        """
        Retorna una representación en string del artículo con formato legible
        incluyendo título, autores, journal y otros detalles relevantes.
        """
        authors_str = "\n".join(str(author) for author in self.authors)
        return (
            f"Título: {self.title}\n"
            f"Autores: \n{authors_str}\n"
            f"Journal: {self.journal} ({self.volume})\n"
            f"DOI: {self.doi}\n"
            f"Publicado: {self.publication_date.strftime('%d/%m/%Y')}\n"
            f"Campo: {self.field}\n"
            f"Estado: {self.status.value}"
        )
