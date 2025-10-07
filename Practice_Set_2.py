#Q1: WAP to input user's first name and print it's length.
first_name = input("Enter your first name: ")
print("the length of string is ",len(first_name))
#Q2: WAP to find the occurrence of '$' in a string.
str = "Ahmed$"
print(str.count("$"))
#Q3: Grade students based on marks. (Conditional statement)

marks = eval(input("Enter your marks: "))
if 80<marks >= 90 :
    print("Grade A+")
elif 70<marks >= 80:
     print("Grade A")
elif 60<marks >= 70:
     print("Grade B+")
elif 50<marks >= 60:
     print("Grade B")
elif 40<marks >= 50:
    print("Grade C")
elif marks < 50 :
    print("FAIL.")
#Q4: WAP to check if a number entered by user is even or odd.

num = int(input("Enter a number: "))
if num%2 == 0 :
    print("EVEN.")
else:
    print("ODD.")

#Q5 : WAP to find the greatest of 3 numbers entered by user.

num1 = eval(input("Enter 1st Number: "))
num2 = eval(input("Enter 2nd Number: "))
num3 = eval(input("Enter 3rd Number: "))

if num1 > num2 :
    print("Number 1 is greater.")
elif num2 > num3 :
    print("Number 2 is greater.")
elif num3 > num1 :
    print("Number 3 is greater.")
else:
    print("Invalid Number.")

#Q6: WAP to check if a number is a multiple of 7 or not.

num = int(input("Enter any number: "))
if num % 7 == 0 :
    print(num," is a multiple of 7.")
else:
    print(num," not a multiple of 7.")

color = input("Enter any color: ")
color= color.lower()
if color == "red" :
    print("DANGER AHEAD!")
elif color == "green" :
    print("SAFE!")
elif color == "yellow" :
    print("NORMAL!")
else:
    print("Invalid Color..")