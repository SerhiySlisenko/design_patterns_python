
from structural.composite.components import SingleValue, ManyValues


def main() -> None:
    """
    Client app
    """

    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.add(22)
    other_values.add(33)

    all_values = ManyValues()
    all_values.add(single_value)
    all_values.add(other_values)

    print(all_values.sum())


if __name__ == '__main__':
    main()
