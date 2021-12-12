from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares methods for executing commands.
    """
    def __init__(self) -> None:
        self._snapshots = []

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass
