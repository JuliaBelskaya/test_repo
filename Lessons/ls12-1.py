from abc import ABC, abstractmethod

class Pet(ABC):
    __counter = 0

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.is_alive = True
        Pet.__counter += 1

    @classmethod
    def get_counter(cls):
        return cls.__counter

    def run(self):
        print('run')

    def jump(self):
        print('jump')

    def birthday(self):
        self.age += 1

    def change_weight(self, weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight += 0.2

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height += 0.2

    def voice(self):
        pass


class Dog(Pet):

    def voice(self):
        print('bark')

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 13:
                self.is_alive = False


class Cat(Pet):

    def voice(self):
        print('meow')

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 16:
                self.is_alive = False


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def fly(self):
        if self.weight > 0.1:
            print('parrot not fly')
        else:
            print('fly')

    def change_weight(self, weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight += 0.05

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height += 0.2

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 60:
                self.is_alive = False

    @abstractmethod
    def voice(self):
        pass


class Hourse(Pet):
    def voice(self):
        print('igogo')


class Donkey(Pet):
    def voice(self):
        print('iaia')


class Mule(Donkey, Hourse):
    pass


def call_voice(animals):
    for animal in animals:
        animal.voice()


def main():
    dog = Dog('Jack', 10, 'Max', 5, 7)
    cat = Cat('Bars', 5, 'Bob', 10, 5)
    cat_2 = Cat('aaa', 3, 'ddd', 5, 8)
    mule = Mule('bbb', 3, 'sss', 6, 9)
    parrot = Parrot('aaaa', 2, 'Vova', 0.1, 2, 'blue')
    print(parrot.weight)
    parrot.change_weight()
    print(parrot.weight)
    parrot.fly()

    # print(dog.name)
    # print(dog.age)
    # print(dog.master)
    # print(cat.name)
    # print(cat.age)
    # print(cat.master)
    # print(parrot.name)
    # print(parrot.age)
    # print(parrot.master)
    # print(parrot.weight)
    print(Pet.get_counter())
    mule.voice()


if __name__ == '__main__':
    main()
