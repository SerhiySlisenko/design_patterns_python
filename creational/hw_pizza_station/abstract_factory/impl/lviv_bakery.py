from ..bakery_factory import BakeryFactory
from creational.hw_pizza_station.pizza import Pizza


class LvivBakery(BakeryFactory):
    """
    Specific Bakery which determines own rules of baking, cutting, and boxing a pizza.
    Specific bakery may cook limited pizza types.
    """
    PIZZA_STATION = "Lviv"

    def bake(self, pizza: Pizza) -> None:
        print(f"Bake {pizza.pizza_type} pizza 15 minutes in an oven preheated to 200°C ")

    def cut(self, pizza: Pizza) -> None:
        print(f"Cut {pizza.pizza_type} pizza into 6 pieces")

    def box(self, pizza: Pizza) -> None:
        print(f"Put {pizza.pizza_type} pizza in a square cardboard box")
