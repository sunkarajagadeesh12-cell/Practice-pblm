"""
marks = [93.4, 83.3, 23.2, 43.2]
print(marks[3])  #we can print the character by using index value
print(marks[1])  #we can print the character by using index value
print(type(marks))
print(len(marks))
"""

#we can use different data types in a list
"""
student = ["Arjun", 93.2, 17, "Sai"]
print(student)
"""
#strings ar immuteble in python (which cannot change)
#list ar mutable in python   (which can change)

#example
"""
str = "hello" 
print(str[0])
str[0]="y"   #it cannot change the value
"""
"""
student = ["Arjun", 93.2, 17, "Sai"]
student[0] = "Jaggu"
print(student[0])
print(student)
""" 
"""
#list slicing (sub list )
marks = [82, 94, 76, 56, 48 ] 
print(marks[1:4])
print(marks[0:])
print(marks[-4:-1])
"""

#list methods
#list.append
#list = [2, 1, 3,]
"""
print(list.append(7))
print(list)       #it will add the input variable in the list(mutating the list)
#list.sort
print(list.sort())
print(list)       #it will arrange in asending order

print(list.sort(reverse=True))
print(list)
"""
list = ['g', 'f', 'd', 's','a']
"""
print(list.sort())
print(list)

#list.reverse
print(list.reverse())
print(list)
"""
#list.insert
"""
print(list.insert(2,'r'))
print(list)  #we can insert any value in index by using insert function

#list.remove
print(list.remove('f'))
print(list)  #it can remove the any variable in the list

#list.pop
print(list.pop(0))
print(list)"""