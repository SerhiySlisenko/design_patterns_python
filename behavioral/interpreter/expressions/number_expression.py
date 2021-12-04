from behavioral.interpreter.abstract_expression import AbstractExpression


class NumberExpression(AbstractExpression):
    """
    Terminal Expression.
    Implement an interpret operation associated with terminal symbols in
    the grammar.
    """
    def __init__(self, value: int) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"{self.value}"

    def interpret(self) -> int:
        return self.value
