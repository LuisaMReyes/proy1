from __future__ import annotations

from datetime import date, timedelta
from typing import List
from library.helpers.item_type import ProductType


class Loan:

    next_id = 1
    _loans: List[Loan] = []

    def __init__(
        self,
        loan_id: str,
        product_type: ProductType,
        product_id: str,
        reader_id: str,
        days: int,
        loan_date: date,
        active: bool,
    ):
        self.loan_id = loan_id
        self.product_type = product_type
        self.product_id = product_id
        self.reader_id = reader_id
        self.days = days
        self.loan_date = loan_date
        self.estimated_return_date= self.calculate_return_date()
        self.active = active

    def calculate_return_date(self) -> date:
        return self.loan_date + timedelta(days=self.days)

    def register(
        self,
        loan_id: str,
        product_type: ProductType,
        product_id: str,
        reader_id: str,
        days: int,
        loan_date: date,
    ) -> bool:
        if self.get_by_id(loan_id):
            return False
        new_loan = Loan(
            loan_id,
            product_type,
            product_id,
            reader_id,
            days,
            loan_date,
            active=True,
        )
        self._loans.append(new_loan)
        return True

    @classmethod
    def get_by_id(cls, loan_id: str) -> Loan | None:
        for loan in cls._loans:
            if loan.loan_id == loan_id:
                return loan
        return None

    @classmethod
    def get_by_reader_id(cls, reader_id: str, onlyActive: bool = True) -> List[Loan]:
        matching_loans = []
        for loan in cls._loans:
            if loan.reader_id == reader_id:
                if onlyActive:
                    if loan.active:
                        matching_loans.append(loan)
                else:
                    matching_loans.append(loan)
        return matching_loans

    @classmethod
    def get_all(cls) -> List[Loan]:
        return cls._loans

    def cancel(self, loan_id: str) -> bool:
        loan = self.get_by_id(loan_id)
        if not loan:
            return False
        loan.active = False
        return True
