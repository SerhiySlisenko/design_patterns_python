from __future__ import annotations

from typing import Callable

from subjects.connection import Connection


def is_singleton(class_name: Callable) -> bool:
    """
    Function to check if given class is type of Singleton
    """
    obj1 = class_name()
    obj2 = class_name()

    return obj1 == obj2 and obj1 is obj2


def main() -> None:
    """
    Client app
    """
    first_connection = Connection("elonmask777", 'tesla999')
    print(first_connection)
    second_connection = Connection("buterin", 'ethereum')
    print(second_connection)
    print(is_singleton(Connection))
    second_connection.connect()


if __name__ == '__main__':
    main()
