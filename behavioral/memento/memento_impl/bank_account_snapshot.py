from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

from memento import Memento

if TYPE_CHECKING:
    from behavioral.memento.bank_account import BankAccount


class BankAccountSnapshot(Memento):
    """
    Concrete implementation of Memento class in order to save/restore BankAccount balance.
    """
    def __init__(self, bank_account: BankAccount, balance: int) -> None:
        self._bank_account = bank_account
        self._balance = balance
        self._date = str(datetime.now())[:19]

    def get_name(self) -> str:
        return f"{self._date} / BankAccount(balance={self._balance})"

    def get_date(self) -> str:
        return self._date

    def restore(self) -> None:
        self._bank_account._set_balance(self._balance)
