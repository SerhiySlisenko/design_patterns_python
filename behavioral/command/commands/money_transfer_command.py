from behavioral.command.bank_account import BankAccount
from behavioral.command.commands.bank_account_command import BankAccountCommand
from behavioral.command.commands.composite_bank_account_command import CompositeBankAccountCommand


class MoneyTransferCommand(CompositeBankAccountCommand):
    """
    The MoneyTransferCommand class implements a mechanism to save money transfer
    between different accounts based on CompositeBankAccountCommand class.
    """
    def __init__(self, from_acct: BankAccount, to_acct: BankAccount, amount: int) -> None:
        super().__init__([
            BankAccountCommand(from_acct,
                               BankAccount.Action.WITHDRAW,
                               amount),
            BankAccountCommand(to_acct,
                               BankAccount.Action.DEPOSIT,
                               amount)])

    def execute(self) -> None:
        ok = True
        for command in self:
            if ok:
                command.execute()
                ok = command.success
            else:
                command.success = False
        self.success = ok
