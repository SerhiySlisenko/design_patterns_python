from ..components.shape import Shape
from .decorator import Decorator


class ColoredShape(Decorator):
    """
    The concrete wrapping code. ColoredShape execute his behavior after the call to a wrapped object.
    """

    def __init__(self, shape: Shape, color: str) -> None:
        super().__init__(shape)
        self.color = color

    def __str__(self) -> str:
        return f'{self._shape} has the color {self.color}'
