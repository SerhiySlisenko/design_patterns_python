from typing import List

from .subsystems import Generator, Splitter, Verifier


class MagicSquareGenerator:
    """
    This class generates a magic square of a given size.
    Magic square wiki: https://en.wikipedia.org/wiki/Magic_square
    """

    def __init__(self) -> None:
        self.g = Generator()
        self.s = Splitter()
        self.v = Verifier()
        self.checked_combinations = 0

    def generate(self, size: int) -> List[List[int]]:
        square = self._fill_matrix(size)
        self.checked_combinations = 1

        while self.v.verify(self.s.split(square)) is False:
            square = self._fill_matrix(size)
            self.checked_combinations += 1

        return square

    def generate_another(self, size: int) -> List[List[int]]:
        self.checked_combinations = 0
        while self.v.verify(self.s.split((square := self._fill_matrix(size)))) is False:
            self.checked_combinations += 1

        return square

    def _fill_matrix(self, size: int) -> List[List[int]]:
        square = [self.g.generate(size) for _ in range(size)]

        return square

    @staticmethod
    def print_matrix(square: List[List[int]]) -> None:
        for row in square:
            print(row)
