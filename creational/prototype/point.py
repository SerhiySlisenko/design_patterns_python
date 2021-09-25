class Point:
    """
     Contains some of the important components of the Point that are required
     in order to construct the point object.
     """
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"
