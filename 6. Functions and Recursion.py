#Functions in python are block of statements that perform
# a specific task.

a = eval(input("Enter 1st number:"))
b = eval(input("Enter 2nd number:"))

#Function Definition
def addition (a,b): #parameters
    s = a+b
    return s
print("Addition:",addition(a,b)) #arguments

def subtraction (a,b):
    s = a-b
    return s
print("Subtraction:",subtraction(a,b))

def multiplication (a,b):
    s = a*b
    return s
print("Multiplication:",multiplication(a,b))
#
def division (a,b):
    s = a/b if b !=0 else "Error"
    return s
print("Division:",division(a,b))
#
def modulus (a,b):
    s = a%b if b !=0 else "Error"
    return s
print("Modulus:",modulus(a,b))

def print_hello():
    print("Hello")
output = print_hello()
print(output)

#Average of 3 numbers:

def avg(num1,num2,num3):
    average = (num1+num2+num3)/3
    return average
print(avg(1,2,3))

#Built-in Functions:
#print(),len(),type(),range() #these are built-in functions.
#User defined function means functions which are built by user.
#Assigning a default value to parameter, which is used when no
# argument is passed.

def cal_prod (a=1,b=1) :
    print(a*b)
    return a*b
cal_prod(4,5)

#Recursion: When a function calls itself repeatedly.

def show(n):
    if n == 0: #Base case
        return
    print(n)
    show(n-1)
show(5) #5 4 3 2 1

def calc_fact (n):
    if n == 0 or n == 1:
        return 1
    return n * calc_fact(n-1)
fact = calc_fact(5)
print(fact)

def calc_fib (n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else:
        return calc_fib(n-1) + calc_fib(n-2)
fib = calc_fib(5)
print(fib)