# Set is the collection of the unordered items.
#Each element in the set must be unique and immutable.
#In sets list and dict are not used because they are mutable means in them the values can change .
"""
collection = {1,2,3,4,"hello","world","world"}

print(collection)   #duplicate values are ignored
print(type(collection))#Repeated elements stored only once, so it resolved 
print(len(collection))

collection = {}  #empty dictionary
collection = set() #empty set
#sets are mutable but in sets element are immutable

"""
# set methods
#set.add(),set.remove
"""
set1 = set()
set1.add(1)
set1.add(2)
set1.add(2)
set1.add(3)
set1.add("Sai")
set1.add((1,"sai"))
#set1.add([1,"sai"]) (unhashable means immutable which cannot change any value(dictionary,list,set) )
set1.remove(3)
#set1.remove(7) then it will show keyerror
print(set1)
"""
"""
#set.clear()
set1 = set()
set1.add(1)
set1.add(2)
set1.add(2)
set1.add(3)
set1.add("Sai")
set1.clear()#it will clear all the values in the set
print(len(set1))
"""

#set.pop()
"""
set1 = {"sai","jaggu", "om","suraj"}
print(set1.pop())
print(set1.pop())  #it will return the random value not in order wise
"""
#set.union()
"""
set1 = {1,2,3}
set2 = {4,5,3}
print(set1.union(set2))
print(set1)
print(set2)
"""

#set.intersection()
"""
set1 = {1,2,3}
set2 = {4,5,3}
print(set1.intersection(set2))
print(set1)
print(set2)
"""
"""
set1 = "abba"
print(len(set(set1)))
"""
"""
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))              #rough 
if (num1>num2 and num1>num3):
    print("num1 is greater:",num1)
elif (num2>num1 and num2>num3) :
    print("num2 is greater:",num2)
elif (num3>num1 and num3>num2) :
    print("num3 is greater:",num3)
else :
    print("numbers are equal")
"""

n = 151
for i in range (len(n)):
    print(i)