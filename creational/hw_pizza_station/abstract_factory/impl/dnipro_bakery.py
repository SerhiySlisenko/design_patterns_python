from typing import Dict, Type

from ..bakery_factory import BakeryFactory
from creational.hw_pizza_station.pizza import Pizza

from creational.hw_pizza_station.builders.pizza_builder import PizzaBuilder
from creational.hw_pizza_station.enums.pizza_type import PizzaType
from creational.hw_pizza_station.builders import CheesePizzaBuilder, VeggiePizzaBuilder


class DniproBakery(BakeryFactory):
    """
    Specific Bakery which determines own rules of baking, cutting, and boxing a pizza.
    Specific bakery may cook limited pizza types.
    """
    PIZZA_TYPES: Dict[PizzaType, Type[PizzaBuilder]] = {
        PizzaType.CHEESE: CheesePizzaBuilder,
        PizzaType.VEGGIE: VeggiePizzaBuilder,
    }
    PIZZA_STATION = "Dnipro"

    def bake(self, pizza: Pizza) -> None:
        print(f"Bake {pizza.pizza_type} pizza 20 minutes in an oven preheated to 190°C ")

    def cut(self, pizza: Pizza) -> None:
        print(f"Cut {pizza.pizza_type} pizza into 6 pieces")

    def box(self, pizza: Pizza) -> None:
        print(f"Put {pizza.pizza_type} pizza in a square wooden box")
