from creational.prototype.point import Point
from creational.prototype.line import Line


def main() -> None:
    """
    Client app
    """
    start_point = Point(1, 2)
    end_point_a = Point(5, 2)
    end_point_b = Point(1, 10)

    horizontal_line = Line(start_point, end_point_a)
    vertical_line = horizontal_line.deep_copy()
    vertical_line.end = end_point_b

    print(horizontal_line, vertical_line, sep="\n")

    diagonal_line = Line()
    diagonal_line.end = Point(-5, -5)
    opposite_diagonal_line = diagonal_line.deep_copy()
    opposite_diagonal_line.end = Point(5, 5)
    print(diagonal_line, opposite_diagonal_line, sep="\n")


if __name__ == '__main__':
    main()
