#python can be used to perform operations on a file.
#types of all files
#1)text files :.txt,.docx,.log etc.
#2)binary files : .mp4,.mov,.png,.jpeg etc.
"""
we have to open a file before reading or writing.
f = open("file_name","mode")
file_name = sample.txt,demo.docx
mode = read mode,write mode
data = f.read()
f.close()
"""
"""
f = open("basic","r")
data = f.read()
print(data)      
print(type(data))
f.close()
"""
#different functions and meanings
"""
'r'-open for reading 
'w'-open for writing , truncating the file first(overwrite - all the data  will delete first and then it will store the updated data )
'x'-create a new file and open it for writing
'a'-open for writing , appending to the end of the file if it FileExists
'b'-binary mode 
't'-text Mode
'+'-open a disk file for updating (reading and writing)
'r++'-open for reading and writing
"""
#reading a file 
#data = f.read()  #reads entire file
#data = f . readline()  #reads one line at a time
"""
f = open("basic","r")
data = f.read(5) # here we can print the values which we needed only
print(data)      
print(type(data))
f.close()
"""
"""
f = open("basic","r")
data = f.readline() # it will print the full line
print(data)      
print(type(data))
f.close() 
"""
"""
f = open("basic","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
"""
# if there is no data in the next line then it will print an empty space


#  writing to a file
#'a'- add at the end (append)
"""
f = open("basic","a")
f.write("\nI am an ai engineer")
f.close()
"""
# if there is no file found then it will create 
"""
f = open("sample.txt","w")
f.close()
"""
#if we want to overwrite in the file we use r+
"""
f = open("basic","r+") # Here we can read and overwrite the existing data
f.write("hi") # No truncate
print(f.read())
f.close()
"""
"""
f = open("basic","w+") # Truncate
print(f.read())
f.write("Hi my name is Sai")# Now we can write and update the file
f.close()#it will truncate the file and the file will empty
"""
"""
f = open("basic","a+")# It will not overwrite but it will append
print(f.read())# The stream is positioned at the end of the file
f.write("Hi my name is Sai")# It will not print any thing at the terminal
f.close()# And it will print the same sentence from the end point
#no truncate
"""

# with syntax # alias = same name(f)
#[with open("demo.txt","a") as f:
#data = f.read()]
"""
with open("basic","r") as f:
    data = f.read()
    print(data)
    #f.close is not necessary because with function will automatically close the file
with open("basic","w") as f:
   f.write("my age is 18")
# No it will print the old data in the terminal and new data in the file
"""
# Deleting a File
"""
using the os module 
module (like a code library) is a flie written by another programmer that generally has a functions we can use
"""
"""
f = open("sample.txt","w")
f.close()
"""
# if we want to install the module 
#then pip or pip3 install tenserflow\
"""
import os # this is preinstalled
os.remove("sample.txt")
#so it will remove the 
"""
