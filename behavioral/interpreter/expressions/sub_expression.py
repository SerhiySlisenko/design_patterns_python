from behavioral.interpreter.abstract_expression import AbstractExpression


class SubExpression(AbstractExpression):
    """
    Non-Terminal Expression.
    Implement an Interpret operation for non-terminal symbols in the grammar. Subtract in this particular case.
    """
    def __init__(self, left: AbstractExpression, right: AbstractExpression) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"({self.left} SUB {self.right})"

    def interpret(self) -> int:
        return self.left.interpret() - self.right.interpret()
