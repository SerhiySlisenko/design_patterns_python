from typing import Dict

from creational.hw_pizza_station.abstract_factory import BakeryFactory, LvivBakery, KyivBakery, DniproBakery

menu_str: Dict[str, str] = dict()
menu_str["1"] = "Lviv"
menu_str["2"] = "Kyiv"
menu_str["3"] = "Dnipro"
menu_str["Q"] = "Quit"

bakery_dict: Dict[str, BakeryFactory] = dict()
bakery_dict["1"] = LvivBakery()
bakery_dict["2"] = KyivBakery()
bakery_dict["3"] = DniproBakery()


def main() -> None:
    """
    Client app
    """
    bakery_key: str = ""
    while bakery_key != "Q":
        print("\n\nWelcome to Pizza Station")
        for key in menu_str:
            print(f"{key} - {menu_str.get(key)}")
        print("\n-> Select your location: ", end="")
        bakery_key = str(input()).upper()
        if bakery_key in bakery_dict:
            bakery = bakery_dict[bakery_key]
            pizza_type = bakery.suggest_choosing_pizza()
            if pizza_type is None:
                continue
            pizza = bakery.prepare(pizza_type)
            print("\n=========================================================")
            print(f"Bon Appetit, {pizza.pizza_type} pizza is ready. "
                  f"See you next time in {bakery.PIZZA_STATION} Pizza Station.")
            print("=========================================================")


if __name__ == '__main__':
    main()
