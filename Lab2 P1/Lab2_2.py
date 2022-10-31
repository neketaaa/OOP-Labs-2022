from datetime import datetime

class Pizza:

    def __init__(self, name: str, isThick: bool, ingredients = []):
        self.name = name
        self.isThick = isThick
        self.ingredients = ingredients

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError

    @property
    def isThick(self):
        return self.__isThick

    @isThick.setter
    def isThick(self, isThick):
        if isinstance(isThick, bool):
            self.__isThick = isThick
        else:
            raise ValueError

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        if not isinstance(ingredients, list):
            raise ValueError
        self.__ingredients = {
            'cheese': 0,
            'peperoni': 0,
            'mushrooms': 0,
            'ham': 0,
            'sweetcorn': 0,
            'onions': 0,
            'pineapple': 0,
            'bacon': 0,
            'peppers': 0,
            'sausage': 0,
            'tomatoes': 0,
            'burger_sause': 0,
            'pesto_sause': 0,
            'ketchup': 0,
            'mayo_sause': 0
        }
        self.add_ingredient(ingredients)

    def __str__(self):
        pizza = self.name
        if self.isThick:
            pizza += '\nThick base'
        else:
            pizza += '\nThin base'
        for key in self.ingredients:
            value = self.ingredients.get(key)
            if self.ingredients.get(key):
                pizza += f'\n {key}: {value}'
        return pizza

    def add_ingredient(self, ingredients):
        for item in ingredients:
            if item in self.__ingredients:
                self.__ingredients[item] += 1


class Pizza_of_the_day(Pizza):

    def __init__(self):
        day = int(datetime.now().strftime('%w'))
        match day:
            case 1:
                super().__init__('Monday pizza', False, ['cheese', 'ham', 'onions', 'pineapple', 'pesto_sause'])
            case 2:
                super().__init__('Tuesday pizza', True, ['onions', 'bacon', 'tomatoes', 'burger_sause', 'sausage', 'cheese'])
            case 3:
                super().__init__('Wednesday pizza', True, ['cheese', 'mushrooms', 'onions', 'peppers', 'sweetcorn', 'mayo_sause'])
            case 4:
                super().__init__('Thursday pizza', False, ['ketchup', 'peperoni', 'peppers', 'bacon', 'tomatoes'])
            case 5:
                super().__init__('Friday pizza', True, ['ketchup', 'mushrooms', 'sweetcorn', 'sausage'])
            case 6:
                super().__init__('Saturday pizza', False, ['bacon', 'pesto_sause', 'cheese', 'peppers'])
            case 0:
                super().__init__('Sunday pizza', True, ['mayo_sause', 'sausage', 'bacon', 'ham', 'peperoni', 'burger_sause'])

x = Pizza_of_the_day()
print(x)
x.add_ingredient(['mushrooms', 'cheese', 'tomatoes'])
print(x)
