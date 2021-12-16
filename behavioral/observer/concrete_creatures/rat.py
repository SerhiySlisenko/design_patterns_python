from __future__ import annotations
from typing import TYPE_CHECKING

from behavioral.observer.creature import Creature

if TYPE_CHECKING:
    from behavioral.observer.game import Game


class Rat(Creature):
    """
    Concrete creature in the Game - Rat.
    When Rat enters the Game it add the attack for all other rats on 1 point.
    When Rat leaves the Game it subtracts 1 point on all rats in the Game.
    """

    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self.attack = 1

        game.enters.append(self.subscribe)
        game.notify.append(self.notify)
        game.dies.append(self.unsubscribe)

        self.game.enters(self)

    def subscribe(self, rat: Rat) -> None:
        if isinstance(rat, Rat) and rat != self:
            self.attack += 1
            self.game.notify(rat)

    def notify(self, rat: Rat) -> None:
        if rat == self:
            self.attack += 1

    def unsubscribe(self, rat: Rat) -> None:
        if isinstance(rat, Rat):
            self.attack -= 1
