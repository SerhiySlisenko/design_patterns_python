from ..bakery_factory import BakeryFactory
from creational.hw_pizza_station.pizza import Pizza


class KyivBakery(BakeryFactory):
    """
    Specific Bakery which determines own rules of baking, cutting, and boxing a pizza.
    Specific bakery may cook limited pizza types.
    """
    PIZZA_STATION = "Kyiv"

    def bake(self, pizza: Pizza) -> None:
        print(f"Bake {pizza.pizza_type} pizza 25 minutes in an oven preheated to 180°C ")

    def cut(self, pizza: Pizza) -> None:
        print(f"Cut {pizza.pizza_type} pizza into 8 pieces")

    def box(self, pizza: Pizza) -> None:
        print(f"Put {pizza.pizza_type} pizza in a round cardboard box")
