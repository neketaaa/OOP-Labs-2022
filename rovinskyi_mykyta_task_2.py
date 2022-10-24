class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if isinstance(day, int) and 0<day<32:
            self.__day = day
        else:
            raise ValueError

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if isinstance(month, int) and 0 < month < 13 :
            self.__month = month
        else:
            raise ValueError

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if isinstance(year, int):
            self.__year = year
        else:
            raise ValueError

    def show1(self):
        return f'{self.day}.{self.month}.{self.year}'

    def show2(self):
        months = [' ','Jan', 'Feb', 'March', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        return f'{self.day} of {months[self.month]} {self.year} year'


def main():
    exp = Date(16, 6, 2004)
    print(exp.show1())
    print(exp.show2())


if __name__ == "__main__":
    main()

