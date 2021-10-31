from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Final

from creational.hw_pizza_station.pizza import Pizza
from creational.hw_pizza_station.enums.pizza_type import PizzaType


class PizzaBuilder(ABC):
    """
    PizzaBuilder is the builders interface contains set of common methods used
    in order to build the pizza object and its components.
    """

    def __init__(self, pizza_type: PizzaType) -> None:
        self._pizza: Final[Pizza] = Pizza(pizza_type)

    @abstractmethod
    def choose_dough(self) -> PizzaBuilder:
        """You MUST TO override me, I'm a placeholder."""

    @abstractmethod
    def choose_sauce(self) -> PizzaBuilder:
        """You MUST TO override me, I'm a placeholder."""

    @abstractmethod
    def add_topping(self) -> PizzaBuilder:
        """You MUST TO override me, I'm a placeholder."""

    def get_pizza(self) -> Pizza:
        return self._pizza
