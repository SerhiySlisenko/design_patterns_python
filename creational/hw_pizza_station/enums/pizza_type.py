from enum import Enum, auto


class PizzaType(Enum):
    """
    Collects different pizza types.
    """
    CHEESE = auto()
    VEGGIE = auto()
    MEAT = auto()
    PEPPERONI = auto()
    CUSTOM = auto()
