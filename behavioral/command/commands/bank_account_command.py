from behavioral.command.bank_account import BankAccount
from behavioral.command.command import Command


class BankAccountCommand(Command):
    """
    The BankAccountCommand class implements methods of Command interface in order to interact with BankAccount.
    """
    def __init__(self, account: BankAccount, action: BankAccount.Action, amount: int) -> None:
        super().__init__()
        self.amount = amount
        self.action = action
        self.account = account

    def execute(self) -> None:
        if self.action == BankAccount.Action.DEPOSIT:
            self.success = self.account.deposit(self.amount)
        elif self.action == BankAccount.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self) -> None:
        if self.success:
            # frankly speaking this is not correct to undo a deposit by withdrawing, but I used it to simplify
            if self.action == BankAccount.Action.DEPOSIT:
                self.account.withdraw(self.amount)
            elif self.action == BankAccount.Action.WITHDRAW:
                self.account.deposit(self.amount)
