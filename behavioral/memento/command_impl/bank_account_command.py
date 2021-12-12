from behavioral.memento.bank_account import BankAccount
from behavioral.memento.command import Command


class BankAccountCommand(Command):
    """
    The BankAccountCommand class implements methods of Command interface in order to interact with BankAccount.
    """
    def __init__(self, account: BankAccount, action: BankAccount.Action, amount: int) -> None:
        super().__init__()
        self._account = account
        self.action = action
        self.amount = amount

    def execute(self) -> None:
        self._backup()
        success = False
        if self.action == BankAccount.Action.DEPOSIT:
            success = self._account.deposit(self.amount)
        elif self.action == BankAccount.Action.WITHDRAW:
            success = self._account.withdraw(self.amount)
        if not success:
            self.undo()

    def undo(self) -> None:
        if not len(self._snapshots):
            print(f"                                     "
                  f"Nothing to undo")
            return
        snapshot = self._snapshots.pop()
        snapshot.restore()
        print(f"                                     "
              f"Restored snapshot: {snapshot.get_name()}")

    def _backup(self) -> None:
        snapshot = self._account.save()
        print(f"                                     "
              f"Saved snapshot: {snapshot.get_name()}")

        self._snapshots.append(snapshot)
