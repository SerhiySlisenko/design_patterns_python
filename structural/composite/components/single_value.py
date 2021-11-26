from __future__ import annotations

from ..components.value import Value


class SingleValue(Value):
    """
    The SingleValue class represents single value of a composition. It can't
    have multiple values.
    """
    def __init__(self, value: int) -> None:
        self.value = value

    def sum(self) -> int:
        return self.value
