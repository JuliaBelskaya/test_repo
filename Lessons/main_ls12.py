from ls12 import Dog, Cat, Parrot


def main():
    dog = Dog("Jack", 60, "Kevin", 12, 13)

    print(dog.name)
    print(dog.master)

    dog.run()
    dog.jump()
    dog.bark()

    print(dog.age)
    dog.birthday()

    dog.birthday()
    print(dog.is_alive)

    print(dog.weight)
    dog.change_weight()

    print(dog.height)
    dog.change_height()

    print()

    cat = Cat("Kitty", 2, "Mark", 12, 1)

    print(cat.name)
    print(cat.master)

    cat.run()
    cat.jump()
    cat.meow()

    print(cat.age)
    cat.birthday()

    cat.birthday()
    print(cat.is_alive)

    print(cat.height)
    cat.change_height()

    print(cat.weight)
    cat.change_weight()

    print()

    parrot = Parrot("Kesha", 5, "Kate", 11, 3, 'curly')

    print(parrot.name)
    print(parrot.master)
    print(parrot.species)

    parrot.run()
    parrot.jump()
    parrot.fly()


    print(parrot.age)
    parrot.birthday()

    parrot.birthday()
    print(parrot.is_alive)

    print(parrot.weight)
    parrot.change_weight()

    print(parrot.weight)
    parrot.change_height()


if __name__ == "__main__":
    main()
