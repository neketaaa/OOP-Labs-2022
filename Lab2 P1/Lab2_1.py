import random
import string
import os
import json
from datetime import datetime, timedelta

def get_random_key():
     letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
     result_str = ''.join(random.choice(letters) for i in range(6))
     return result_str


class Ticket:

    def __init__(self, number, price, ticket_type = 'Regular' ):
        self.ticket_type = ticket_type
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
        super().__init__(number, price * 0.6, 'Advanced')

    def __str__(self):
        return f'Ticket type: Advanced\nNumber: {self.number}\nPrice: {self.price}'


class Student_ticket(Ticket):

    def __init__(self, number, price):
        super().__init__(number, price * 0.5, 'Student')

    def __str__(self):
        return f'Ticket type: Student\nNumber: {self.number}\nPrice: {self.price}'


class Late_ticket(Ticket):

    def __init__(self, number, price):
        super().__init__(number, price * 1.1, 'Late')

    def __str__(self):
        return f'Ticket type: Late\nNumber: {self.number}\nPrice: {self.price}'


class Event:

    def __init__(self, file_name, name, amount, price, date: datetime, adv_date=0, late_date=0):
        self.file_name = file_name
        self.name = name
        self.amount = amount
        self.price = price
        self.act_number = 0
        self.list = 'tickets'
        self.date = date
        self.adv_date = adv_date
        self.late_date = late_date

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name):
        if os.path.isfile(file_name) and '.json' in file_name:
            self.__file_name = file_name
        else:
            raise ValueError



    @property
    def list(self):
        return self.__list

    @list.setter
    def list(self, attr):
        self.__list = {attr: []}
        if os.stat(self.file_name).st_size:
            with open(self.file_name, 'r') as json_file:
                self.act_number = len(json.load(json_file)['tickets'])
                for index in range(self.act_number):
                    self.__list[attr].append(self.pull_json(self.file_name,index))
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

    @property
    def adv_date(self):
        return self.__adv_date

    @adv_date.setter
    def adv_date(self, adv_date):
        if isinstance(adv_date, int) and adv_date > 0:
            self.__adv_date = adv_date
        else:
            raise  ValueError

    @property
    def late_date(self):
        return self.__late_date

    @late_date.setter
    def late_date(self, late_date):
        if isinstance(late_date, int) and late_date > 0 and late_date <= self.adv_date:
            self.__late_date = late_date
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

    def constr_by_num(self, number):
        for i in range(self.act_number-1):
            temp_num = self.pull_json(self.file_name, i)
            if temp_num['_Ticket__number'] == number:
                return temp_num

        return 'Fault'

    def sell_ticket(self, isStudent: bool):
        if not isinstance(isStudent, bool):
            raise ValueError
        if self.act_number < self.amount:
            time = self.date - datetime.now()
            #key = str(self.act_number)
            key = get_random_key()
            if isStudent:
                self.list['tickets'].append(Student_ticket(key, self.price).__dict__)
            else:
                if time.days > self.adv_date:
                    self.list['tickets'].append(Advanced_ticket(key, self.price).__dict__)
                else:
                    if time.days < self.late_date:
                        self.list['tickets'].append(Late_ticket(key, self.price).__dict__)
                    else:
                        self.list['tickets'].append(Ticket(key, self.price).__dict__)
            self.act_number += 1
            self.push_json(self.list, self.file_name)
            return self.pull_json(self.file_name, self.act_number-1)
        else:
            return 'Sold Out'




x = Event('tickets.json', 'Lesson', 16, 100, datetime(2022,11,15), 60, 10)
print(x.sell_ticket(True))
print(x.sell_ticket(False))
print(x.sell_ticket(True))
print(x.sell_ticket(False))
print(x.sell_ticket(False))
x.sell_ticket(False)
x.sell_ticket(True)

print(x.constr_by_num('qOD9qZ'))
