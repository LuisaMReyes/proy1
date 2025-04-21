from __future__ import annotations
from datetime import date


class Author:
    _authors = []

    def __init__(self, author_id: str, name: str, nationality: str, birth_date: date):
        self.author_id = author_id
        self.name = name
        self.nationality = nationality
        self.birth_date = birth_date

    def __str__(self):
        return (
            f"ID: {self.author_id}\n"
            f"Nombre: {self.name}\n"
            f"Nacionalidad: {self.nationality}\n"
            f"Fecha de nacimiento: {self.birth_date}\n"
        )

    @classmethod
    def create(
        cls, author_id: str, name: str, nationality: str, birth_date: date
    ) -> bool:
        if cls.get_author_by_id(author_id):
            return False

        new_author = Author(author_id, name, nationality, birth_date)
        cls._authors.append(new_author)
        return True

    @classmethod
    def get_author_by_id(cls, author_id) -> Author | None:
        for author in cls._authors:
            if author.author_id == author_id:
                return author
        return None

    @classmethod
    def get_authors(cls):
        return cls._authors

    @classmethod
    def patch_author(
        cls,
        author_id: str,
        name: str | None = None,
        nationality: str | None = None,
        birth_date: date | None = None,
    ) -> bool:
        author = cls.get_author_by_id(author_id)
        if not author:
            return False

        if name is not None:
            author.name = name
        if nationality is not None:
            author.nationality = nationality
        if birth_date is not None:
            author.birth_date = birth_date
        return True
