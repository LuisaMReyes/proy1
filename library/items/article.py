from __future__ import annotations

from typing import List
from datetime import date
from library.categories.category import Category
from library.helpers.status import Status
from library.people.author import Author


class Article:
    """
    Clase que representa un artículo científico con sus atributos correspondientes.
    """

    # Variable de clase para mantener el contador de IDs
    _next_id = 1
    # Lista para almacenar todos los artículos
    _articles = []

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
        categories: List[Category] = [],
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
        self.categories = categories

    def __str__(self) -> str:
        """
        Retorna una representación en string del artículo con formato legible
        incluyendo título, autores, journal y otros detalles relevantes.
        """
        authors_str = "\n".join(str(author) for author in self.authors)
        categories_str = "\n".join(str(category) for category in self.categories)

        return (
            f"Título: {self.title}\n"
            f"Autores: \n{authors_str}\n"
            f"Journal: {self.journal} ({self.volume})\n"
            f"DOI: {self.doi}\n"
            f"Publicado: {self.publication_date.strftime('%d/%m/%Y')}\n"
            f"Campo: {self.field}\n"
            f"Estado: {self.status.value}"
            f"Categorías: \n{categories_str}\n"
        )

    @classmethod
    def create(
        cls,
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
        categories: List[Category] = [],
    ) -> bool:
        # Verificar que el DOI no exista ya
        if cls.get_article_by_doi(doi):
            return False

        # Crear nueva instancia
        new_article = cls(
            doi=doi,
            title=title,
            publisher_name=publisher_name,
            publication_date=publication_date,
            journal=journal,
            periodicity=periodicity,
            volume=volume,
            field=field,
            status=status,
            authors=authors,
            categories=categories,
        )

        # Agregar a la lista de artículos
        cls._articles.append(new_article)
        return True

    @classmethod
    def get_article_by_doi(cls, doi: str) -> Article | None:
        for article in cls._articles:
            if article.doi == doi:
                return article
        return None
