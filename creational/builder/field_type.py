from typing import Union


class Field:
    """
    Contains some of the important components that are required
    in order to construct the field object.
    """
    def __init__(self, name: str, value: Union[str, int]) -> None:
        self.value = value
        self.name = name

    def __str__(self) -> str:
        return f'self.{self.name} = {self.value}'
