from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game


class Creature(ABC):
    """
    Base abstract class of any creature in the game. Here we are implementing a Context Manager as a Class.
    Added abstract methods to implement Event Manager logic of Observer design pattern.
    """
    def __init__(self, game: Game) -> None:
        self.game = game

    def __enter__(self) -> Creature:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.game.dies(self)

    @abstractmethod
    def subscribe(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def notify(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, creature: Creature) -> None:
        pass
