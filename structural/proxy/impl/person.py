from __future__ import annotations
from abc import ABC, abstractmethod


class Person(ABC):
    """
    The Person interface declares common operations for both RealPerson and
    the ProxyPerson. As long as the client works with RealPerson using this
    interface, you'll be able to pass it a proxy person instead of a real person.
    """
    @abstractmethod
    def drink(self) -> str:
        pass

    @abstractmethod
    def drive(self) -> str:
        pass

    @abstractmethod
    def drink_and_drive(self) -> str:
        pass
