from __future__ import annotations

from datetime import date, timedelta
from typing import List
from library.helpers.item_type import ProductType
from library.loans.loan import Loan

class Fine:
    next_id=1
    _fines:List[Fine]=[]

    def __init__(
        self,
        id_fine: str,
        id_loan:str,
        real_delivery_date:date,
        delay_days:int,
        fine_days:int,
        start_date:date,
        end_date:date,
        active:bool,
    ):
        self.id_fine=id_fine
        self.id_loan=id_loan
        self.real_delivery_date=real_delivery_date
        self.delay_days=delay_days
        self.fine_days=fine_days
        self.start_date=start_date
        self.end_date=end_date
        self.active=active
