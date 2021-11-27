from structural.flyweight.sentence import Sentence


def main() -> None:
    """
    Client app
    """

    sentence = Sentence('Hello, world.')
    print(sentence)

    sentence[0].bold = True
    sentence[1].bold = True
    print(sentence)

    sentence[0].capitalized = True
    sentence[1].italic = True
    print(sentence)


if __name__ == '__main__':
    main()
