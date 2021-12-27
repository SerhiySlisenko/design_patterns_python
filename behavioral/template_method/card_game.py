from abc import ABC, abstractmethod
from typing import List, final

from behavioral.template_method.creature import Creature


class CardGame(ABC):
    """
    The Abstract Class defines a template method (combat) that contains a skeleton of algorithm.
    CardGame implements the logic for two(our limitation) creatures fighting each other.
    However, the exact mechanics of how damage is dealt is different.
    """
    def __init__(self, creatures: List[Creature]) -> None:
        self.creatures = creatures
        self.winner = None

    @final
    def combat(self, c1_index, c2_index) -> None:
        self._hit(self.creatures[c1_index], self.creatures[c2_index])
        self._hit(self.creatures[c2_index], self.creatures[c1_index])
        if self._is_game_with_jokers:
            self._joker_do(self.creatures[c1_index], self.creatures[c2_index])
        self.__find_winner(self.creatures[c1_index], self.creatures[c2_index])

    @abstractmethod
    def _hit(self, attacker: Creature, defender: Creature) -> None:
        pass

    def __find_winner(self, creature1: Creature, creature2: Creature) -> None:
        if creature1.health > 0 >= creature2.health:
            self.winner = creature1
        elif creature2.health > 0 >= creature1.health:
            self.winner = creature2
        elif creature1.health <= 0 and creature1.health <= 0:
            self.winner = -1

    @property
    def _is_game_with_jokers(self) -> bool:
        return False

    def _joker_do(self, creature1: Creature, creature2: Creature) -> None:
        """If you call me that you MUST TO override me"""
        raise ChildProcessError("The derived class must have an implementation")
