#Создать иерархию(слайды 49-50).
# Добавить конструктор в родительский класс Animal.
# Добавить абстрактный метод voice в класс Animal.
# Переопределить метод voice в классах Dog, Wold, Lion, Cat.
# Добавить два абстрактных метода в интерфейсы.
# Переопределить их в дочерних классах.
# Создать объекты классов Dog, Wold, Lion, Cat.
# Вызвать каждый из метод каждого объекта.


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def voice(self):
        pass


class Pet(Animal):
    pass


class WildAnimal(Animal):
    pass


class FelineInterface(ABC):
    @abstractmethod
    def scratch(self):
        raise NotImplemented

    @abstractmethod
    def eat_mouse(self):
        raise NotImplemented


class CanineInterface(ABC):
    @abstractmethod
    def howl(self):
        raise NotImplemented

    @abstractmethod
    def swim(self):
        raise NotImplemented


class Cat(Pet, FelineInterface):
    def voice(self):
        print("meow!")

    def scratch(self):
        print("khhh!")

    def eat_mouse(self):
        print("yummy!")


class Dog(Pet, CanineInterface):
    def voice(self):
        print("woof!")

    def howl(self):
        print("whoooo!")

    def swim(self):
        print("pluuh!")


class Lion(WildAnimal, FelineInterface):
    def voice(self):
        print("roarrr!")

    def scratch(self):
        print("skrh!")

    def eat_mouse(self):
        print("tasty!")


class Wolf(WildAnimal, CanineInterface):
    def voice(self):
        print("grrrr!")

    def howl(self):
        print("uuuhhh!")

    def swim(self):
        print("plouf!")


dog = Dog("Gavr", "7 yaers old")
cat = Cat("Kitty", "3 years old")
lion = Lion("Alex", "5 years old")
wolf = Wolf("Wolf", "2 years old")

print(dog.name)
print(dog.age)
print(cat.name)
print(cat.age)
print(wolf.name)
print(wolf.age)
print(lion.name)
print(lion.age)

dog.voice()
dog.howl()
dog.swim()
cat.voice()
cat.scratch()
cat.eat_mouse()
wolf.voice()
wolf.howl()
wolf.swim()
lion.voice()
lion.scratch()
lion.eat_mouse()
