from __future__ import annotations
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.mediator.room import Room


class Participant:
    """
    Regular person in our room.
    Particular participant knows nothing about other participants and cannot contact any of them directly
    """
    def __init__(self, name: str, room: Room) -> None:
        self.name = name
        self.points = 0
        self.room = room
        room.alert.append(self.mediator_alert)

    def mediator_alert(self, sender: Participant, event: Callable, value: int) -> None:
        if sender != self:
            if event.__name__ == self.increase.__name__:
                self.points += value
            if event.__name__ == self.decrease.__name__:
                self.points -= value

    def increase(self, value: int) -> None:
        self.room.notify(self, self.increase, value)

    def decrease(self, value: int) -> None:
        self.room.notify(self, self.decrease, value)
