from __future__ import annotations
from typing import TYPE_CHECKING

from behavioral.visitor.classic.component_expr import ComponentExpression

if TYPE_CHECKING:
    from behavioral.visitor.classic.visitor import Visitor


class ValueExpression(ComponentExpression):
    """
    Demonstrates a single value that actually can be treated as expression.
    """
    def __init__(self, value: int) -> None:
        self.value = value

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_value(self)
