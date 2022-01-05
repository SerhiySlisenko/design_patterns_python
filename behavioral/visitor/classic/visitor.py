from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.visitor.classic.expressions import ValueExpression, AdditionExpression, SubtractionExpression, \
        MultiplicationExpression


class Visitor(ABC):
    """
    The Visitor Interface declares a set of visiting methods that correspond to component classes.
    The signature of a visiting method allows the visitor to identify the exact class of the component
    that it's dealing with.
    """

    @abstractmethod
    def visit_value(self, element: ValueExpression) -> None:
        pass

    @abstractmethod
    def visit_addition_expr(self, element: AdditionExpression) -> None:
        pass

    @abstractmethod
    def visit_subtraction_expr(self, element: SubtractionExpression) -> None:
        pass

    @abstractmethod
    def visit_multiplication_expr(self, element: MultiplicationExpression) -> None:
        pass
