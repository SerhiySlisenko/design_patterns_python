from __future__ import annotations

from structural.bridge.impl.renderer_impl import RendererImplementation


class ShapeAbstraction:
    """
    ShapeAbstraction defines the interface for the "control"(Renderer) part of the
    class hierarchies.
    """

    def __init__(self, renderer: RendererImplementation) -> None:
        self.renderer = renderer
        self.name = None

    def __str__(self):
        return self.renderer.what_to_render_as(self.name)
