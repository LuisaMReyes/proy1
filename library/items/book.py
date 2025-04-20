from __future__ import annotations

from typing import List
from datetime import date
from library.categories.category import Category
from library.copies.copies import Copies
from library.helpers.item_status import ItemStatus
from library.people.author import Author



class Book:

    _next_ido = 1
    _books = []

    def __init__(
        self,
        genre: str,
        title: str,
        edition: str,
        publication_date: date,
        publisher: str,
        authors: List[Author],
        ISBN: str,
        language: str,
        status: ItemStatus,
        categories: List[Category] = [],
    ):
        self.genre = genre
        self.title = title
        self.edition = edition
        self.publication_date = publication_date
        self.publisher = publisher
        self.authors = authors
        self.ISBN = ISBN
        self.language = language
        self.status = status
        self.categories = categories

    def __str__(self) -> str:
        authors_str = "\n".join(str(author) for author in self.authors)
        categories_str = "\n".join(str(category) for category in self.categories)
        copias=Copies.get_copy_by_ISBN(self.ISBN)
        available_copies=len(copias)

        return (
            f"Título:{self.title}\n"
            f"Autor(es):\n{authors_str}\n"
            f"Género:{self.genre}\n"
            f"Edicion:{self.edition}\n"
            f"Fecha de publicacion:{self.publication_date.strftime('%d/%m/%Y')}\n"
            f"Editorial:{self.publisher}\n"
            f"ISBN:{self.ISBN}\n"
            f"Idioma:{self.language}\n"
            f"Número de copias disponibles:{available_copies}\n"
            f"Categorías:\n{categories_str}\n"
            f"Estado:{self.status.value}\n"
        )

    @classmethod
    def register(
        cls,
        genre: str,
        title: str,
        edition: str,
        publication_date: date,
        publisher: str,
        authors: List[Author],
        ISBN: str,
        language: str,
        # available_copies:copies,
        status: ItemStatus,
        categories: List[Category] = [],
    ) -> bool:
        if cls.get_book_by_ISBN(ISBN):
            return False
        new_book = cls(
            genre=genre,
            title=title,
            edition=edition,
            publication_date=publication_date,
            publisher=publisher,
            authors=authors,
            ISBN=ISBN,
            language=language,
            # available_copies=available_copies,
            status=status,
            categories=categories,
        )
        cls._books.append(new_book)

        #Debe registrarse al menos 1 copia
        Copies.register(
            copy_ID=f"Copia_{ISBN}_1",
            ISBN=ISBN,
            status=ItemStatus.AVAILABLE
        )





        return True

    @classmethod
    def get_book_by_ISBN(cls, 
                         ISBN: str,
                         ) -> Book | None:
        for book in cls._books:
            if book.ISBN == ISBN:
                return book
        return None
    def update_book(
            self,
            new_genre:str=None,
            new_title:str=None,
            new_edition:str=None,
            new_publication_date:date=None,
            new_publisher:str=None,
            new_authors:List[Author]=None,
            new_language:str=None,
            new_status:ItemStatus=None,
            new_categories:List[Category]=None,
    )-> None:
         if new_genre:
            self.genre=new_genre
         if new_title:
            self.title=new_title
         if new_edition:
            self.edition=new_edition
         if new_publication_date:
            self.publication_date=new_publication_date
         if new_publisher:
            self.publisher=new_publisher
         if new_authors:
            self.authors=new_authors  
         if new_language:
            self.language=new_language
         if new_status:
            self.status=new_status
         if new_categories:
            self.categories=new_categories
  
    def disable_book(self)->None:
        self.status=ItemStatus.UNAVAILABLE


