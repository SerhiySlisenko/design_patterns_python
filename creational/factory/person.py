class Person:
    """
     Contains some of the important components of the Person that are required
     in order to construct the person object.
     """
    def __init__(self, _id: int, name: str) -> None:
        self.id = _id
        self.name = name

    def __str__(self) -> str:
        return f"Name: {self.name} (id={self.id})"
