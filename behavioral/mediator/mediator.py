from abc import ABC, abstractmethod
from typing import Any, Callable


class Mediator(ABC):
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to other components.
    """
    @abstractmethod
    def notify(self, sender: object, event: Callable, value: Any) -> None:
        pass
