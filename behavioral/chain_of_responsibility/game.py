from behavioral.chain_of_responsibility.query import Query
from behavioral.chain_of_responsibility.characters.creature import Creature


class Game:
    """
    The class is responsible for containing all creatures and applying queries to them.
    """
    def __init__(self) -> None:
        self.creatures = set()

    def apply_query(self, given_creature: Creature, query: Query) -> None:
        if given_creature in self.creatures:
            for creature in self.creatures:
                creature.query(given_creature, query)
