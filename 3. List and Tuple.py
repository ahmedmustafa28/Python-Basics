#List is a built-in data type that stores set of values.
#It can store elements of different types (Integer, float, string,etc)

marks = [23,24,"Marks",32.4]
print(marks)
print(type(marks))
marks[0]=33
print(marks[0])
print(len(marks))

#String is immutable(not changeable) in python while lists are mutable(changeable).
str = "hello"
print(str)
str[0] = "a"

student = ["Mustafa",87.4,20,"Dadu"]
print(student)

# LIST SLICING:

marks = [85,94,76,63,48]
print(marks[:4])
print(marks[-3:-1])

#List Methods:

list = [2,1,3]
list.append(4) #adds one element at the end.Mutating the list.
print(list)
list.sort() #sorts in ascending order.
print(list)
list.sort(reverse=True) #sorts in descending order.
print(list)
list.reverse() #reverses list
print(list)
list.insert(2,9) #insert element at index.
print(list)
list.remove(1) #removes first occurrence of element.
print(list)
list.pop(2) #removes element at index.
print(list)

#Tuple is a built-in data type that lets us create immutable sequences of vales.
tup = (1,2,3,4)
print(type(tup))
print(tup[1])
# tup[0] = 9 not allowed.
tup = (1,)
print(tup)
print(tup[0:3]) # SLicing
#Tuple Methods:
tup = (2,1,3,1)
print(tup.index(1)) #returns index of first occurrence.
print(tup.count(1)) #counts total occurrences.
