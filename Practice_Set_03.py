#Q1: WAP to ask the user to enter 3 names of their favorite movies and store them in a list.

fav_movies1= input("Enter 1st name of your favorite movie: ")
fav_movies2 = input("Enter 2nd name of your favorite movie: ")
fav_movies3 = input("Enter 3rd name of your favorite movie: ")

list1 = [fav_movies1,fav_movies2,fav_movies3]
print(list1)

#Q2: WAP to check if a list contains a palindrome of elements

list1 = [1,2,3,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()
print(copy_list1)
if list1 == copy_list1:
    print("Palindrome.")
else:
    print("Not Palindrome.")

#Q3: WAP to count the number of students with the grade in the following tuple

grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

#Q4: Store the above values in a list and sort them from "A" to "D".

grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)