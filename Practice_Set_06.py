#Q1: WAF to print the length of a list.(list is the parameter)

nums = [1,2,3,4,5,6]
def print_len (list) :
    print(len(list))
print_len(nums)

#Q2: WAF to print the elements of a list in a single line.
# (list is the parameter.)

fruit = ["apple","banana","mango","litchi","grapefruit"]
def print_list (list) :
    for item in list :
        print(item,end = " ")
print_list(fruit)

#Q3: WAF to find the factorial of n.(n is the parameter)

def calc_fact (n) :
    fact = 1
    for i in range(1,n+1):
        fact *= i
        i += 1
    print(fact)
calc_fact(5)

#Q4: WAF to convert USD in PKR.

def converter (usd_val) :
    pkr_val = usd_val * 280
    print(pkr_val)
converter(10)

#Q5: WAF which takes a number from user and tells
# whether it's even or odd

#
def even_odd (a) :
    if a % 2 == 0:
        print("EVEN")
    elif a % 2 != 0:
        print("ODD")
    else:
        print("INVALID NUMBER.")
even_odd(8)

#Q6: Write a recursive function to calculate the sum of first
# n natural numbers.

def calc_sum (n) :
    if n == 0:
        return 0
    return n + calc_sum(n-1)
sum = calc_sum(10)
print(sum)

#Q7: Write a recursive function to print all elements in list.
# Hint: use list and index as parameters.

def print_list (list,idx=0) :
    if idx == len(list) :
        return
    print(list[idx])  # print the element at idx
    print_list(list,idx + 1)  # recursive call

cities = ["Hyderabad", "Karachi", "Lahore", "Sukkur", "Islamabad"]

print_list(cities)



