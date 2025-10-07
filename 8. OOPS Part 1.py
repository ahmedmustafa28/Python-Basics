#To map with real world scenarios, we started using objects in code.
# This is called object-oriented programming.
#redundancy (decreases) and reusability (increases).
#Class is a blueprint for creating objects.

class Student :
    name = "Ahmed Mustafa"
s1 = Student()
print(s1.name)

class Car:
    color = "Black"
    brand = "Toyoto"
car1 = Car()
print(car1.color)
print(car1.brand)

# __init__ Function or Constructor:
#All classes have a function called __init__(), which always
# executed when the object is being initiated.

class Student :
    #Default constructors
    def __init__(self):
        pass

    #parameterized constructor
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("Adding new student in Database..")

s1 = Student("Ahmed",78)
print(s1.name,s1.marks)

s2 = Student("Mustafa",89)
print(s2.name,s1.marks)

#The self parameter is a reference to the current instance of
# ths class, and is used to access variables that belong to
# the class.
#Attributes:
#There are two types of attributes named as Class Attributes
# and Object Attributes.
#Class is collection of attributes and methods.
#Methods are functions that belong to objects.

class Student :

    def __init__(self,fullname):
        self.name = fullname
    def hello(self):
        print("Welcome Student",self.name)

s1 = Student("Ahmed")
s1.hello()

#Methods that don't use the self parameter(work at class level)
# are known as Static methods.
#Decorators allows us to wrap another function in order to
#extend the behavior of the wrapped function, without
# permanently modifying it.

class Student:
    @staticmethod
    def college():
        print("ABC College")
s1 = Student()
s1.college()

#Pillars of OOP:

#1. Abstraction: Hiding the implementation details of a class
#and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started...")
car1 = Car()
car1.start()

#2. Encapsulation: Wrapping data and function into a single unit(object)


