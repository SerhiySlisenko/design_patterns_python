from __future__ import annotations
from typing import Tuple

from creational.hw_pizza_station.enums.pizza_components import PizzaComponents

from .. import PizzaBuilder


class VeggiePizzaBuilder(PizzaBuilder):
    """
    Creates specific pizza type.
    """
    DEFAULT_DOUGH = PizzaComponents.Dough.THIN
    DEFAULT_SAUCE = PizzaComponents.Sauce.PESTO
    DEFAULT_TOPPINGS = (
        PizzaComponents.Topping.CHEESE, PizzaComponents.Topping.MUSHROOMS, PizzaComponents.Topping.OLIVE,
        PizzaComponents.Topping.CORN, PizzaComponents.Topping.ONION, PizzaComponents.Topping.TOMATO,
    )

    def choose_dough(self, dough_type: str = DEFAULT_DOUGH) -> VeggiePizzaBuilder:
        self._pizza.dough = dough_type
        return self

    def choose_sauce(self, sauce_type: str = DEFAULT_SAUCE) -> VeggiePizzaBuilder:
        self._pizza.sauce = sauce_type
        return self

    def add_topping(self, toppings: Tuple[str] = DEFAULT_TOPPINGS) -> VeggiePizzaBuilder:
        for topping in toppings:
            self._pizza.add_topping(topping)
        return self
