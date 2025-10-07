#Dictonaries are used to store data values in key:value pairs.
#They are unordered, mutable, and don't allow duplicate keys.
from os import lstat

info = {
    "key" : "value",
    "name" : "Mustafa",
    "cgpa" : 3.11,
    "age" : 20
}
info["name"] = "Ahmed Mustafa"
info["surname"] = "Bhurgri"
print(info)

#Nested Dictionaries:

student = {
    "name" : "Ahmed Mustafa",
    "subjects" :  {
    "Chemistry" : 78,
    "Physics" : 65,
     "Maths" : 91,
    "English" : 63
}
}
print(student["subjects"]["Chemistry"])

student = {
    "name" : "Ahmed Mustafa",
    "subjects" :  {
    "Chemistry" : 78,
    "Physics" : 65,
     "Maths" : 91,
    "English" : 63
}
}

# Dictionaries Methods:

print(student.keys()) #returns all keys
print(len(student)) #returns length of keys
print(list(student.keys())) #Typecasting.
print(len(list(student.keys())))
print(student.values()) #returns all values
print(student.items()) #returns all (key,value)pairs as tuples
print(student.get("name")) #returns the key according to value
student.update({"city":"Dadu"}) #inserts the specified items to the dictionaries.
print(student)

#SET:
#Set is the collection of the unordered items(no index).
#Each element in the set must be unique and immutable.
#Every data type is stored in set except list and dictionary.

collection = {1,2,2,3,3,4,"hello","world"}
print(collection)
print(type(collection))
#set ignores duplicate/repeated values.
null_set = set
var = {} #empty set
print(type(null_set))

# #Set Methods:

collection.add(5) #adds an element
print(collection)
collection.remove(3) #removes an element
print(collection)
collection.pop() #removes a random value
print(collection)
collection.clear() #empties the set
print(collection)

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
