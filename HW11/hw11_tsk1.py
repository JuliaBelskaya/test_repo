#Создать пять классов описывающие реальные
# объекты. Каждый класс должен содержать
# минимум три приватных атрибута, конструктор,
# геттеры и сеттеры для каждого атрибута, два метода.


class Cat:
    def __init__(self, name, weight, age):
        self.__name = name
        self.__weight = weight
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def meow(self):
        print('Meeoow')

    def play(self):
        print('Want to play')

cat = Cat("Kitty", "15 kg", "3 years old")
print(cat.name)
cat.name = 'Simon'
print(cat.name)
print(cat.weight)
print(cat.age)

cat.meow()
cat.play()