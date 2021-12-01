from typing import List

from behavioral.command.command import Command
from behavioral.command.commands.bank_account_command import BankAccountCommand


class CompositeBankAccountCommand(Command, list):
    """
    The CompositeBankAccountCommand class implements a mechanism to execute several commands in a row.
    """
    def __init__(self, commands: List[BankAccountCommand]) -> None:
        super().__init__()
        for command in commands:
            self.append(command)

    def execute(self) -> None:
        for command in self:
            command.execute()

    def undo(self) -> None:
        for command in reversed(self):
            command.undo()
