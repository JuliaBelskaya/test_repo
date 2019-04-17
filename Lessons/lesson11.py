# # 11.01 Создать пустой класс Dog
#
#
# class Dog:
#     pass
#
#
# # Создание объекта
#
#
# class Dog:  #имя класса
#     pass
#
#
# dog = Dog()     #объект класса Dog

# 11.02 Создать два объекта класса Dog. Вывести их на экран


# class Dog:
#     pass
#
#
# dog1 = Dog()
# dog2 = Dog()
#
# print(dog1)
# print(dog2)

# 11.03 Добавить два метода в класс Dog: jump и run. Методы выводят на экран Jump! и Run! соответственно.

#
# class Dog:
#     def jump(self):
#         print("Jump!")
#
#     def run(self):
#         print("Run!")
#
#     def bark(self):
#         print('Woof Woof!')
#
# dog_1 = Dog()
# dog_1.bark()
#
#
# dog_2 = Dog()
# dog_2.jump()
#
# dog_3 = Dog()
# dog_3.run()
#

# Конструктор
# class Dog:
#    def __init__(self, name):
#        self.name = name
#
# dog_1 = Dog('Bob')
# print(dog_1.name)

# 11.4 Создать класс Dog. Класс имеет четыре атрибута:
# height, weight, name, age. Класс имеет три метода:
# jump, run, bark. Каждый метод выводит сообщение на экран.
# Создать два объекта класса Dog, вызвать все методы у каждого объекта.

#
# class Dog:
#     def __init__(self, name, height, weight, age):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age
#
#     def jump(self):
#         print("Jump!")
#
#     def run(self):
#         print("Run!")
#
#     def bark(self):
#         print("Woof Woof!")
#
#
# dog_1 = Dog("Bob", "100 cm", "60 kg", "10 years old")
# print(dog_1.name)
# print(dog_1.height)
# print(dog_1.weight)
# print(dog_1.age)
#
# dog_1.bark()
# dog_1.run()
# dog_1.jump()
#
# dog_2 = Dog('Cat', '100 cm', '55 kg', '15 years old')
# print(dog_2.name)
# print(dog_2.height)
# print(dog_2.weight)
# print(dog_2.age)
#
# dog_2.bark()
# dog_2.run()
# dog_2.jump()


# 11.05 Добавить в класс Dog метод change_name.
# Метод принимает на вход новое имя и меняет атрибут
# имени у объекта. Создать один объект класса. Вывести имя.
# Вызвать метод change_name. Вывести имя.


# class Dog:
#     def __init__(self, name, height, weight, age):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age
#
#     def jump(self):
#         print("Jump!")
#
#     def run(self):
#         print("Run!")
#
#     def bark(self):
#         print("Woof Woof!")
#
#     def change_name(self, name):
#         self.name = name
#
#
# dog_1 = Dog("Bob", "100 cm", "60 kg", "10 years old")
# dog_1.change_name("Bil")
# print(dog_1.name)
# print(dog_1.height)
# print(dog_1.weight)
# print(dog_1.age)
#
# dog_1.bark()
# dog_1.run()
# dog_1.jump()
#
#
# dog_2 = Dog("Cat", "100 cm", "55 kg", "15 years old")
# print(dog_2.name)
# print(dog_2.height)
# print(dog_2.weight)
# print(dog_2.age)
#
# dog_2.bark()
# dog_2.run()
# dog_2.jump()


# Модификаторы доступа
#
# class Dog:
#    def __init__(self, name, age, weight):
#        self.__name = name # private
#        self._age = age # protected
#        self.weight = weight # public
#
# dog = Dog('Bob', 8, 2.4)
# print(dog.__name) # ERROR
# print(dog._age)
# print(dog.weight)

# 11.05 Добавить в метод инициализации новый
# приватный атрибут - master. Создать метод
# get_master() который возвращает значение атрибута master.

#
# class Dog:
#     def __init__(self, name, height, weight, age, master):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age
#         self.__master = master
#
#     def get_master(self):
#         return self.__master
#
#
#
# dog_1 = Dog("Bob", "100 cm", "60 kg", "10 years old", "Kate")
# print(dog_1.name)
# print(dog_1.height)
# print(dog_1.weight)
# print(dog_1.age)
# print(dog_1.get_master())

# 11.06 Добавить новый приватный атрибут адрес
# (по-умолчанию равен ‘Minsk’). Добавить getter и setter для адреса.
#
# class Dog:
#     def __init__(self, name, height, weight, age, master, address='Minsk'):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age
#         self.__master = master
#         self.__address = address
#
#     def get_master(self):
#         return self.__master
#
#     def get_address(self):          #получить значение
#         return self.__address
#
#     def set_address(self, address):     #изменить значение
#         self.__address = address
#
#
#
# dog_1 = Dog("Bob", "100 cm", "60 kg", "10 years old", "Kate")
# print(dog_1.name)
# print(dog_1.height)
# print(dog_1.weight)
# print(dog_1.age)
# print(dog_1.get_master())
# print(dog_1.get_address())
#
# dog_1.set_address('Brest')
# print(dog_1.get_address())

# getter, setter через декораторы
#
# class Dog:
#     def __init__(self, master):
#         self.__master = master
#
#     @property
#     def master(self):
#         return self.__master
#
#     @master.setter
#     def master(self, master):
#         if len(master) < 5:
#             self.__master = master
#
#
# dog = Dog("Alex")
# dog.master = "Moe"
# print(dog.master)

#11.07 Сделать все атрибуты класса Dog приватными.
# Сделать для каждого атрибута getter и setter используя декораторы.

class Dog:
    def __init__(self, name, height, weight, age, master, address='Minsk'):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age
        self.__master = master
        self.__address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight




dog_1 = Dog("Bob", "100 cm", "60 kg", "10 years old", "Kate")
dog_1.name = 'Kim'      #setter
print(dog_1.name)       #getter
print(dog_1.height)
print(dog_1.weight)