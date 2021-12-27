from behavioral.template_method.card_game import CardGame
from behavioral.template_method.creature import Creature


class PermanentDamageCardGame(CardGame):
    """
    This is a type of game (e.g. Hearthstone) where health damage persists.
    So, in order to kill some creature, you can take several shots.
    Also in this type of Game Jokers card have some additional effects.
    """

    def _hit(self, attacker: Creature, defender: Creature) -> None:
        defender.health -= attacker.attack

    @property
    def _is_game_with_jokers(self) -> bool:
        return True

    def _joker_do(self, creature1: Creature, creature2: Creature) -> None:
        if creature1.is_joker and not creature2.is_joker:
            creature2.health -= 2
            print(f"Log: {creature2.name} health in decreased. {creature1.name} is Joker")
        elif creature2.is_joker and not creature1.is_joker:
            creature1.health -= 2
            print(f"Log: {creature1.name} health in decreased. {creature1.name} is Joker")
        elif creature1.is_joker and creature2.is_joker:
            creature1.health += 2
            creature2.health += 2
            print(f"Log: {creature1.name} and {creature1.name} health in increased. They are Jokers")
