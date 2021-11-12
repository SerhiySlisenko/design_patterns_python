from __future__ import annotations

from structural.bridge.impl.renderer_impl import RendererImplementation


class VectorRendererImplementation(RendererImplementation):
    """
    VectorRendererImplementation corresponds to a Vector rendering type and implements
    the VectorRendererImplementation interface.
    """

    def what_to_render_as(self, name: str) -> str:
        return 'Drawing {0} as pixels'.format(name)
