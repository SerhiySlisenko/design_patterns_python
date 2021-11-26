from abc import ABC


class Shape(ABC):
    """
    The base Shape interface defines operations that can be altered by decorators.
    """

    def __str__(self) -> str:
        return ''
