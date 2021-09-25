from copy import deepcopy

from point import Point


class Line:
    """
     Contains some of the important components of the Line that are required
     in order to construct the line object.
     """
    def __init__(self, start: Point = Point(), end: Point = Point()) -> None:
        self.start = start
        self.end = end

    def deep_copy(self):
        return deepcopy(self)

    def __str__(self) -> str:
        return f"Line starts at {self.start}, ends at {self.end}"
