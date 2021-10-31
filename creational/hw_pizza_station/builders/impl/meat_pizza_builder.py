from __future__ import annotations
from typing import Tuple

from creational.hw_pizza_station.enums.pizza_components import PizzaComponents

from .. import PizzaBuilder


class MeatPizzaBuilder(PizzaBuilder):
    """
    Creates specific pizza type.
    """
    DEFAULT_DOUGH = PizzaComponents.Dough.THICK
    DEFAULT_SAUCE = PizzaComponents.Sauce.MARINARA
    DEFAULT_TOPPINGS = (
        PizzaComponents.Topping.CHEESE, PizzaComponents.Topping.CHICKEN, PizzaComponents.Topping.PEPPERONI,
        PizzaComponents.Topping.BACON, PizzaComponents.Topping.TOMATO, PizzaComponents.Topping.MUSHROOMS,
    )

    def choose_dough(self, dough_type: str = DEFAULT_DOUGH) -> MeatPizzaBuilder:
        self._pizza.dough = dough_type
        return self

    def choose_sauce(self, sauce_type: str = DEFAULT_SAUCE) -> MeatPizzaBuilder:
        self._pizza.sauce = sauce_type
        return self

    def add_topping(self, toppings: Tuple[str] = DEFAULT_TOPPINGS) -> MeatPizzaBuilder:
        for topping in toppings:
            self._pizza.add_topping(topping)
        return self
