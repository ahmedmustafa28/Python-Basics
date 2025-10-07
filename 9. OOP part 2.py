#del keyword=is used to delete object properties/object itself.

class Student:
    def __init__(self,name):
        self.name = name
s1 = Student("Ahmed Mustafa")
print(s1.name)
del s1.name
print(s1.name)

#Private attributes and methods are meant to be used only
# within the class and are not accessible from outside the class.
#Conceptual implementations
class Account:
    def __init__(self,acc_no,acc_pass):
        self.__acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)
        #private attributes are accessible in the class.


acc1 = Account(12131,"ahmed12121")
print(acc1.__acc_pass)
#private attributes are not accessible outside the class.

#3.Inheritance: When one class(child/derived) derives the
# properties and methods of another class(parent/base).
#Types of inheritance: Single and multi level inheritance.
class Car:
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Prius(ToyotaCar):
    def __init__(self,type):
        self.type = type
car1 = Prius("Diesel")
print(car1.type)
car1.start()

# Multiple Inheritance:
class A:
    varA = "Welcome to class A."
class B:
    varB = "Welcome to class B."
class C(A,B):
    varC = "Welcome to class C."

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

#Super method is used to access methods of the parent class.
class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()
car1 = ToyotaCar("Prius","Electric")
print(car1.type)

#Class method is bound to class & receives the class as an
# implicit first argument.
#Note: Static methods can't access/modify class state &
# generally for utility.

class Person:
    name = "Ahmed Mustafa"

    # def change_Name(self,name):
    #     self.name = name

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("Ali Ahmed")
print(p1.name)
print(Person.name)

#Property: We use @property on any method in the class to
# use the method as a property.

class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"
std1 = Student(67,78,89)
print(std1.percentage)

std1.phy = 96
print(std1.percentage)

#4. Polymorphism:Polymorphism means the ability of the same
# function or method to behave differently based on the
# object or data type it is acting upon.
#When the same operator is allowed to have different meaning
# according to the context is called operator overloading.

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber (self) :
        print(self.real,"+",self.img,"i")

    def __add__(self, other): #dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)

    def __sub__(self, other):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1-num2
num3.showNumber()