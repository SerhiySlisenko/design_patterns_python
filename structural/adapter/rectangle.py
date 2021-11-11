class Rectangle:
    """
    External Rectangle class. We can not inherit from it, only use it public API
    """
    def __init__(self, width: int = 0, height: int = 0) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f'Rectangle: width = {self.width}, height = {self.height}'

    @staticmethod
    def calculate_area(rc) -> int:
        return rc.width * rc.height
