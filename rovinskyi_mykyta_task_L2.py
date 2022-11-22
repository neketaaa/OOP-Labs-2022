from datetime import datetime


class Person:

    def __init__(self, name, surname, patronymic, date, sex):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.date = date
        self.sex = sex

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
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str):
            self.__surname = surname
        else:
            raise ValueError

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if isinstance(patronymic, str):
            self.__patronymic = patronymic
        else:
            raise ValueError

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if isinstance(date, datetime) and date < datetime.now():
            self.__date = date
        else:
            raise ValueError

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        if isinstance(sex, str) and sex == 'M' or 'F':
            self.__sex = sex
        else:
            raise ValueError

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.date > other.date
        return None

    def __ge__(self, other):
        if isinstance(other, Person):
            return self.date >= other.date
        return None

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.date < other.date

    def __le__(self, other):
        if isinstance(other, Person):
            return self.date <= other.date


class Worker(Person):
    def __init__(self, name, surname, patronymic, date, sex, company, education, role, salary, exp):
        super().__init__(name, surname, patronymic, date, sex)
        self.company = company
        self.education = education
        self.role = role
        self.salary = salary
        self.exp = exp  # years

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company):
        if isinstance(company, str):
            self.__company = company
        else:
            raise ValueError

    @property
    def education(self):
        return self.__education

    @education.setter
    def education(self, education):
        if isinstance(education, str):
            self.__education = education
        else:
            raise ValueError

    @property
    def education(self):
        return self.__education

    @education.setter
    def education(self, education):
        if isinstance(education, str):
            self.__education = education
        else:
            raise ValueError

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        if isinstance(role, str):
            self.__role = role
        else:
            raise ValueError

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if isinstance(salary, float | int) and salary > 0:
            self.__salary = salary
        else:
            raise ValueError

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, exp):
        if isinstance(exp, float | int) and exp < datetime.now().year - self.date.year:
            self.__exp = exp
        else:
            raise ValueError

class Organisation:

    def __init__(self,name):
        self.name = name
        self.workers = []

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
    def workers(self):
        return self.__workers

    def __add__(self, other):
        if isinstance(other, Worker) and self.workers.count(other) == 0:
            return self.workers.append(other)
        else:
            raise ValueError

    def __iadd__(self, other):
        if isinstance(other, Worker) and self.workers.count(other) == 0:
            return self.workers.append(other)
        else:
            raise ValueError


    def check_exp(self, number):
        iter_workers = iter(self.workers)
        more_exp = 0
        for worker in self.workers
            if next(iter_workers).exp > number:
                more_exp += 1
        return more_exp



x = Worker('Mykyta', 'Rovinskyi', 'Maks', datetime(1999, 6, 16), 'M', 'College','Software engeneering', 'Proffesor', 15000, 2)
y = Worker('Mykyta', 'Rovinskyi', 'Maks', datetime(1998, 6, 16), 'M', 'College','Software engeneering', 'Proffesor', 15000, 2)

print(x > y)
