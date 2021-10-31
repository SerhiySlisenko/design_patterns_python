from __future__ import annotations
from typing import Tuple

from creational.hw_pizza_station.enums.pizza_components import PizzaComponents

from .. import PizzaBuilder


class PepperoniPizzaBuilder(PizzaBuilder):
    """
    Creates specific pizza type.
    """
    DEFAULT_DOUGH = PizzaComponents.Dough.THIN
    DEFAULT_SAUCE = PizzaComponents.Sauce.TOMATO
    DEFAULT_TOPPINGS = (
        PizzaComponents.Topping.DOUBLE_CHEESE, PizzaComponents.Topping.PEPPERONI,
        PizzaComponents.Topping.TOMATO, PizzaComponents.Topping.BASIL,
    )

    def choose_dough(self, dough_type: str = DEFAULT_DOUGH) -> PepperoniPizzaBuilder:
        self._pizza.dough = dough_type
        return self

    def choose_sauce(self, sauce_type: str = DEFAULT_SAUCE) -> PepperoniPizzaBuilder:
        self._pizza.sauce = sauce_type
        return self

    def add_topping(self, toppings: Tuple[str] = DEFAULT_TOPPINGS) -> PepperoniPizzaBuilder:
        for topping in toppings:
            self._pizza.add_topping(topping)
        return self
