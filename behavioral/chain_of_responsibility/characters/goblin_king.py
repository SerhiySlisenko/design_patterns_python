from __future__ import annotations
from typing import TYPE_CHECKING

from behavioral.chain_of_responsibility.what_to_query_enum import WhatToQuery
from .goblin import Goblin

if TYPE_CHECKING:
    from .creature import Creature
    from behavioral.chain_of_responsibility.game import Game
    from behavioral.chain_of_responsibility.query import Query


class GoblinKing(Goblin):
    """
    Class represents Goblin King.
    """
    def __init__(self, game: Game, name: str):
        super().__init__(game, name, 3, 3)

    def query(self, source: Creature, query: Query):
        if self != source and query.what_to_query == WhatToQuery.ATTACK:
            query.value += 1
