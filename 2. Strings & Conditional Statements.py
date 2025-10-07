# String is a data type that stores a sequence of characters.

str1 = "This is a string."
str2 = 'ApnaCollege'
str3= """This is a string."""

# Above three are methods to create/initialize a string.

str1 = "This is a string.\nWe are creating it in python."
print(str1)

# escape sequence characters are special characters used for formatting.

# String Functions:

#1. Concatenation:
str1 = "This is a string."
str2 = 'ApnaCollege'
finalStr= str1+str2
print(finalStr)

#Length of String (len(str)):

str1 = "This is a string."
print(len(str1))

#Indexing: Number of position, starts with 0, spaces/special characters are also given indx.

str = "Apna College"
# str[0] is A, str[1] is p....
# str[0] = B Not allowed
print(str[4])

#Slicing (Accessing parts of a string):
#str[ starting index : ending index ]

str = "Apna College"
print(str[:4]) #[0:4]
print(str[5:]) #[5:len(str)]

# str = "apple"
# print(str[-3:-1])

str = "i am a coder."
print(str.endswith("er.")) #returns true if string ends with substr.
print(str.capitalize()) #capitalizes 1st character.
print(str.replace("e","o")) # replaces all occurrences of old with new.
print(str.find("c")) #returns 1st index of 1st occurrence.
print(str.count("o")) #counts the occurrence of substr in string.

# Conditional Statements:

# if-elif-else (Syntax)

age = 20
if True:
    print("Can vote and drive.")

light = "Green"
if light == "red" :
    print("Stop!")
elif light == "Green" :
    print("Go!")
elif light == "Yellow" :
    print("Wait!")
# The difference between if and elif statement is the if will always chcek for the condition but elif will check the condition only when the if statement is false.

light = "Pink"
if light == "red" :
    print("Stop!")
elif light == "Green" :
    print("Go!")
elif light == "Yellow" :
    print("Wait!")
else:
    print(" Light is broken.")

# usage of tab space/four spaces is called indentation means proper spacing.

# statement within statement is called nesting.

age = 79
if age >=18 :
    if age >=80 :
        print("Can not drive.")
    else:
        print("Can drive.")
else:
    print("Cannot Drive.")