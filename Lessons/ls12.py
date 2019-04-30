# Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и
# методы: run, jump, birthday(увеличивает age на 1),
# sleep. Класс Parrot имеет дополнительный метод fly.
# Cat - meow, Dog - bark.


class Dog:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print("run")

    def jump(self):
        print("jump")

    def birthday(self):
        self.age += 1
        print(self.age)

    def bark(self):
        print("baark!")


def main():

    dog = Dog("Jack", 3, "Kevin")
    print(dog.name)
    print(dog.age)
    print(dog.master)

    dog.run()
    dog.jump()
    dog.birthday()
    dog.bark()


if __name__ == "__main__":
    main()


class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print("run!")

    def jump(self):
        print("jump")

    def birthday(self):
        self.age += 1
        print(self.age)

    def meow(self):
        print("meeeoow!")


def main():
    cat = Cat("Kitty", 2, "Mark")
    print(cat.name)
    print(cat.age)
    print(cat.master)

    cat.run()
    cat.jump()
    cat.birthday()
    cat.meow()


if __name__ == "__main__":
    main()


class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print("run!")

    def jump(self):
        print("jump!")

    def birthday(self):
        self.age += 1
        print(self.age)

    def fly(self):
        print("flyy!")


def main():
    cat = Parrot("Kesha", 5, "Kate")
    print(cat.name)
    print(cat.age)
    print(cat.master)

    cat.run()
    cat.jump()
    cat.birthday()
    cat.fly()


if __name__ == "__main__":
    main()
