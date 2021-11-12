from __future__ import annotations

from structural.bridge.impl.renderer_impl import RendererImplementation


class RasterRendererImplementation(RendererImplementation):
    """
    RasterRendererImplementation corresponds to a Raster rendering type and implements
    the RendererImplementation interface.
    """

    def what_to_render_as(self, name: str) -> str:
        return 'Drawing {0} as lines'.format(name)
