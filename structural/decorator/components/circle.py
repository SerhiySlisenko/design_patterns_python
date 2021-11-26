from .shape import Shape


class Circle(Shape):
    """
    The concrete Circle class provide default implementations of the operation.
    """

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def resize(self, factor: int) -> None:
        """
        This method is intently not included in the base class. It should work only in Circle class.
        """
        self.radius *= factor

    def __str__(self) -> str:
        return f'A circle of radius {self.radius}'
