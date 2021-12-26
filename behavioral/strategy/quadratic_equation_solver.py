from typing import Tuple
import cmath

from behavioral.strategy.strategy import DiscriminantStrategy


class QuadraticEquationSolver:
    """
    This is kind of Context class. It defines the interface of interest to clients.
    In our case it only solves the quadratic equation.
    """
    def __init__(self, strategy: DiscriminantStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> DiscriminantStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: DiscriminantStrategy) -> None:
        self._strategy = strategy

    def solve(self, a: int, b: int, c: int) -> Tuple[complex, complex]:
        """ Returns a pair of complex (!) values """
        sqrt_of_discriminant = cmath.sqrt(self._strategy.calculate_discriminant(a, b, c))
        x1 = (-b + sqrt_of_discriminant) / (2 * a)
        x2 = (-b - sqrt_of_discriminant) / (2 * a)
        return x1, x2
