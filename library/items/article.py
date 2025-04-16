from typing import List
from datetime import date


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
        status: str,
        authors: List[str],
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
        """retornamos una representación en string del artículo"""
        return (
            f"{self.title} - {', '.join(self.authors)} ({self.publication_date.year})"
        )

    def get_citation(self) -> str:
        """retornamos la cita del artículo en formato APA"""
        authors_citation = ", ".join(self.authors[:-1])
        if len(self.authors) > 1:
            authors_citation += f" & {self.authors[-1]}"
        elif len(self.authors) == 1:
            authors_citation = self.authors[0]

        return f"{authors_citation}. ({self.publication_date.year}). {self.title}. {self.journal}, {self.volume}. {self.doi}"
