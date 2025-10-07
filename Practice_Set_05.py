#Q1: Print numbers from 1 to 100

i = 1
while i<=100 :
    print(i)
    i+=1

#Q2: Print numbers from 100 to 1

i = 100
while i>=1 :
    print(i)
    i-=1

#Q3: print the multiplication table of a number n.

i = 1
n = int(input("Enter any number: "))
while i<=10 :
    print(n*i)
    i+=1

#Q4: Print the elements of the following list using a while loop:
#(1,4,9,16,25,36,49,64,81,100)

numbers = (1,4,9,16,25,36,49,64,81,100)
idx = 0
while idx < len(numbers) :
    print(numbers[idx])
    idx+=1

#Q5: Search for a number x in this tuple using while loop:
#(1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)
i = 0
x = 36
while i < len(nums) :
    if nums[i] == x:
        print("FOUND at index",i)
        break
    else:
        print("Finding...")
    i +=1

#Q6: Print the elements of the following list using a for loop:
#(1,4,9,16,25,36,49,64,81,100)

elements = (1,4,9,16,25,36,49,64,81,100)
for val in elements :
    print(val)

#Q7: Search for a number x in this tuple using for loop:
#(1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)
x = 49
idx = 0
for el in nums:
    if el == x :
        print("FOUND at index",idx)
        break
    idx +=1

#Q8: using for and range():

# 1: Print numbers from 1 to 100:

for i in range(1,101):
    print(i)

# 2: Print numbers from 100 to 1:

for i in range(100,0,-1):
    print(i)

#3: Print the multiplication table of a number n.

n = int(input("Enter any number:"))
for i in range(1,11):
    print(n*i)

#Q9: WAP to find the sum of first n natural numbers.(using while)

num = int(input("Enter any number:"))
i = 1
total = 0
while i <= num :
    total+=i
    i+=1
print("The sum of first",num,"numbers is ",total)

#Q10: WAP to find the factorial of first n numbers.(using for):

n = int(input("Enter any number:"))
factorial = 1
for i in range(1,n+1):
    factorial*=i
    i+=1
print("factorial of ",n,"is ",factorial)