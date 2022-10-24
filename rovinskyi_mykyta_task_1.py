import datetime
from operator import attrgetter


class Wheather:
    days = []

    def __init__(self, date,  aver_temp, pressure, precipitation):
        if isinstance(date, datetime.datetime) and  isinstance(aver_temp, float | int) and isinstance(pressure,float | int) and isinstance(precipitation, float | int):
            self.date = date
            self.aver_temp = aver_temp
            self.pressure = pressure
            self.precipitation = precipitation
            self.days.append(self)
        else:
            raise ValueError

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if date and isinstance(date, datetime.datetime):
            self.__date = date
        else:
            raise ValueError

    @property
    def aver_temp(self):
        return self.__aver_temp

    @aver_temp.setter
    def aver_temp(self, temp):
        if temp and isinstance(temp, float | int):
            self.__aver_temp = temp
        else:
            raise ValueError

    @property
    def pressure(self):
        return self.__pressure

    @pressure.setter
    def pressure(self, pressure):
        if pressure and isinstance(pressure, float | int):
            self.__pressure = pressure
        else:
            raise ValueError

    @property
    def precipitation(self):
        return self.__precipitation

    @precipitation.setter
    def precipitation(self, precipitation):
        if precipitation and isinstance(precipitation, float | int):
            self.__precipitation = precipitation
        else:
            raise ValueError

    def highest_pressure(self):
        list = sorted(self.days, key=attrgetter('pressure'), reverse=True)
        return f'{list[0].date} {list[0].pressure}'



def main():
    x = Wheather(datetime.datetime(2022,6,15), 20, 300, 1010)
    y = Wheather(datetime.datetime(2022,6,5), 50, 1010, 10)
    z = Wheather(datetime.datetime(2021,7,5), 50, 1030, 20)
    print(x.highest_pressure())


if __name__ == "__main__":
    main()

