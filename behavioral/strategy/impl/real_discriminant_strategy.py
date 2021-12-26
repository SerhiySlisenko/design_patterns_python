from behavioral.strategy.strategy import DiscriminantStrategy


class RealDiscriminantStrategy(DiscriminantStrategy):
    """
    Concrete Strategies implement the algorithm while following the base Strategy
    interface. The interface makes them interchangeable in the Context.

    If discriminant is negative, we return it as-is.
    """
    def calculate_discriminant(self, a: int, b: int, c: int) -> int:
        discriminant = b*b - 4*a*c
        return discriminant
