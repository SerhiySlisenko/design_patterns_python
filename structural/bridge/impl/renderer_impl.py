from __future__ import annotations

from abc import ABC, abstractmethod


class RendererImplementation(ABC):
    """
    RendererImplementation defines the interface for all implementation classes
    """

    @abstractmethod
    def what_to_render_as(self, name: str) -> str:
        pass
