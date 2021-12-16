from __future__ import annotations
from typing import TYPE_CHECKING

from behavioral.observer.creature import Creature

if TYPE_CHECKING:
    from behavioral.observer.game import Game


class Cat(Creature):
    """
    Concrete creature in the Game - Cat.
    When Cat enters the Game it add the attack for all other cats on 2 points.
    When Cat leaves the Game it subtracts 2 points on all cats in the Game.
    """
    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self.attack = 2

        game.enters.append(self.subscribe)
        game.notify.append(self.notify)
        game.dies.append(self.unsubscribe)

        self.game.enters(self)

    def subscribe(self, cat: Cat) -> None:
        if isinstance(cat, Cat) and cat != self:
            self.attack += 2
            self.game.notify(cat)

    def notify(self, cat: Cat) -> None:
        if cat == self:
            self.attack += 2

    def unsubscribe(self, cat: Cat) -> None:
        if isinstance(cat, Cat) and cat != self:
            self.attack -= 2
