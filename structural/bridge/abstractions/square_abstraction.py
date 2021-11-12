from __future__ import annotations

from structural.bridge.abstractions.shape_abstraction import ShapeAbstraction
from structural.bridge.impl.renderer_impl import RendererImplementation


class SquareAbstraction(ShapeAbstraction):
    """
    SquareAbstraction extend the Abstraction without changing the Implementation classes.
    """

    def __init__(self, renderer: RendererImplementation) -> None:
        super().__init__(renderer)
        self.name = 'Square'

