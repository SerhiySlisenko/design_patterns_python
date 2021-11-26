from __future__ import annotations
from typing import List, Union

from ..components import Value, SingleValue


class ManyValues(Value):
    """
    The ManyValues class represents multiple object that may have
    several values or even include other ManyValues objects. ManyValues(Composite) objects
    delegate the actual work to their children and then "sum-up" the result.
    """

    def __init__(self) -> None:
        self._values: List[Value] = []

    def add(self, value: Union[Value, int]) -> None:
        if isinstance(value, int):
            value = SingleValue(value)
        self._values.append(value)

    def remove(self, value: Value) -> None:
        self._values.remove(value)

    def is_composite(self) -> bool:
        return True

    def sum(self) -> int:
        result = 0
        for value in self._values:
            result += value.sum()
        return result
