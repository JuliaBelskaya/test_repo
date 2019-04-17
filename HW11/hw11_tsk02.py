# Создать класс Car. Атрибуты: марка, модель,
# год  выпуска, скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5),
# уменьшение скорости(скорость  - 5),
# стоп(сброс скорости на 0),
# отображение скорости,
# разворот(изменение знака скорости).
# Все атрибуты приватные.


class Car:
    def __init__(self, mark, model, year, speed=0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        self.__mark = mark

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def speed_up(self):
        self.__speed += 5

    def slow_down(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def display_speed(self):
        print(self.__speed)

    def reverse(self):
        self.speed *= -1


mycar = Car("bmv", "x5", "3")
mycar.speed = 100
print(mycar.mark)
print(mycar.model)
print(mycar.year)
print(mycar.speed)

mycar.speed_up()
mycar.display_speed()

mycar.slow_down()
mycar.display_speed()

mycar.reverse()
mycar.display_speed()

mycar.stop()
mycar.display_speed()
