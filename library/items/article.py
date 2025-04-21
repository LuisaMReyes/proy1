from __future__ import annotations

from typing import List
from datetime import date
from library.categories.category import Category
from library.helpers.item_status import ItemStatus
from library.people.author import Author


class Article:
    """
    Clase que representa un artículo científico con sus atributos correspondientes.
    """

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
        status: ItemStatus,
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
        status: ItemStatus,
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

    @classmethod
    def get_all_articles(cls) -> List[Article]:
        return cls._articles

    def update_article(
        self,
        new_doi: str | None = None,
        new_title: str | None = None,
        new_publisher_name: str | None = None,
        new_publication_date: date | None = None,
        new_journal: str | None = None,
        new_periodicity: str | None = None,
        new_volume: str | None = None,
        new_field: str | None = None,
        new_status: ItemStatus | None = None,
        new_authors: List[Author] | None = None,
        new_categories: List[Category] | None = None,
    ) -> None:

        if self.status != ItemStatus.AVAILABLE:
            print("No se puede modificar un artículo inhabilitado .")
            return
        if new_doi:
            self.doi = new_doi
        if new_title:
            self.title = new_title
        if new_publisher_name:
            self.publisher_name = new_publisher_name
        if new_publication_date:
            self.publication_date = new_publication_date
        if new_journal:
            self.journal = new_journal
        if new_periodicity:
            self.periodicity = new_periodicity
        if new_volume:
            self.volume = new_volume
        if new_field:
            self.field = new_field
        if new_status:
            self.status = new_status
        if new_authors:
            self.authors = new_authors
        if new_categories:
            self.categories = new_categories

    @classmethod
    def delete_article(cls, doi: str) -> bool:
        article = cls.get_article_by_doi(doi)
        if article:
            cls._articles.remove(article)
            return True
        return False
