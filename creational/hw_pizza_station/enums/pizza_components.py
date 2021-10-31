from enum import Enum, auto


class PizzaComponents:
    """
    Collects different pizza components, like dough, sauce, and toppings.
    """
    class Dough(Enum):
        """
        Collects different dough types for pizza.
        """
        THICK = auto()
        THIN = auto()

    class Sauce(Enum):
        """
        Collects different sauces for pizza.
        """
        MARINARA = auto()
        PLUM = auto()
        TOMATO = auto()
        PESTO = auto()

    class Topping(Enum):
        """
        Collects different toppings for pizza.
        """
        CHEESE = auto()
        DOUBLE_CHEESE = auto()
        CHICKEN = auto()
        PEPPERONI = auto()
        BACON = auto()
        MUSHROOMS = auto()
        OLIVE = auto()
        CORN = auto()
        ONION = auto()
        TOMATO = auto()
        BASIL = auto()
