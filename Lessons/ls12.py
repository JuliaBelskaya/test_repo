# 12.1 Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и
# методы: run, jump, birthday(увеличивает age на 1),
# sleep. Класс Parrot имеет дополнительный метод fly.
# Cat - meow, Dog - bark.

#
# class Dog:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         print("run")
#
#     def jump(self):
#         print("jump")
#
#     def birthday(self):
#         self.age += 1
#         print(self.age)
#
#     def bark(self):
#         print("baark!")
#
#
# def main():
#
#     dog = Dog("Jack", 3, "Kevin")
#     print(dog.name)
#     print(dog.age)
#     print(dog.master)
#
#     dog.run()
#     dog.jump()
#     dog.birthday()
#     dog.bark()
#
#     print()
#
#
# if __name__ == "__main__":
#     main()
#
#
# class Cat:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         print("run!")
#
#     def jump(self):
#         print("jump")
#
#     def birthday(self):
#         self.age += 1
#         print(self.age)
#
#     def meow(self):
#         print("meeeoow!")
#
#
# def main():
#     cat = Cat("Kitty", 2, "Mark")
#     print(cat.name)
#     print(cat.age)
#     print(cat.master)
#
#     cat.run()
#     cat.jump()
#     cat.birthday()
#     cat.meow()
#
#     print()
#
# if __name__ == "__main__":
#     main()
#
#
# class Parrot:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         print("run!")
#
#     def jump(self):
#         print("jump!")
#
#     def birthday(self):
#         self.age += 1
#         print(self.age)
#
#     def fly(self):
#         print("flyy!")
#
#
# def main():
#     parrot = Parrot("Kesha", 5, "Kate")
#     print(parrot.name)
#     # print(parrot.age)
#     print(parrot.master)
#
#     parrot.run()
#     parrot.jump()
#     parrot.birthday()
#     parrot.fly()
#
#
# if __name__ == "__main__":
#     main()

# 12.2 Создать родительский класс Pet,
# содержащий все общие методы классов Dog,
# Cat, Parrot. Унаследовать Dog, Cat, Parrot
# от класса Pet. Удалить в дочерних классах
# те методы, которые имеются у родительского
# класса. Создать объект каждого класса и вызвать все его методы.
#
# class Pet:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         print("run")
#
#     def jump(self):
#         print("jump")
#
#     def birthday(self):
#         self.age += 1
#         print(self.age)
#
# class Dog(Pet):
#     def bark(self):
#         print("baark!")
#
# class Cat(Pet):
#     def meow(self):
#         print("meeeoow!")
#
# class Parrot(Pet):
#     def fly(self):
#         print("flyy!")

# вызов находится в файлу main_ls12

# перегрузка методов:
#
# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def set_name(self, name=None):
#         if name:
#             self.name = name
#         else:
#             print('Name was not changed')
#
#
# dog1 = Dog('Vasya')
# dog1.set_name('Bob')

# 12.3 Добавить два новых атрибута
# в родительский класс: weight и height.
# Добавить методы change_weight, change_height
# принимающий один параметр и прибавляющий его
# к соответствующему аргументу. В случае если
# параметр не был передан, увеличивать на 0.2.
# Изменить метод fly класса Parrot.
# Если вес больше 0.1 выводить сообщение This parrot cannot fly.

#
# class Pet:
#     def __init__(self, name, age, master, weight, height):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.weight = weight
#         self.height = height
#
#     def run(self):
#         print("run")
#
#     def jump(self):
#         print("jump")
#
#     def birthday(self):
#         self.age += 1
#         print(self.age)
#
#     def change_weight(self, weight=None):
#         if weight:
#             self.weight = weight
#         else:
#             self.weight += 0.2
#
#     def change_height(self, height=None):
#         if height:
#             self.height = height
#         else:
#             self.height += 0.2
#
#
# class Dog(Pet):
#     def bark(self):
#         print("baark!")
#
#
# class Cat(Pet):
#     def meow(self):
#         print("meeeoow!")
#
#
# # class Parrot(Pet):
# #     def fly(self):
# #         if self.weight > 0.1:
# #             print("This parrot cannot fly")
#
# #Переопределить методы change_weight,
# # change_height в классе Parrot.
# # В случае не передачи параметра - вес изменяется на 0.05
#
# class Parrot(Pet):
#     def fly(self):
#         if self.weight > 0.1:
#             print("This parrot cannot fly")
#
#     def change_weight(self, weight=None):
#         if weight:
#             self.weight = weight
#         else:
#             self.weight += 0.05
#
#     def change_height(self, height=None):
#         if height:
#             self.height = height
#         else:
#             self.height += 0.05

# Вызов родительского метода

# class A:
#    def do_something(self):
#        print('AA')
# class B(A):
#     def do_something(self):
#         super(B, self).do_something()
#         print('BB')
# b = B()
# b.do_something()

#Добавить атрибут is_alive равный при создании True.
# Переопределить метод birthday в дочерних классах.
# Если измененный возраст у собаки больше 13,
# менять is_alive на False. Для кошки - 16. Для попугая - 60.
# Добавить проверку по возрасту при создании,
# в случае если значения больше максимального, ставить is_alive = False
# Добавить проверку is_alive в дочерних методах.
# Если is_alive = false -> не вызывать метод родительского класса


class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.is_alive = True

    def run(self):
        print("run")

    def jump(self):
        print("jump")

    def birthday(self):
        self.age += 1
        print(self.age)

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




class Dog(Pet):
    def bark(self):
        print("baark!")

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 13:
                self.is_alive = False



class Cat(Pet):
    def meow(self):
        print("meeeoow!")

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
            print("This parrot cannot fly")

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 60:
                self.is_alive = False


    def change_weight(self, weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight += 0.05

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height += 0.05
