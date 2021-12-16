from game import Game
from behavioral.observer.concrete_creatures.rat import Rat
from behavioral.observer.concrete_creatures.cat import Cat


def main() -> None:
    """
    Client app
    """
    game = Game()
    cat = Cat(game)
    rat = Rat(game)

    print(f"Cat attack={cat.attack}")
    print(f"Rat attack={rat.attack}\n")

    rat2 = Rat(game)
    print(f"Cat attack={cat.attack}")
    print(f"Rat attack={rat.attack}")
    print(f"Rat2 attack={rat2.attack}\n")

    with Rat(game) as rat3:
        print(f"Cat attack={cat.attack}")
        print(f"Rat attack={rat.attack}")
        print(f"Rat2 attack={rat2.attack}")
        print(f"Rat3 attack={rat3.attack}\n")
        with Cat(game) as cat2:
            print(f"Cat attack={cat.attack}")
            print(f"Cat2 attack={cat2.attack}")
            print(f"Rat attack={rat.attack}")
            print(f"Rat2 attack={rat2.attack}")
            print(f"Rat3 attack={rat3.attack}\n")
        print(f"Cat attack={cat.attack}")
        print(f"Rat attack={rat.attack}")
        print(f"Rat2 attack={rat2.attack}")
        print(f"Rat3 attack={rat3.attack}\n")

    print(f"Cat attack={cat.attack}")
    print(f"Rat attack={rat.attack}")
    print(f"Rat2 attack={rat2.attack}")


if __name__ == '__main__':
    main()
