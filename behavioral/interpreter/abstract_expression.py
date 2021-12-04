from abc import ABC, abstractmethod


class AbstractExpression(ABC):
    """
    Declare an abstract Interpret operation that is common to all nodes
    in the abstract syntax tree.
    """
    @abstractmethod
    def interpret(self) -> int:
        pass
