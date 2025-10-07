#Q1:Define a Circle class to create a circle with radius r
#using the constructor.
#Define an Area() method of the class which calculates the area
# of the circle.
#Define a perimeter() method of the class which allows you to
# calculate the perimeter of the circle.

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def calc_area(self):
        area = (22/7) * self.radius ** 2
        print("Area of circle is",area)

    def calc_perimeter(self):
        perimeter = 2 * (22/7) * self.radius
        print("Perimeter of circle is",perimeter)

c1 = Circle(21)
c1.calc_area()
c1.calc_perimeter()

#Q2:Define an Employee class with attributes role,department, & salary.
#This class also contains a showDetail() method.
#Create an Engineer class that inherits properties from
# Employee & has additional attributes name and age.

class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.department = dept
        self.salary = salary

    def showDetails(self):
        print("Role :",self.role)
        print("Department :", self.department)
        print("Salary :", self.salary)

# e1 = Employee("Accountant","Finance","85000")
# e1.showDetails()

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75000")

eng1 = Engineer("Ahmed Mustafa","20")
eng1.showDetails()

#Q3:Create a class called Order which stores item & its price.
#Use dunder function __gt__() to convey that:
# order1 > order2 if price of order1 > price of order2.

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order("Chips",20)
odr2 = Order("Tea",15)

print(odr1>odr2)