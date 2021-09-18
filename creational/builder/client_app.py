from builders.code_builder import CodeBuilder


def main() -> None:
    """
    Client app
    """
    cb_with_fields = CodeBuilder('Person')\
        .add_field('name', '""') \
        .add_field('age', '0')

    print(cb_with_fields)
    print("\n")

    cb_just_class = CodeBuilder('Car')

    print(cb_just_class)


if __name__ == '__main__':
    main()
