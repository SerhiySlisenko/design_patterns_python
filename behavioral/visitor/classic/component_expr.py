from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.visitor.classic.visitor import Visitor


class ComponentExpression(ABC):
    """
    The Component interface declares an `accept` method that should take the base visitor interface as an argument.
    """

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass
