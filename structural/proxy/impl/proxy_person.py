from __future__ import annotations
from .person import Person
from .real_person import RealPerson


class ProxyPerson(Person):
    """
    The ProxyPerson has an interface identical to the RealPerson.
    But it can change the behavior of RealPerson without changing its code.
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self._person = RealPerson(name, age)

    def drink(self) -> str:
        return f'{self.name} is too young to drink.' if self.age < 18 else self._person.drink()

    def drive(self) -> str:
        return f'{self.name} is too young to drive.' if self.age < 16 else self._person.drive()

    def drink_and_drive(self) -> str:
        return 'Drunk driving is too dangerous!'
