#Python can be used to perform operations on a file(read and write data)
#Text files: .txt,.docx,.log etx
#Binary files: .mp4, .mov, .png, .jpeg etc

#We have to open a file before reading or writing.

#"r"= open for reading (default)
# "w"= open for writing, truncating the file first
# "x" = creates a new file and open it for writing
#"a"=open for writing, appending to the end of the file if it exists.
#"b" = binary mode
# "t" = text mode (default)
# "+" = opens a disk file for updating (reading and writing)

#Reading a file:

f=open("demo.txt","r")
data = f.read() #we can also print particular no of characters
data = f.readline() #read line by line
print(data)
f.close()

#Writing to a file:

f=open("demo.txt","a")
f.write("I want to learn OOP tomorrow.")
f.write("Then I'll move to libraries.")
f.close()

f= open("demo.txt","r+") #read and overwrite the file in starting.
f.write("abc")
f.close()

f= open("demo.txt","w+") #read+overwrite, truncate.
f.write("abc")
f.read()
f.write("abc")
f.close()

f= open("demo.txt","a+") #read and append,pointer in the end.
f.write("abc")
f.read()
f.write("abc")
f.close()

#With syntax:

with open("demo.txt","r") as f :
    data = f.read()
    print(data)
with open("demo.txt","w") as f :
     f.write("New data")

#Deleting the file: (using the os module)
#Module(like a code library) is a file written by another
# programmer that generally has a function we can use.

import os
os.remove("demo.txt")