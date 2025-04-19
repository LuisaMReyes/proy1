from __future__ import annotations

from typing import List
from datetime import date
from library.categories.category import Category
from library.helpers.status import Status
from library.people.author import Author
#from library.copies.


class Book:

    _next_ido=1
    _books=[]
    def __init__(
            self,
            genre:str,
            title:str,
            edition:str,
            publication_date:date,
            publisher:str,
            authors:List[Author],
            ISBN:str,
            language:str,
            #available_copies:copies,
            status:Status,
            categories:List[Category]=[],
         ):
         self.genre=genre
         self.title=title
         self.edition=edition
         self.publication_date=publication_date
         self.publisher=publisher
         self.authors=authors
         self.ISBN=ISBN
         self.language=language
         #self.available_copies=available_copies
         self.status=status
         self.categories=categories

    def __str__(self) -> str:
     authors_str="\n".join(str(author)for author in self.authors )
     categories_str="\n".join(str(category)for category in self.categories)

     return(
         f"Título:{self.title}\n"
         f"Autor(es):\n{authors_str}\n"
         f"Género:{self.genre}\n"
         f"Edicion:{self.edition}\n"
         f"Fecha de publicacion:{self.publication_date.strftime('%d/%m/%Y')}\n"
         f"Editorial:{self.publisher}\n"
         f"ISBN:{self.ISBN}\n"
         f"Idioma:{self.language}\n"
         f"Categorías:\n{categories_str}\n"
         f"Estado:{self.status.value}\n"
        )
    @classmethod
    def register(
       cls,
       genre:str,
       title:str,
       edition:str,
       publication_date:date,
       publisher:str,
       authors:List[Author],
       ISBN:str,
       language:str,
       #available_copies:copies,
       status:Status,
       categories:List[Category]=[],

    )->bool:
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
         #available_copies=available_copies,
                status=status,
                categories=categories,
       )
       cls._books.append(new_book)
       return True
    
    @classmethod
    def get_book_by_ISBN(cls, ISBN:str)->Book|None:
       for book in cls._books:
          if book.ISBN==ISBN:
            return book
       return None

       

         
        
        
        
    