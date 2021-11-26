from .shape import Shape


class Square(Shape):
    """
    The concrete Square class provide default implementations of the operation.
    """

    def __init__(self, side: int) -> None:
        self.side = side

    def __str__(self) -> str:
        return f'A square with side {self.side}'
