from abc import ABC, abstractmethod
from typing import Dict, Type

from creational.hw_pizza_station.builders.pizza_builder import PizzaBuilder
from creational.hw_pizza_station.pizza import Pizza
from creational.hw_pizza_station.enums.pizza_type import PizzaType
from creational.hw_pizza_station.builders import CheesePizzaBuilder, VeggiePizzaBuilder, MeatPizzaBuilder,\
    PepperoniPizzaBuilder


class BakeryFactory(ABC):
    """
    Abstract Factory is used to cook the pizza in different bakeries of Pizza Studio franchise.
    """
    PIZZA_TYPES: Dict[PizzaType, Type[PizzaBuilder]] = {
        PizzaType.CHEESE: CheesePizzaBuilder,
        PizzaType.VEGGIE: VeggiePizzaBuilder,
        PizzaType.MEAT: MeatPizzaBuilder,
        PizzaType.PEPPERONI: PepperoniPizzaBuilder,
    }
    PIZZA_STATION = ""

    def prepare(self, pizza_type: PizzaType) -> Pizza:
        pizza_builder: PizzaBuilder = self.PIZZA_TYPES.get(pizza_type)(pizza_type)

        pizza = pizza_builder\
            .choose_dough()\
            .choose_sauce()\
            .add_topping()\
            .get_pizza()
        pizza.show_components()
        self.bake(pizza)
        self.cut(pizza)
        self.box(pizza)

        return pizza

    @abstractmethod
    def bake(self, pizza: Pizza) -> None:
        pass

    @abstractmethod
    def cut(self, pizza: Pizza) -> None:
        pass

    @abstractmethod
    def box(self, pizza: Pizza) -> None:
        pass

    def suggest_choosing_pizza(self) -> PizzaType:
        self.__welcome()
        self.__show_available_pizza_types()
        try:
            pizza_key = str(input("\n-> Select pizza: ")).upper()
            if pizza_key == "B":
                pizza_type = None
            elif int(pizza_key) not in [p_type.value for p_type in self.PIZZA_TYPES]:
                raise ValueError
            else:
                pizza_type = PizzaType(int(pizza_key))
            return pizza_type

        except ValueError:
            print("Invalid key. Try again!")
            self.suggest_choosing_pizza()

    def __welcome(self) -> None:
        print("\n=========================================================")
        print(f"Welcome in {self.PIZZA_STATION} Pizza Station")
        print("=========================================================")

    def __show_available_pizza_types(self) -> None:
        print("Menu:")
        for pizza_type in self.PIZZA_TYPES:
            print(f"{pizza_type.value} - {pizza_type.name}")
        print("B - Back to the main menu")
