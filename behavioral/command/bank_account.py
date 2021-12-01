from enum import Enum


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
        self.balance = balance

    def deposit(self, amount: int) -> bool:
        self.balance += amount
        print(f'Deposited {amount}, balance = {self.balance}')
        return True

    def withdraw(self, amount: int) -> bool:
        successful = False
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Withdrew {amount}, balance = {self.balance}')
            successful = True

        return successful

    def __str__(self) -> str:
        return f'Balance = {self.balance}'
