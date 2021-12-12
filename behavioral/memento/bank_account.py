from enum import Enum

from behavioral.memento.memento_impl.bank_account_snapshot import BankAccountSnapshot


class BankAccount:
    """
    The BankAccount class contains some important business logic. They know how to
    perform all kinds of operations (like deposit/withdraw).
    """
    class Action(Enum):
        """
        Enum is responsible for containing possible types of actions on bank account.
        """
        DEPOSIT = 0
        WITHDRAW = 1

    OVERDRAFT_LIMIT = -500

    def __init__(self, balance: int = 0) -> None:
        self._balance = balance

    def _set_balance(self, balance: int) -> None:
        self._balance = balance

    def deposit(self, amount: int) -> bool:
        self._balance += amount
        print(f'Deposited {amount}, balance = {self._balance}')
        return True

    def withdraw(self, amount: int) -> bool:
        successful = False
        if self._balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self._balance -= amount
            print(f'Withdrew {amount}, balance = {self._balance}')
            successful = True

        return successful

    def save(self) -> BankAccountSnapshot:
        return BankAccountSnapshot(self, self._balance)

    def __str__(self) -> str:
        return f'Balance = {self._balance}'
