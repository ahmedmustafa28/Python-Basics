#Q1: Create a new file "practice.txt" using python. Add the following data in it:

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O"
           "\nusing Java\nI like programming in Java")


#Q2: WAF that replaces all occurrence of "java" with "python" in above file.

def rep_java():
    with open("practice.txt", "r") as f:
        data = f.read()
        new_data = data.replace("Java", "Python")
        print(new_data)

    with open("practice.txt","w") as f:
        f.write(new_data)

#Q3: Search if the word "learning" exists in the file or not.

def check_for_data() :
    word  = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if data.find(word) != -1 :
            print("FOUND")
        else:
            print("NOT FOUND")
check_for_data()

#Q4: WAF to find in which line of the file does the word "learning" occur first.
# print -1 if word not found.

def check_for_word ():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if word in data:
            print("FOUND")
        else:
            print("NOT FOUND")
check_for_word()

def check_for_line() :
    word = "Learning"
    with open("practice.txt","r") as f:
        data = True
        line_no = 1
        while data :
            data = f.readline()
            if word in data:
                print(line_no)
                line_no += 1
    return -1
check_for_line()

#Q5: From a file containing numbers separated by comma,
# print the count of even numbers.

count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums :
        if int(val) % 2 == 0:
            count += 1
print(count)
