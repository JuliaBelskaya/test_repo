#Создать пять классов описывающие реальные
# объекты. Каждый класс должен содержать
# минимум три приватных атрибута, конструктор,
# геттеры и сеттеры для каждого атрибута, два метода.


#1
class Cat:
    def __init__(self, name, weight, age, hunger=0):
        self.__name = name
        self.__weight = weight
        self.__age = age
        self.__hunger = hunger

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
        
    @property
    def hunger(self):
        return self.__hunger

    @hunger.setter
    def hunger(self, hunger):
        self.__hunger = hunger

    def meow(self):
        print('Meeoow')

    def tired(self):
        self.__hunger -= 1
            
#2            
cat = Cat("Kitty", "15 kg", "3 years old")
print(cat.name)
cat.name = 'Simon'
print(cat.name)
print(cat.weight)
print(cat.age)
print(cat.hunger)
cat.hunger = 5
cat.meow()
cat.tired()
print(cat.hunger)


class Human:
    def __init__(self, name, job, pay):
        self.__name = name
        self.__job = job
        self.__pay = pay

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, job):
        self.__job = job

    @property
    def pay(self):
        return self.__pay

    @pay.setter
    def pay(self, pay):
        self.__pay = pay

    def rise_pay(self, pay):
        self.__pay = pay

    def greeting(self):
        print('Hello, world!!!')
        
human = Human("Jack", "A1QA", "5000$")
print(human.name)
print(human.job)
print(human.pay)
human.rise_pay = "7000$"
print(human.rise_pay)
human.greeting()



#3
class Figure:
    def __init__(self, name, colour, radius=3):
        self.__name = name
        self.__colour = colour
        self.__radius = radius
    
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def colour(self):
        return self.__colour
    
    @colour.setter
    def colour(self, colour):
        self.__colour = colour
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        self.__radius = radius
    
    def perimeter(self):
        P = 2 * 3.14 * self.__radius
        print(f'perimeter = {P}')
       
        
    def square(self):
        S = 3.14 * (self.__radius ** 2)
        print(f' square = {S}')
        
        
figure = Figure("Circle", "yellow")
print(figure.name)
print(figure.colour)
print(figure.radius)

figure.perimeter()
figure.square()

#4
class Rectangle:
    def __init__(self, width , height, radius):
        self.__radius = radius
        self.__width = width
        self.__height = height
       
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def square(self):
        S = self.__width * self.__height
        print(f'square = {S}')
        
        
    def diagonal(self):
        d = 2 * self.__radius
        print(f'diagonal = {d}')
        
        
figure = Rectangle(5, 6, 7)
print(figure.width)
print(figure.height)
print(figure.radius)

figure.square()
figure.diagonal()
              
              
#5
class Apple:
    def __init__(self, colour, form, taste):
        self.__colour = colour
        self.__form = form
        self.__taste = taste

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour):
        self.__colour = colour

    @property
    def form(self):
        return self.__form

    @form.setter
    def form(self, form):
        self.__form = form

    @property
    def taste(self):
        return self.__taste

    @taste.setter
    def taste(self, taste):
        self.__taste = taste
     
fruit = Apple("red", "sphere", "sweet")
print(fruit.colour)
print(fruit.form)
print(fruit.taste)
       
