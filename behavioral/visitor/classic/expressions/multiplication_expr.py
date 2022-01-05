from __future__ import annotations
from typing import TYPE_CHECKING

from behavioral.visitor.classic.component_expr import ComponentExpression

if TYPE_CHECKING:
    from behavioral.visitor.classic.visitor import Visitor


class MultiplicationExpression(ComponentExpression):
    """
    Demonstrates multiplication expression. Expression is not supposed to be executed in this class directly in any way.
    """
    def __init__(self, left: ComponentExpression, right: ComponentExpression) -> None:
        self.right = right
        self.left = left
        self.sign = '*'

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_multiplication_expr(self)
