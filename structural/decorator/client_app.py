from structural.decorator.components import Circle, Square
from structural.decorator.decorators import ColoredShape


def main() -> None:
    """
    Client app
    """

    circle = ColoredShape(Circle(5), 'red')
    print(circle)
    print("Try to perform resizing...")
    circle.resize(2)
    print(circle)
    square = Square(4)
    print(square)
    square = ColoredShape(square, 'blue')
    print(square)
    print("Try to perform resizing...")
    square.resize(2)
    print(square)


if __name__ == '__main__':
    main()
