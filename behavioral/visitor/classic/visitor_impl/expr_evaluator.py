from behavioral.visitor.classic.visitor import Visitor
from behavioral.visitor.classic.expressions.value_expr import ValueExpression
from behavioral.visitor.classic.expressions import AdditionExpression, SubtractionExpression, \
    MultiplicationExpression


class ExpressionEvaluator(Visitor):
    """
    ExpressionEvaluator Visitor. Supports the execution of the expression.
    """
    def __init__(self) -> None:
        self.value = None

    def visit_value(self, element: ValueExpression) -> None:
        self.value = element.value

    def visit_addition_expr(self, element: AdditionExpression) -> None:
        element.left.accept(self)  # instead of `self.visit(element.left)`
        temp = self.value
        element.right.accept(self)  # instead of `self.visit(element.right)`
        self.value += temp

    def visit_subtraction_expr(self, element: SubtractionExpression) -> None:
        element.right.accept(self)
        temp = self.value
        element.left.accept(self)
        self.value -= temp

    def visit_multiplication_expr(self, element: MultiplicationExpression) -> None:
        element.left.accept(self)
        temp = self.value
        element.right.accept(self)
        self.value *= temp

    def __str__(self) -> str:
        return str(self.value)
