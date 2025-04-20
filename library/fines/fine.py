from __future__ import annotations

from datetime import date, timedelta
from typing import List
from library.helpers.item_type import ProductType
from library.helpers.fine_status import Fine_Status
from library.loans.loan import Loan

class Fine:
    next_id=1
    _fines:List[Fine]=[]

    def __init__(
        self,
        loan:Loan,
        real_delivery_date:date,
        
    ):
        #Crea ID unica para la multa
        self.id_fine= f"FINE_{Fine.next_id}"
        Fine.next_id+=1#Aumenta cada vez que se crea una nueva multa
        self.loan=loan
        self.real_delivery_date=real_delivery_date

        self.delay_days=0
        self.fine_days=0
        self.start_date=None
        self.end_date=None
        self.status=Fine_Status.INACTIVE
        
        Fine._fines.append(self)
    
    def calculate_delay_days(self)->int:
        start_count=self.loan.estimated_return_date+timedelta(days=1)
        delay=(self.real_delivery_date- start_count).days
        self.delay_days=max(0,delay)
        return self.delay_days
    @classmethod
    def generate_fine(
        cls,
        loan:Loan,
        real_delivery_date:date,
    )->Fine:
        
        fine=Fine(loan,real_delivery_date)
        fine.calculate_delay_days()

        if fine.delay_days >0:
            fine.fine_days=fine.delay_days*3
            fine.start_date=date.today()
            fine.end_date=fine.start_date+timedelta(days=fine.fine_days)
            fine.status=Fine_Status.ACTIVE
        return fine
    @classmethod
    def lift_fine(
        cls,
        fine_id:str,
    )->bool:
        for fine in cls._fines:
            if fine.id_fine==fine_id and fine.status==Fine_Status.ACTIVE:
                if fine.end_date and date.today()>=fine.end_date:
                    fine.status=Fine_Status.INACTIVE
                    return True
        return False
    @classmethod
    def lift_fine_Auto(
        cls,
        current_date:date=None,
        )->None:
        if current_date is None:
            current_date=date.today()

        for fine in cls._fines:
            if fine.status==Fine_Status.ACTIVE and fine.end_date and current_date>=fine.end_date:
                fine.status=Fine_Status.INACTIVE
    
    
    def __str__(self)->str:
        return(
            f"ID Multa:{self.id_fine}\n"
            f"ID Préstamo :{self.loan.loan_id}\n"
            f"Fecha de entrega real:{self.real_delivery_date.strftime('%d/%m/%Y')}\n"
            f"Días de retraso:{self.delay_days}\n"
            f"Días de multa:{self.fine_days}\n"
            f"Fecha de inicio de la multa:{self.start_date.strftime('%d/%m/%Y') if self.start_date else 'NO iniciada'}\n"
            f"Fecha final de la multa:{self.end_date.strftime('%d/%m/%Y')if self.end_date else 'No finalizada'}\n"
            f"Estado:{self.status.value}\n"

        )
    @classmethod
    def get_all_fines(cls)->List[Fine]:
        return cls._fines
    @classmethod
    def get_active_fines(cls)->List[Fine]:
        return [fine for fine in cls._fines if fine.status==Fine_Status.ACTIVE]
    
    @classmethod
    def get_inactive_fines(cls)->List[Fine]:
        return [fine for fine in cls._fines if fine.status==Fine_Status.INACTIVE]
