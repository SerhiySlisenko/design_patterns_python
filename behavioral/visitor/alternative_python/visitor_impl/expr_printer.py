from behavioral.visitor.alternative_python.visitor import visitor
from behavioral.visitor.alternative_python.value import Value
from behavioral.visitor.alternative_python.expressions import AdditionExpression, SubtractionExpression, \
    MultiplicationExpression


class ExpressionPrinter:
    """
    ExpressionPrinter Visitor. Supports the printing of the expression.
    For addition and subtraction, parentheses are added.
    """
    def __init__(self) -> None:
        self.buffer = []

    @visitor(Value)
    def visit(self, elem: Value) -> None:
        self.buffer.append(str(elem.value))

    @visitor(AdditionExpression)
    def visit(self, elem: AdditionExpression) -> None:
        self.buffer.append("(")
        self.visit(elem.left)
        self.buffer.append(elem.sign)
        self.visit(elem.right)
        self.buffer.append(")")

    @visitor(MultiplicationExpression)
    def visit(self, elem: MultiplicationExpression) -> None:
        self.visit(elem.left)
        self.buffer.append(elem.sign)
        self.visit(elem.right)

    @visitor(SubtractionExpression)
    def visit(self, elem: SubtractionExpression) -> None:
        self.buffer.append("(")
        self.visit(elem.left)
        self.buffer.append(elem.sign)
        self.visit(elem.right)
        self.buffer.append(")")

    def __str__(self) -> str:
        return "".join(self.buffer)

    def reset(self) -> None:
        self.buffer = []
