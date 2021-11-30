from __future__ import annotations
from typing import TYPE_CHECKING

from behavioral.chain_of_responsibility.query import Query
from behavioral.chain_of_responsibility.what_to_query_enum import WhatToQuery
from .creature import Creature

if TYPE_CHECKING:
    from behavioral.chain_of_responsibility.game import Game


class Goblin(Creature):
    """
    Class represents Goblin.
    """
    def __init__(self, game: Game, name: str, attack: int = 1, defense: int = 1) -> None:
        super().__init__(game, name, attack, defense)

    @property
    def attack(self) -> int:
        q = Query(self.initial_attack, WhatToQuery.ATTACK)
        self.game.apply_query(self, q)
        return q.value

    @property
    def defense(self) -> int:
        q = Query(self.initial_defense, WhatToQuery.DEFENSE)
        self.game.apply_query(self, q)
        return q.value

    def query(self, source: Creature, query: Query) -> None:
        if self != source and query.what_to_query == WhatToQuery.DEFENSE:
            query.value += 1
