# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path) as menuPath:
            menu_base = csv.reader(menuPath, delimiter=",")
            cabecalho_menu = next(menu_base)
            dishes = self.make_dishes(menu_base, cabecalho_menu)
        self.menu = menu_base
        self.cabecalho = cabecalho_menu
        self.dishes = dishes

    def make_dishes(self, menu, cabecalho) -> set:
        dish = cabecalho.index('dish')
        price = cabecalho.index('price')
        ingredient = cabecalho.index('ingredient')
        recipe_amount = cabecalho.index('recipe_amount')
        dishes = set()
        recipe = ''
        instanceDish = None
        for data in menu:
            if recipe != data[dish]:
                recipe = data[dish]
                instanceDish = Dish(recipe, float(data[price]))
            instanceIngredient = Ingredient(data[ingredient])
            instanceDish.add_ingredient_dependency(
                instanceIngredient, int(data[recipe_amount]))
            dishes.add(instanceDish)
        return dishes


if __name__ == "__main__":
    teste = MenuData('./tests/mocks/menu_base_data.csv')
