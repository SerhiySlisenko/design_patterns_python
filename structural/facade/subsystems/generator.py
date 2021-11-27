from random import randint
from typing import List


class Generator:
    """
    This class generates a 1-dimensional list of random digits in range 1 to 9
    """
    @staticmethod
    def generate(count: int) -> List[int]:
        return [randint(1, 9) for _ in range(count)]
