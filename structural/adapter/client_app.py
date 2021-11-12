from structural.adapter.square import Square
from structural.adapter.rectangle import Rectangle
from structural.adapter.adapters.square_to_rectangle_adapter import SquareToRectangleAdapter


def main() -> None:
    """
    Client app
    """
    sq = Square(11)
    try:
        print(Rectangle.calculate_area(sq))  # AttributeError: 'Square' object has no attribute 'width'
    except AttributeError as err:
        print(err)

    adapter = SquareToRectangleAdapter(sq)
    print(f"Area of Square(11x11)={Rectangle.calculate_area(adapter)}")

    sq.side = 10
    print(f"Area of Square(10x10)={Rectangle.calculate_area(adapter)}")


if __name__ == '__main__':
    main()
