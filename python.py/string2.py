# String is data type that stores a sequence of character
#Escape sequence character
"""

str1 = "This is sai.\nWe are trying to win the upcoming games."
print(str1)
"""
#Concatination
"""

a = "hello"
len1 = len(a)
print(len1)
b = "bhai"
len2 = len(b)
print(len2)
final_str = b+" "+a
print(final_str)
print(len(final_str))
"""

#indexing
"""

str = "apna college"
ch = str[4]
print(ch)
"""
#Slicing
#positive index
"""
str = "apna college"
print(str[5:len(str)])
print(str[:4])#[0:4]
"""
#negative index
"""
str = "Sai jaggu"
print(str[-5:])
"""

#string function
#endswith
str = "Sai is doing well"
print(str.endswith("Sai"))

#capitalize

str = "sai is doing well"
str = str.capitalize()
print(str.capitalize())
print(str)

#Replace


str = "sai is doing well"
print(str.replace("i","o"))#("python", "Java")

#find
str = "sai is doing well"
print(str.find("i"))#if the letter is not exist it shows -1

#count
str = "sai is doing well"
print(str.count("s"))

