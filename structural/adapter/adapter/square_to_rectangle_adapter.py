from __future__ import annotations

from structural.adapter.square import Square


class SquareToRectangleAdapter:
    """
    Adapter to work with Square as with a Rectangle
    """

    def __init__(self, square: Square) -> None:
        self.square = square

    @property
    def width(self) -> int:
        return self.square.side

    @property
    def height(self) -> int:
        return self.square.side
