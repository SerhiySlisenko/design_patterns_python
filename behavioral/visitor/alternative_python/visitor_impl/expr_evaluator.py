from behavioral.visitor.alternative_python.visitor import visitor
from behavioral.visitor.alternative_python.value import Value
from behavioral.visitor.alternative_python.expressions import AdditionExpression, SubtractionExpression, \
    MultiplicationExpression


class ExpressionEvaluator:
    """
    ExpressionEvaluator Visitor. Supports the execution of the expression.
    """
    def __init__(self) -> None:
        self.value = None

    @visitor(Value)
    def visit(self, val: Value) -> None:
        self.value = val.value

    @visitor(AdditionExpression)
    def visit(self, ae: AdditionExpression) -> None:
        self.visit(ae.left)
        temp = self.value
        self.visit(ae.right)
        self.value += temp

    @visitor(SubtractionExpression)
    def visit(self, se: SubtractionExpression) -> None:
        self.visit(se.right)
        temp = self.value
        self.visit(se.left)
        self.value -= temp

    @visitor(MultiplicationExpression)
    def visit(self, me: MultiplicationExpression) -> None:
        self.visit(me.left)
        temp = self.value
        self.visit(me.right)
        self.value *= temp

    def __str__(self) -> str:
        return str(self.value)
