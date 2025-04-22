from __future__ import annotations

from typing import List
from library.fines.fine import Fine
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

    @classmethod
    def create(
        cls, reader_id: str, name: str, phone: str, address: str, status: ReaderStatus
    ) -> bool:
        if cls.get_by_id(reader_id):
            return False

        new_reader = Reader(reader_id, name, phone, address, status)
        cls._readers.append(new_reader)
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

    @classmethod
    def set_status(cls, reader_id: str, status: ReaderStatus) -> bool:
        reader = cls.get_by_id(reader_id)
        if not reader:
            return False
        reader.status = status
        return True

    @classmethod
    def get_all(cls) -> List[Reader]:
        return cls._readers

    @classmethod
    def get_by_id(cls, reader_id: str) -> Reader | None:
        for reader in cls._readers:
            if reader.reader_id == reader_id:
                return reader
        return None

    @classmethod
    def get_active_loans(cls, reader_id: str) -> List[Loan]:
        return Loan.get_by_reader_id(reader_id)

    @classmethod
    def can_borrow(cls, reader_id: str) -> bool:
        reader = cls.get_by_id(reader_id)
        if not reader:
            return False
        return (
            len(cls.get_active_loans(reader_id)) < 3
            and reader.status == ReaderStatus.NORMAL
        )

    @classmethod
    def get_fines(cls, reader_id: str) -> List[Fine]:
        return Fine.get_fines_by_reader_id(reader_id)
