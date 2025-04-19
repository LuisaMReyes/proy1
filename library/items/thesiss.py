from __future__ import annotations

from typing import List
from datetime import date
from library.categories.category import Category
from library.helpers.status import Status
from library.people.author import Author
#from library.copies.

class Thesis:

    _next_id=1
    _theses=List["Thesis"]=[]
    def __init__(
            self,
            title:str,
            authors:List[Author],
            academy:str,
            investi_date:date,
            publication_date:date,
            field:str,
            page_number:int,
            status:Status,
            categories:List[Category],
            #copies?
            ):
        self.title=title
        self.authors=authors
        self.academy=academy
        self.investi_date=investi_date
        self.publication_date=publication_date
        self.field=field
        self.page_number=page_number
        self.status=status
        self.categories=categories
    def __str__(self)->str:
     authors_str="\n".join(str(author)for author in self.authors)
     categories_str="\n".join(str(category)for category in self.categories)

     return(
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
        title:str,
        authors:List[Author],
        academy:str,
        investi_date:date,
        publication_date:date,
        field:str,
        page_number:int,
        status:Status,
        categories:List[Category],
            #copies?
        
    )->bool:
       new_thesis=cls(
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
    def get_thesis_by_author(cls,author_name:str)->List["Thesis"]:
       result=[]
       for thesis in cls._theses:
          if any(author_name.lower() in author.name.lower() for author in thesis.authors):
             result.append(thesis)
       return result



       
   
