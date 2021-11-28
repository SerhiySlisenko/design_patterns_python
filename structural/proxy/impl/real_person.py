from __future__ import annotations
from .person import Person


class RealPerson(Person):
    """
    The RealPerson contains some core business logic.
    """
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def drink(self) -> str:
        return f'{self.name} is drinking.'

    def drive(self) -> str:
        return f'{self.name} is driving.'

    def drink_and_drive(self) -> str:
        return f'{self.name} is drunk driving.'
