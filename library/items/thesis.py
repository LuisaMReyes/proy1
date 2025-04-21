from __future__ import annotations

from typing import List
from datetime import date
from library.categories.category import Category
from library.helpers.item_status import ItemStatus
from library.people.author import Author


class Thesis:

    _theses: List[Thesis] = []
    _counter: int = 1

    def __init__(
        self,
        title: str,
        authors: List[Author],
        academy: str,
        investi_date: date,
        publication_date: date,
        field: str,
        page_number: int,
        status: ItemStatus,
        categories: List[Category],
    ):
        # Generar código único
        year = publication_date.year
        code = f"TESIS-{year}-{Thesis._counter:03d}"
        Thesis._counter += 1
        self.code = code
        self.title = title
        self.authors = authors
        self.academy = academy
        self.investi_date = investi_date
        self.publication_date = publication_date
        self.field = field
        self.page_number = page_number
        self.status = status
        self.categories = categories

    def __str__(self) -> str:
        authors_str = "\n".join(str(author) for author in self.authors)
        categories_str = "\n".join(str(category) for category in self.categories)

        return (
            f"Código:{self.code}\n"
            f"Título:{self.title}\n"
            f"Autor(es):\n{authors_str}\n"
            f"Institución académica:{self.academy}\n"
            f"Fecha de investigación:{self.investi_date.strftime('%d/%m/%Y')}\n"
            f"Fecha de publicacion:{self.publication_date.strftime('%d/%m/%Y')}\n"
            f"Campo:{self.field}\n"
            f"Número de páginas:{self.page_number}\n"
            f"Estado:{self.status.value}\n"
            f"Categorías:\n{categories_str}\n"
        )

    @classmethod
    def register(
        cls,
        title: str,
        authors: List[Author],
        academy: str,
        investi_date: date,
        publication_date: date,
        field: str,
        page_number: int,
        status: ItemStatus,
        categories: List[Category],
    ) -> bool:
        if cls.get_specific_thesis(authors, academy, investi_date, publication_date):
            return False

        new_thesis = cls(
            title=title,
            authors=authors,
            academy=academy,
            investi_date=investi_date,
            publication_date=publication_date,
            field=field,
            page_number=page_number,
            status=status,
            categories=categories,
        )
        cls._theses.append(new_thesis)
        return True

    @classmethod
    def get_all_theses(cls) -> List[Thesis]:
        return cls._theses

    @classmethod
    def get_thesis_by_author(
        cls,
        author_name: str,
    ) -> List[Thesis]:
        result = []
        for thesis in cls._theses:
            if any(
                author_name.lower() in author.name.lower() for author in thesis.authors
            ):
                result.append(thesis)
        return result

    @classmethod
    def get_thesis_by_code(cls, code: str) -> Thesis | None:
        for thesis in cls._theses:
            if thesis.code == code:
                return thesis
        return None

    @classmethod
    def get_specific_thesis(
        cls,
        authors: List[Author],
        academy: str,
        investi_date: date,
        publication_date: date,
    ) -> Thesis | None:
        for thesis in cls._theses:
            if (
                set(thesis.authors) == set(authors)
                and thesis.academy.lower() == academy.lower()
                and thesis.investi_date == investi_date
                and thesis.publication_date == publication_date
            ):
                return thesis
        return None

    def update_thesis(
        self,
        new_title: str | None = None,
        new_authors: List[Author] | None = None,
        new_academy: str | None = None,
        new_investi_date: date | None = None,
        new_publication_date: date | None = None,
        new_field: str | None = None,
        new_page_number: int | None = None,
        new_status: ItemStatus | None = None,
        new_categories: List[Category] | None = None,
    ) -> None:
        if self.status != ItemStatus.AVAILABLE:
            print("No se puede modificar una tesis inhabilitada .")
            return
        if new_title:
            self.title = new_title
        if new_authors:
            self.authors = new_authors
        if new_academy:
            self.academy = new_academy
        if new_investi_date:
            self.investi_date = new_investi_date
        if new_publication_date:
            self.publication_date = new_publication_date
        if new_field:
            self.field = new_field
        if new_page_number:
            self.page_number = new_page_number
        if new_status:
            self.status = new_status
        if new_categories:
            self.categories = new_categories

    @classmethod
    def delete_thesis(
        cls,
        authors: List[Author],
        academy: str,
        investi_date: date,
        publication_date: date,
    ) -> bool:
        thesis = cls.get_specific_thesis(
            authors, academy, investi_date, publication_date
        )
        if thesis:
            cls._theses.remove(thesis)
            return True
        return False
