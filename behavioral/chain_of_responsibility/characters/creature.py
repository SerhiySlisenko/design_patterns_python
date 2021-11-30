from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.chain_of_responsibility.game import Game
    from behavioral.chain_of_responsibility.query import Query


class Creature(ABC):
    """
    Class represents default creature.
    """
    def __init__(self, game: Game, name: str, attack: int, defense: int) -> None:
        self.game = game
        self.name = name
        self.initial_defense = defense
        self.initial_attack = attack

    @property
    @abstractmethod
    def attack(self) -> int:
        pass

    @property
    @abstractmethod
    def defense(self) -> int:
        pass

    @abstractmethod
    def query(self, source: Creature, query: Query) -> None:
        pass

    def __str__(self) -> str:
        return f'{self.__class__.__name__} named {self.name} ({self.attack}/{self.defense})'
