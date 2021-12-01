from behavioral.command.bank_account import BankAccount
from behavioral.command.commands import BankAccountCommand, CompositeBankAccountCommand, MoneyTransferCommand


def main() -> None:
    """
    Client app
    """
    # Example 1: You have an account with zero balance, then add 1000 twice using the composite command.
    # Try to undo the command and check the results.
    ba = BankAccount()

    deposit1 = BankAccountCommand(ba, BankAccount.Action.DEPOSIT, 1000)
    deposit2 = BankAccountCommand(ba, BankAccount.Action.DEPOSIT, 1000)
    composite = CompositeBankAccountCommand([deposit1, deposit2])

    composite.execute()
    print(ba)
    composite.undo()
    print(ba)
    print('='*50)

    # Example 2: You have two accounts, try to transfer the money from one to another account using composite command.
    # Try to undo the command and check the results.
    ba1 = BankAccount(100)
    ba2 = BankAccount()
    amount = 1000  # no transactions should happen, but second is happened while do execute()

    wc = BankAccountCommand(ba1, BankAccount.Action.WITHDRAW, amount)
    dc = BankAccountCommand(ba2, BankAccount.Action.DEPOSIT, amount)
    transfer = CompositeBankAccountCommand([wc, dc])

    transfer.execute()
    print(f'BankAccount 1: {ba1}\nBankAccount 2: {ba2}')
    transfer.undo()
    print(f'BankAccount 1: {ba1}\nBankAccount 2: {ba2}')
    print('='*50)

    # Example 3: You have two accounts, try to transfer the money from one to another account using transfer command.
    # Try to undo the command and check the results. This time problems from previous example were handled correctly.
    ba1 = BankAccount(100)
    ba2 = BankAccount()
    amount = 1000

    transfer = MoneyTransferCommand(ba1, ba2, amount)

    transfer.execute()
    print(f'BankAccount 1: {ba1}\nBankAccount 2: {ba2}')
    transfer.undo()
    print(f'BankAccount 1: {ba1}\nBankAccount 2: {ba2}')
    print(transfer.success)


if __name__ == '__main__':
    main()
