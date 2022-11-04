from datetime import datetime

class Pizza:

    def __init__(self, name: str, isThick: bool, ingredients = [], price=100):
        self.name = name
        self.isThick = isThick
        self.ingredients = ingredients
        self.price = price


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
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        print(price)
        if isinstance(price, float | int):
            self.__price = price
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
        self.__ingredients = { # [quantity,price]
            'cheese': [0,15],
            'peperoni': [0,10],
            'mushrooms': [0,15],
            'ham': [0,10],
            'sweetcorn': [0,13],
            'onions': [0,10],
            'pineapple': [0,10],
            'bacon': [0,10],
            'peppers': [0,14],
            'sausage': [0,20],
            'tomatoes': [0,10],
            'burger_sause': [0,10],
            'pesto_sause': [0,10],
            'ketchup': [0,10],
            'mayo_sause': [0,10]
        }
        self.add_ingredient(ingredients)

    def __str__(self):
        pizza = self.name + '\nPrice: ' + str(self.price)
        if self.isThick:
            pizza += '\nThick base'
        else:
            pizza += '\nThin base'
        for key in self.ingredients:
            value = self.ingredients.get(key)[0]
            if self.ingredients.get(key)[0]:
                pizza += f'\n {key}: {value}'
        return pizza

    def add_ingredient(self, ingredients, isFirstTime=True):
        for item in ingredients:
            if item in self.__ingredients:
                self.__ingredients[item][0] += 1
                if not isFirstTime:
                    self.price += self.__ingredients[item][1]


class Pizza_of_the_day(Pizza):

    def __init__(self):
        p_o_d = { #pizzas_of_the_day
            'pizzas': [
                {
                    'Name': 'Sunday pizza',
                    'IsThick': True,
                    'Ingredients': ['mayo_sause', 'sausage', 'bacon', 'ham', 'peperoni', 'burger_sause'],
                    'price': 150
                },
                {
                    'Name': 'Monday pizza',
                    'IsThick': False,
                    'Ingredients': ['cheese', 'ham', 'onions', 'pineapple', 'pesto_sause'],
                    'price': 150
                },
                {
                    'Name': 'Tuesday pizza',
                    'IsThick': True,
                    'Ingredients': ['onions', 'bacon', 'tomatoes', 'burger_sause', 'sausage', 'cheese'],
                    'price': 150
                },
                {
                    'Name': 'Wednesday pizza',
                    'IsThick': True,
                    'Ingredients': ['cheese', 'mushrooms', 'onions', 'peppers', 'sweetcorn', 'mayo_sause'],
                    'price': 150
                },
                {
                    'Name': 'Thursday pizza',
                    'IsThick': False,
                    'Ingredients': ['ketchup', 'peperoni', 'peppers', 'bacon', 'tomatoes'],
                    'price': 150
                },
                {
                    'Name': 'Friday pizza',
                    'IsThick': True,
                    'Ingredients': ['ketchup', 'mushrooms', 'sweetcorn', 'sausage'],
                    'price': 150
                },
                {
                    'Name': 'Saturday pizza',
                    'IsThick': False,
                    'Ingredients': ['bacon', 'pesto_sause', 'cheese', 'peppers'],
                    'price': 150
                }

            ]}
        day = int(datetime.now().strftime('%w'))
        super().__init__(p_o_d['pizzas'][day]['Name'],p_o_d['pizzas'][day]['IsThick'],p_o_d['pizzas'][day]['Ingredients'],p_o_d['pizzas'][day]['price'])


        # match day:
        #     case 1:
        #         super().__init__('Monday pizza', False, ['cheese', 'ham', 'onions', 'pineapple', 'pesto_sause'], 150)
        #     case 2:
        #         super().__init__('Tuesday pizza', True, ['onions', 'bacon', 'tomatoes', 'burger_sause', 'sausage', 'cheese'], 150)
        #     case 3:
        #         super().__init__('Wednesday pizza', True, ['cheese', 'mushrooms', 'onions', 'peppers', 'sweetcorn', 'mayo_sause'], 150)
        #     case 4:
        #         super().__init__('Thursday pizza', False, ['ketchup', 'peperoni', 'peppers', 'bacon', 'tomatoes'], 150)
        #     case 5:
        #         super().__init__('Friday pizza', True, ['ketchup', 'mushrooms', 'sweetcorn', 'sausage'], 150)
        #     case 6:
        #         super().__init__('Saturday pizza', False, ['bacon', 'pesto_sause', 'cheese', 'peppers'], 150)
        #     case 0:
        #         super().__init__('Sunday pizza', True, ['mayo_sause', 'sausage', 'bacon', 'ham', 'peperoni', 'burger_sause'], 150)


x = Pizza_of_the_day()
print(x)
x.add_ingredient(['mushrooms', 'cheese', 'tomatoes'], False)
print(x)


