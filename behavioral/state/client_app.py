from behavioral.state.lock_context import LockContext


def main() -> None:
    """
    Client app
    """
    key_menu: str = ""
    password = [1, 2, 3, 4]
    context: LockContext = LockContext(password)

    while key_menu != "Q":
        print("   1 - Enter digit")
        print("   2 - Reset trial pass")
        print("   3 - Set new password")
        print("   Q - exit")
        print("   Please, select menu point.")
        key_menu = str(input()).upper()

        if key_menu == "1":
            digit = int(input("Enter your digit: "))
            context.enter_digit(digit)
        elif key_menu == "2":
            context.reset_lock()
        elif key_menu == "3":
            new_pass = []
            length = int(input("Enter length of password: "))
            for digit in range(length):
                new_pass.append(int(input("Enter your digit: ")))

            context.set_new_password(new_pass)


if __name__ == '__main__':
    main()
