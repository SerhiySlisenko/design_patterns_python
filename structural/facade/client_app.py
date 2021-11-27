from structural.facade.magic_square_generator import MagicSquareGenerator


def main() -> None:
    """
    Client app
    """

    gen = MagicSquareGenerator()

    print("Try first time:")
    square = gen.generate(3)
    gen.print_matrix(square)
    print(f"Found magic square at {gen.checked_combinations} combination\n")

    print("Try second time:")
    square = gen.generate_another(3)
    gen.print_matrix(square)
    print(f"Found magic square at {gen.checked_combinations} combination")


if __name__ == '__main__':
    main()
