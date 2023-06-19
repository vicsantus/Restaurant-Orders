# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, 'r') as menuPath:
            menu_base = list(csv.reader(menuPath, delimiter=","))
        menu_base_list = menu_base[1:]
        dishes = self.make_dishes(menu_base_list)
        self.menu = menu_base_list
        self.dishes = dishes

    def make_dishes(self, menu) -> set:
        dishes = set()
        recipe = ''
        instanceDish = None
        for data in menu:
            if recipe != data[0]:
                recipe = data[0]
                instanceDish = Dish(recipe, float(data[1]))
            instanceIngredient = Ingredient(data[2])
            instanceDish.add_ingredient_dependency(
                instanceIngredient, int(data[3]))
            dishes.add(instanceDish)
        return dishes


if __name__ == "__main__":
    teste = MenuData('./data/menu_base_data.csv')
