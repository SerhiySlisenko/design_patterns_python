from __future__ import annotations
from typing import Tuple

from creational.hw_pizza_station.enums.pizza_components import PizzaComponents

from .. import PizzaBuilder


class CheesePizzaBuilder(PizzaBuilder):
    """
    Creates specific pizza type.
    """
    DEFAULT_DOUGH = PizzaComponents.Dough.THICK
    DEFAULT_SAUCE = PizzaComponents.Sauce.TOMATO
    DEFAULT_TOPPINGS = (
        PizzaComponents.Topping.TOMATO, PizzaComponents.Topping.DOUBLE_CHEESE, PizzaComponents.Topping.BASIL
    )

    def __init__(self, pizza_type):
        super().__init__(pizza_type)

    def choose_dough(self, dough_type: str = DEFAULT_DOUGH) -> CheesePizzaBuilder:
        self._pizza.dough = dough_type
        return self

    def choose_sauce(self, sauce_type: str = DEFAULT_SAUCE) -> CheesePizzaBuilder:
        self._pizza.sauce = sauce_type
        return self

    def add_topping(self, toppings: Tuple[str] = DEFAULT_TOPPINGS) -> CheesePizzaBuilder:
        for topping in toppings:
            self._pizza.add_topping(topping)
        return self
