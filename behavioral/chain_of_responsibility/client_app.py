from behavioral.chain_of_responsibility.game import Game
from behavioral.chain_of_responsibility.characters import Goblin, GoblinKing


def main() -> None:
    """
    Client app
    """

    game = Game()
    goblin_alex = Goblin(game, 'Alex')
    game.creatures.add(goblin_alex)

    goblin_luca = Goblin(game, 'Luca')
    game.creatures.add(goblin_luca)
    print("There are characters in the Game:")
    print(goblin_alex)
    print(goblin_luca)

    goblin_unused = Goblin(game, 'Unused')  # Note: we don't add this creature to the Game
    game.creatures.add(goblin_alex)  # Note: we tried to add this creature to the Game twice
    print("\nThere are characters in the Game after some modifications (Nothing should be changed):")
    print(goblin_alex)
    print(goblin_luca)

    goblin_arthur = GoblinKing(game, 'Arthur')
    game.creatures.add(goblin_arthur)

    print("\nThere are characters in the Game after adding the King Goblin:")
    print(goblin_alex)
    print(goblin_luca)
    print(goblin_arthur)

    game.creatures.remove(goblin_luca)
    print("\nThere are characters in the Game after removing one of them:")
    print(goblin_alex)
    print(f'{goblin_luca} - Note: characteristics are default as it is not in the Game now')
    print(goblin_arthur)

    print("\nThere is our other unused character, as it is not in the game, his characteristics are default:")
    print(goblin_unused)


if __name__ == '__main__':
    main()
