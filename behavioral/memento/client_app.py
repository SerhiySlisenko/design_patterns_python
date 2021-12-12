from behavioral.memento.bank_account import BankAccount
from behavioral.memento.command_impl.bank_account_command import BankAccountCommand


def main() -> None:
    """
    Client app
    """
    ba = BankAccount()
    print(f"Init value: {ba}, Overdraft limit = {ba.OVERDRAFT_LIMIT}\n")
    deposit = BankAccountCommand(ba, BankAccount.Action.DEPOSIT, 1000)
    print("Make 1000$ deposit twice.")
    deposit.execute()
    deposit.execute()
    print(f"Result: {ba}\n")
    print("Undo a deposit once.")
    deposit.undo()
    print(f"Result: {ba}\n")

    print("Undo a deposit. This time twice twice.")
    deposit.undo()
    print(f"Result after first undo: {ba}")
    deposit.undo()
    print(f"Result after second undo: {ba}\n")

    print("Make 1000$ deposit once.")
    deposit.execute()
    print(f"Result after deposit: {ba}\n")

    wc = BankAccountCommand(ba, BankAccount.Action.WITHDRAW, 1000)
    print("Make 1000$ withdrawal once.")
    wc.execute()
    print(f"Result after withdrawal: {ba}\n")
    print("Undo a withdrawal. This time twice twice.")
    wc.undo()
    print(f"Result after first undo: {ba}")
    wc.undo()
    print(f"Result after second undo: {ba}\n")
    print('='*50)


if __name__ == '__main__':
    main()
