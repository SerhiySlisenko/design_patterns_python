import cmath

from behavioral.strategy.strategy import DiscriminantStrategy


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    """
    Concrete Strategies implement the algorithm while following the base Strategy
    interface. The interface makes them interchangeable in the Context.

    If discriminant is negative, the return value is NaN (not a number)!
    """
    def calculate_discriminant(self, a: int, b: int, c: int) -> float:
        discriminant = b*b - 4 * a * c
        if discriminant < 0:
            discriminant = cmath.nan
        return discriminant
