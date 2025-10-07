print("My name is Ahmed Mustafa.")
print(23+11)
# #Python is a simple and easy to understand programming langauge.
# # high level language,portable, developed by Guido van Rossum.
# # Print is a function. Print function is used to display output on console.

# Variables:

name = "Mustafa" # variable means memory location.
age= 20
price = 25.99
print("My name is : ", name)
print("My age is : ", age)
print("Price : ", price)
print(type(name))
print(type(age))
print(type(price))
# #Type is used to find the type of data used.

# # Data Types:

# Integers (+ve, -ve, 0) int
# String ('', "","""""")
# float (decimal values : 1.22 etc.)
# boolean (True and False)
# None (Where we want to store no value)
# a= None
# old = False
# print(type(a))
# print(type(old))
#
# #Python language is a case-sensitive language.
a = 2
b = 5
sum = a+b
print(sum)
# # using hash sign (#) to use single line comment.
# """
# Multi Line comment
# """
# # Arithmetic operators:
a = 5
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
#
# # Comparison/Relational operators:
#
a = 50
b = 20
print(a == b) #False
print(a != b) #True
print(a > b) #True
print(a >= b) #True
print(a < b) #False
print(a <= b) #False
#
# # Assignment Operator
#
num = 10
num+=10
print(num)
#
# # Logical Operators
#
a = 50
b = 30
print(not False)
print(not (a>b))
# #
val1= True
val2 = False
print("And operator : ", val1 and val2)
# #
val1= True
val2 = False
print("Or operator : ", val1 or val2)
#
# User Input:
# input() statement is used to accept values (using keyboard) from user.
# input() #result for input() is always a str.
# int(input()) #int
# float(input()) #float
# #
name= input("Enter your name: ")
age = int(input("Enter age: "))
marks = float(input("Enter Marks: "))
# #
print("Welcome ",name)
print("Age ",age)
print("Marks ", marks)