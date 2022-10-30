import random
import string
import os
import json
from datetime import datetime, timedelta


# def get_random_key():
#     letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
#     result_str = ''.join(random.choice(letters) for i in range(6))
#     return result_str


class Ticket:

    def __init__(self, number, price):
        self.number = number
        self.price = price
        self.date = str(datetime.now())


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

    def __init__(self, name, amount, price, date: datetime):
        self.name = name
        self.amount = amount
        self.price = price
        self.list = {'tickets': []}
        self.act_number = 0
        self.date = date

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

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if isinstance(date, datetime) and (date - datetime.now()).days > 0:
            self.__date = date
        else:
            raise ValueError

    def push_json(self, item, file):
        item = json.dumps(item, indent=2)
        item = json.loads(str(item))
        with open(file, 'w') as json_file:
            json.dump(item, json_file, indent=4)

    def pull_json(self, file_name, index):
        with open(file_name, 'r') as json_file:
            return json.load(json_file)['tickets'][index]

    def sell_ticket(self, isStudent: bool):
        if not isinstance(isStudent, bool):
            raise ValueError
        if self.act_number < self.amount:
            time = self.date - datetime.now()
            key = str(self.act_number + 1)
            if isStudent:
                self.list['tickets'].append(Student_ticket(key, self.price).__dict__)
            else:
                if time.days > 60:
                    self.list['tickets'].append(Advanced_ticket(key, self.price).__dict__)
                else:
                    if time.days < 10:
                        self.list['tickets'].append(Late_ticket(key, self.price).__dict__)
                    else:
                        self.list['tickets'].append(Ticket(key, self.price).__dict__)
            self.act_number += 1
            self.push_json(self.list, 'tickets.json')
            return self.pull_json('tickets.json', self.act_number-1)
        else:
            return 'Sold Out'




x = Event('Lesson', 10, 100, datetime(2022,11,15))
print(x.sell_ticket(True))
print(x.sell_ticket(False))
print(x.sell_ticket(True))
print(x.sell_ticket(False))
print(x.sell_ticket(False))
x.sell_ticket(False)
x.sell_ticket(True)

print(x.pull_json('tickets.json', 3))
