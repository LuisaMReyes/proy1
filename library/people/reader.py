from __future__ import annotations

from typing import List
from library.helpers.reader_status import ReaderStatus
from library.loans.loan import Loan


class Reader:
    _readers: List[Reader] = []

    def __init__(
        self, reader_id: str, name: str, phone: str, address: str, status: ReaderStatus
    ):
        self.reader_id = reader_id
        self.name = name
        self.phone = phone
        self.address = address
        self.status = status

    def create(
        self, reader_id: str, name: str, phone: str, address: str, status: ReaderStatus
    ) -> bool:
        if self.get_by_id(reader_id):
            return False

        new_reader = Reader(reader_id, name, phone, address, status)
        self._readers.append(new_reader)
        return True

    def modify(
        self,
        reader_id: str,
        name: str | None = None,
        phone: str | None = None,
        address: str | None = None,
    ) -> bool:
        reader = self.get_by_id(reader_id)
        if not reader:
            return False

        if name:
            reader.name = name
        if phone:
            reader.phone = phone
        if address:
            reader.address = address
        return True

    def set_status(self, reader_id: str, status: ReaderStatus) -> bool:
        reader = self.get_by_id(reader_id)
        if not reader:
            return False
        reader.status = status
        return True

    def get_all(self) -> List[Reader]:
        return self._readers

    def get_by_id(self, reader_id: str) -> Reader | None:
        for reader in self._readers:
            if reader.reader_id == reader_id:
                return reader
        return None

    def get_active_loans(self) -> List[Loan]:
        return Loan.get_by_reader_id(self.reader_id)

    def can_borrow(self, reader_id: str) -> bool:
        reader = self.get_by_id(reader_id)
        if not reader:
            return False
        return len(self.get_active_loans()) < 3 and reader.status == ReaderStatus.NORMAL

    # def add_loan(self, reader_id: str) -> bool:
    #     reader = self.get_by_id(reader_id)
    #     if not reader or not self.can_borrow(reader_id):
    #         return False
    #     reader.active_loans += 1
    #     return True
