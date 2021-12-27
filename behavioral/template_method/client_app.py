from random import randint

from behavioral.template_method.creature import Creature
from behavioral.template_method.card_game import CardGame
from behavioral.template_method.impl import TemporaryDamageCardGame, PermanentDamageCardGame


def main() -> None:
    """
    Client app
    """
    c1: Creature = Creature("Player_1", randint(1, 5), randint(3, 8))
    c2: Creature = Creature("Player_2", randint(1, 5), randint(3, 8))
    print(f"{c1} has {c1.attack} attack and {c1.health} health")
    print(f"{c2} has {c2.attack} attack and {c2.health} health")

    game: CardGame = PermanentDamageCardGame([c1, c2])

    while game.winner is None:
        game.combat(0, 1)
        print(f"{c1} has {c1.health} health")
        print(f"{c2} has {c2.health} health")
    if game.winner != -1:
        print(f"Winner is {game.winner}")
    else:
        print("Draw")

    print(f"{'*'*40}")

    c1: Creature = Creature("Player_1", randint(1, 3), randint(1, 3))
    c2: Creature = Creature("Player_2", randint(1, 3), randint(1, 3))
    print(f"{c1} has {c1.attack} attack and {c1.health} health")
    print(f"{c2} has {c2.attack} attack and {c2.health} health")

    game: CardGame = TemporaryDamageCardGame([c1, c2])
    game.combat(0, 1)

    print(f"{c1} has {c1.health} health")
    print(f"{c2} has {c2.health} health")
    if game.winner is not None and game.winner != -1:
        print(f"Winner is {game.winner}")
    else:
        print("Draw")

    print(f"{'*'*40}")

    c1: Creature = Creature("Player_1", randint(1, 5), randint(15, 20), is_joker=True)
    c2: Creature = Creature("Player_2", randint(1, 5), randint(15, 20), is_joker=False)
    print(f"{c1} has {c1.attack} attack and {c1.health} health")
    print(f"{c2} has {c2.attack} attack and {c2.health} health")

    game: CardGame = PermanentDamageCardGame([c1, c2])

    while game.winner is None:
        game.combat(0, 1)
        print(f"{c1} has {c1.health} health")
        print(f"{c2} has {c2.health} health")
    if game.winner != -1:
        print(f"Winner is {game.winner}")
    else:
        print("Draw")


if __name__ == '__main__':
    main()
