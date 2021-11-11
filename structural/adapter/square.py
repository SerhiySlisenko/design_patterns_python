class Square:
    """
    Defines Square class
    """
    def __init__(self, side: int = 0) -> None:
        self.side = side

    def __str__(self) -> str:
        return f'Square with side length = {self.side}'
