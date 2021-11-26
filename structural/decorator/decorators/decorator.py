from ..components.shape import Shape


class Decorator(Shape):
    """
    The base Decorator wrapping code.
    """
    _shape: Shape = None

    def __init__(self, shape: Shape) -> None:
        self._shape = shape

    @property
    def shape(self) -> Shape:
        """
        The Decorator delegates all work to the wrapped component.
        """

        return self._shape

    def resize(self, factor: int) -> None:
        """
        This method wasn't included in the base class.
        We want to call resize only for the concrete component classes that have it implemented. Otherwise, ignore it.
        """
        resize = getattr(self._shape, "resize", None)  # if concrete shape has 'resize' method we can call it
        if callable(resize):
            self.shape.resize(factor)

    def __str__(self) -> str:
        return str(self._shape)
