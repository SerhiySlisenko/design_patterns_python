from __future__ import annotations
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from behavioral.visitor.alternative_python.value import Value
    from behavioral.visitor.alternative_python.expressions import AdditionExpression, MultiplicationExpression


class SubtractionExpression:
    """
    Demonstrates subtraction expression. Expression is not supposed to be executed in this class directly in any way.
    """
    def __init__(self,
                 left: Union[Value, AdditionExpression, SubtractionExpression, MultiplicationExpression],
                 right: Union[Value, AdditionExpression, SubtractionExpression, MultiplicationExpression]
                 ) -> None:
        self.right = right
        self.left = left
        self.sign = '-'
