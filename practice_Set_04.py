#Q1: Store following word meanings in a python dictionary:
 #table : "a piece of furniture","list of facts and figures"
  #cat: "a small animal"

dictionary = {
    "table" : ["a piece of furniture","list of facts and figures"],
    "cat" : "a small animal"
}

print(dictionary)

#Q2: You are given a list of subjects for students. Assume one cassroom is required for 1 subject.
# How many classrooms are needed by all students.
# "python", "java", "C++", "python","javascript",
#"java","python","java","C++","C"

subjects = {"python","java","C++","python","javascript","java",
            "python","java","C++","C"}
print(subjects)
print("Total number of classrooms required are ",len(subjects))

#Q3: WAP to enter marks of 3 subjects from the user and store
# them in a dictionary. Start with an empty dictionary and add
# one by one. Use subject name as key and marks as value.

dictionary = {}
subject1 = eval(input("Enter marks of Chemistry:"))
subject2 = eval(input("Enter marks of Physics:"))
subject3 = eval(input("Enter marks of Mathematics:"))

dictionary.update({
    "Chemistry":subject1,
    "Physics" : subject2,
    "Mathematics" : subject3
})
print(dictionary)

#Q4: Figure out a way to store 9 & 9.0 as separate values in set.
# (You can take help of built-in data types)

values = {9,"9.0"} #first possible solution. Storing 9.0 as a string.
print(values)
values = {
    ("int",9),
    ("float", 9.0)
}
print(values)