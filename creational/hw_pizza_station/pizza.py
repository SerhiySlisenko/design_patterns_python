from __future__ import annotations
from typing import List, Optional
from creational.hw_pizza_station.enums.pizza_type import PizzaType
from creational.hw_pizza_station.enums.pizza_components import PizzaComponents


class Pizza:
    """
     Class for Pizza object.
     """
    def __init__(self, pizza_type: PizzaType):
        self.__dough: Optional[str] = None
        self.__sauce: Optional[str] = None
        self.__toppings: Optional[List[str]] = []
        self.__pizza_type: str = pizza_type.name

    @property
    def pizza_type(self) -> str:
        return self.__pizza_type

    @pizza_type.setter
    def pizza_type(self, value: PizzaType) -> None:
        self.__pizza_type = value.name

    @property
    def dough(self) -> str:
        return self.__dough

    @dough.setter
    def dough(self, value: PizzaComponents.Dough) -> None:
        self.__dough = value.name

    @property
    def sauce(self) -> str:
        return self.__sauce

    @sauce.setter
    def sauce(self, value: PizzaComponents.Sauce) -> None:
        self.__sauce = value.name

    @property
    def toppings(self) -> List[str]:
        return self.__toppings

    def add_topping(self, value: PizzaComponents.Topping) -> None:
        self.__toppings.append(value.name)

    def __str__(self) -> str:
        return f"Pizza {self.__pizza_type}"

    def show_components(self) -> None:
        pizza_str = f"----------------------Pizza {self.__pizza_type} components----------------------\n"
        pizza_str += f"Dough: {self.__dough}\n" if self.__dough is not None else ""
        pizza_str += f"Sauce: {self.__sauce}\n" if self.__sauce is not None else ""
        if self.__toppings is not None:
            pizza_str += f"Toppings: {', '.join(sorted(self.__toppings))}"
        pizza_str += f"\n------------------------------------------------------------------\n"
        print(pizza_str)
