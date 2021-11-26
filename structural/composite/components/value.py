from __future__ import annotations
from abc import ABC, abstractmethod


class Value(ABC):
    """
    The base Value class declares common operations for both simple and
    complex values of a composition.
    """

    def add(self, value: Value) -> None:
        pass

    def remove(self, value: Value) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def sum(self) -> int:
        pass
