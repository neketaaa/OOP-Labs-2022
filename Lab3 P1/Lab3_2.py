class Goods:


    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name:
            self.__name = name
        else:
            raise TypeError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, int | float) and price >= 0:
            self.__price = price
        else:
            raise TypeError

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            self.__quantity = quantity
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, int) and other > 0:
            self.quantity += other
            return self

    def __iadd__(self, other):
        if isinstance(other, int) and other > 0:
            self.quantity += other
            return self

    def __sub__(self, other):
        if isinstance(other, int) and other > 0:
            self.quantity -= other
            return self

    def __isub__(self, other):
        if isinstance(other, int) and other > 0:
            self.quantity -= other
            return self

    def __str__(self):
        return f'{self.name}, {self.price}, {self.quantity}'



class Composition:

    def __init__(self):
        self.goods = []

    def find_good(self, name):
        for i in range(0, len(self.goods)):
            if self.goods[i].name == name:
                return i
        return None


    def __add__(self, other):
        if isinstance(other, Goods):
            self.goods.append(other)
            return self
        else:
            raise TypeError

    def __iadd__(self, other):
        if isinstance(other, Goods):
            self.goods.append(other)
            return self
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, str) and self.find_good(other) != None: #can`t do without '!= None' cause index can == 0
            del self.goods[self.find_good(other)]
            return self
        else:
            raise ValueError

    def __getitem__(self, item):
        if isinstance(item, str) and self.find_good(item) != None: #can`t do without '!= None' cause index can == 0
            return self.goods[self.find_good(item)]
        else:
            raise ValueError

    def __setitem__(self, key, value):
        if isinstance(key, str) and isinstance(value, Goods) and self.find_good(key) != None:
            self.goods[self.find_good(key)] = value
        else:
            raise ValueError

    def request(self, items):
        request = 'Avability in stock'
        if isinstance(items, list):
            for item in items:
                if self.find_good(item) != None:
                    request += f'\n{self.goods[self.find_good(item)]}'
            return request
        else:
            raise TypeError


x = Composition()

x += Goods('name', 100, 1)
x += Goods('date', 100, 1)
x += Goods('oop', 100, 1)
x['name'] -= 1
#print(x['name'])
print(x.request(['name', 'date']))


