from behavioral.template_method.card_game import CardGame
from behavioral.template_method.creature import Creature


class TemporaryDamageCardGame(CardGame):
    """
    This is type of game (e.g. Magic: the Gathering), unless the creature has been killed,
    its health returns to the original value at the end of the combat.
    So, any creature can be killed only by one shot.
    """
    def _hit(self, attacker: Creature, defender: Creature) -> None:
        if defender.health - attacker.attack <= 0:
            defender.health -= attacker.attack
