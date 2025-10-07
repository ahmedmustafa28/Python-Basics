#loops are used to repeat instructions. two types while and for loops.
#While Loop:

count = 1
while count<=5 :
    print("Hello")
    count+=1
print(count)

i = 1
while i<=1000:
    print(i)
    i+=1
print("Loop Ended")

i = 5
while i>=1 :
    print(i)
    i-=1

#Break keyword is used to terminate the loop when encountered.

i = 1
while i <=5 :
    print(i)
    if i == 3 :
        break
    i+=1

#Continue keyword terminates execution in the current iteration
# and continues execution of the loop with the next iteration.

i = 1
while i <=10 :
    if i%2 != 0 :
        i += 1
        continue #skip
    print(i)
    i += 1

#For Loop:
#for loops are used for sequential traverse. for traversing list,string,tuple,etc.

nums = [1,2,3,4,5]
for val in nums :
    print(val)
veggies = ["potato","brijal","ladyfinger","cucumber"]
for val in veggies :
    print(val)

tup = (1,2,3,4,2,8,9)
for num in tup:
    print(num)

str = "AhmedMustafa"
for char in str :
    print(char)

#We can use optional else in while loop and for loop.

str = "AhmedMustafa"
for char in str :
    if char == 'd':
        print("a found")
        break
    print(char)
else:
    print("Loop ended")

#range() : Range function returns a sequence of numbers,
# starting from 0 by default, and increments by 1 by default,
# and stops before a specified number.

for el in range(5): #range(stop)
    print(el)
for el in range(2,10): #range(start,stop)
    print(el)
for el in range(2,10,2): #range(start,stop,step)
    print(el)

#Pass Statement: pass is a null statement that does nothing.
# It is used as a placeholder for future code.

for i in range(5):
    pass
print("Some useful work")
