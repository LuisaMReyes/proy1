from __future__ import annotations
from typing import List
from library.helpers.copy_status import Copy_status
from library.helpers.error import ErrorType,ErrorManager

class Copies:

    _copies=List["Copies"]=[]
    def __init__(
            self,
            copy_ID:str,
            ISBN:str,
            status:Copy_status,
    ):
        self.copy_ID=copy_ID
        self.ISBN=ISBN
        self.status=status
    def __str__(self) -> str:
        return(
            f"Identificador:{self.copy_ID}\n"
            f"ISBN:{self.ISBN}\n"
            f"Estado:{self.status.value}\n"
        )
    
    @classmethod
    def register(
        cls,
        copy_ID:str,
        ISBN:str,
        status:Copy_status,
    )->bool:
        if cls.get_copy_by_id(copy_ID):
            ErrorManager(ErrorType.COPY_ALREADY_EXISTS)
            return False
        new_copy=cls(
            copy_ID=copy_ID,
            ISBN=ISBN,
            status=status,
        )
        cls._copies.append(new_copy)
        return True
    
    @classmethod
    def get_copy_by_id(cls, copy_ID:str)-> Copies|None:
        for copy in cls._copies:
            if copy.copy_ID==copy_ID:
                return copy
        return None
    
    @classmethod
    def get_copy_by_ISBN(cls,ISBN:str)->List["Copies"]:
        copies= [copy for copy in cls._copies if copy.ISBN==ISBN]
        if not copies:
            ErrorManager(ErrorType.NO_COPIES_FOR_BOOK)
        return copies
    
    @classmethod
    def delete_copy(cls,copy_ID:str)->bool:
        copy=cls.get_copy_by_id(copy_ID)
        if copy :
            cls._copies.remove(copy)
            return True
        else:
         ErrorManager(ErrorType.COPY_NOT_FOUND)
         return False
    @classmethod
    def update_copy_status(self,new_status:Copy_status)->None:
        self.status=new_status




        