from abc import ABC, abstractmethod
from typing import Union


class DiscriminantStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by concrete implementations of Strategy.
    """

    @abstractmethod
    def calculate_discriminant(self, a: int, b: int, c: int) -> Union[int, float]:
        pass
