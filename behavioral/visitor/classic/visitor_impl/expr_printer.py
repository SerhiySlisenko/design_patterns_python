from behavioral.visitor.classic.visitor import Visitor
from behavioral.visitor.classic.expressions.value_expr import ValueExpression
from behavioral.visitor.classic.expressions import AdditionExpression, SubtractionExpression, \
    MultiplicationExpression


class ExpressionPrinter(Visitor):
    """
    ExpressionPrinter Visitor. Supports the printing of the expression.
    For addition and subtraction, parentheses are added.
    """
    def __init__(self) -> None:
        self.buffer = []

    def visit_value(self, element: ValueExpression) -> None:
        self.buffer.append(str(element.value))

    def visit_addition_expr(self, element: AdditionExpression) -> None:
        self.buffer.append("(")
        element.left.accept(self)  # instead of `self.visit(element.left)`
        self.buffer.append(element.sign)
        element.right.accept(self)  # instead of `self.visit(element.right)`
        self.buffer.append(")")

    def visit_subtraction_expr(self, element: SubtractionExpression) -> None:
        self.buffer.append("(")
        element.left.accept(self)
        self.buffer.append(element.sign)
        element.right.accept(self)
        self.buffer.append(")")

    def visit_multiplication_expr(self, element: MultiplicationExpression) -> None:
        element.left.accept(self)
        self.buffer.append(element.sign)
        element.right.accept(self)

    def __str__(self) -> str:
        return "".join(self.buffer)

    def reset(self) -> None:
        self.buffer = []
