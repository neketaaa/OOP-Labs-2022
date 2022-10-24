import random
import string


def get_random_key():
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(6))
    return result_str


class Ticket:

    def __init__(self, number, price):
        self.number = number
        self.price = price

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if number:
            self.__number = number
        else:
            raise ValueError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, float | int) and price > 0:
            self.__price = price
        else:
            raise ValueError

    def __str__(self):
        return f'Ticket type: Regular\nNumber: {self.number}\nPrice: {self.price}'


class Advanced_ticket(Ticket):

    def __init__(self, number, price):
        super().__init__(number, price * 0.6)

    def __str__(self):
        return f'Ticket type: Advanced\nNumber: {self.number}\nPrice: {self.price}'


class Student_ticket(Ticket):

    def __init__(self, number, price):
        super().__init__(number, price * 0.5)

    def __str__(self):
        return f'Ticket type: Student\nNumber: {self.number}\nPrice: {self.price}'


class Late_ticket(Ticket):

    def __init__(self, number, price):
        super().__init__(number, price * 1.1)

    def __str__(self):
        return f'Ticket type: Late\nNumber: {self.number}\nPrice: {self.price}'


class Event:

    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        self.list = []
        self.act_number = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name and isinstance(name, str):
            self.__name = name
        else:
            raise ValueError

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__amount = amount
        else:
            raise ValueError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, float | int) and price > 0:
            self.__price = price
        else:
            raise ValueError

    def sell_ticket(self, type):
        key = get_random_key()
        # Type: R/A/S/L
        if self.act_number < self.amount:
            match type:
                case 'R':
                    self.list.append(Ticket(key, self.price))
                case 'A':
                    self.list.append(Advanced_ticket(key, self.price))
                case 'S':
                    self.list.append(Student_ticket(key, self.price))
                case 'L':
                    self.list.append(Late_ticket(key, self.price))
            self.act_number += 1
            return self.list[self.act_number - 1]
        else:
            return 'Sold Out'


x = Event('Lesson', 5, 100)
print(x.sell_ticket('S'))
print(x.sell_ticket('R'))
print(x.sell_ticket('S'))
print(x.sell_ticket('A'))
print(x.sell_ticket('S'))
x.sell_ticket('L')
x.sell_ticket('R')
x.sell_ticket('S')
x.sell_ticket('L')
print(x.sell_ticket('S'))
print(x.sell_ticket('A'))
