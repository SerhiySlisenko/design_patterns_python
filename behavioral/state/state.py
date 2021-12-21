from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from lock_context import LockContext


class State(ABC):
    """
    The base State class declares methods that all Concrete State should implement.
    """
    @abstractmethod
    def enter(self, context: LockContext, digit: int) -> None:
        pass

    @abstractmethod
    def reset(self, context: LockContext) -> None:
        pass

    @abstractmethod
    def set_password(self, context: LockContext, combination: List[int]) -> None:
        pass
