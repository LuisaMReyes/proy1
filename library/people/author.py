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
        return f"ID: {self.author_id}\n" f"Nombre: {self.name}\n"

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

    def get_authors(self):
        return self._authors
