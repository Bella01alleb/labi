import datetime
import itertools

class Car:
    brand = "volvo"
    __year = datetime.datetime.now().year
    model = "hatchback"
    __id = itertools.count(1,1)

    def __init__(self, brand, color,model, number_registration):
        self.__id = next(Car.__id)
        self.brand = brand
        self.color = color
        self.model = model
        self.number_registration = number_registration
        self.price = number_registration / 2


    def get_id(self):
        return self.__id

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    @staticmethod
    def how_old_car(year):
        print("Car {datetime.datetime.now().year - year} лет")

    @classmethod
    def current_year_car(cls):
        print("Car current {cls.__year}")

    def show_car_info(self):
        print(" модель: {self.model}, год выпуска: {self.get_year()}, ""марка: {self.get_brand()},"
              " цвет: {self.color}, цена: {self.price}, регистрационный номер: {self.number_registration},"
              " id номер: {self.__id} ")


car1 = Car("Volvo", "Red","c30", 1054)
car1.set_year(2010)
car1.show_car_info()
car1.how_old_car(car1.get_year())

car2 = Car("Mercedes", "Silver","x5", 9690)
car2.set_brand("BMW")
car2.show_car_info()
Car.how_old_car(2022)