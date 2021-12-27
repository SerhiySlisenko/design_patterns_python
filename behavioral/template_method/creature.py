class Creature:
    """
    Component of the game. Actually it is a card with two main attributes such as attack and health.
    Creatures can fight each other, dealing their Attack damage, thereby reducing opponent's health.
    Some cards could be a Joker, this can somehow help in the game.
    """
    def __init__(self, name: str, attack: int, health: int, is_joker: bool = False) -> None:
        self.name = name
        self.attack = attack
        self.health = health
        self.is_joker = is_joker

    def __str__(self) -> str:
        return f"{self.name} creature"
