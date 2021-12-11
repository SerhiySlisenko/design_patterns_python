from __future__ import annotations
from typing import Any, Callable, TYPE_CHECKING

from mediator import Mediator
if TYPE_CHECKING:
    from participant import Participant


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Room(Mediator):
    """
    The Room class implements notify method of Mediator interface.
    In this case method send an event to all participants with reference to this Concrete Mediator.
    """
    def __init__(self) -> None:
        self.alert = Event()

    def notify(self, sender: Participant, event: Callable, value: Any) -> None:
        self.alert(sender, event, value)
