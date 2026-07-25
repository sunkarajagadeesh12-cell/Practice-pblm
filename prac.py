"""
a = "Sai"                #concatinate in strings 
len1 = len(a)
print(len1)
b = "Jaggu"
len2 = len(b)
print(len2)
final_str = a + " " + b
print(final_str)
print(len(final_str))
"""
"""
        #indexing in string
str = "apna college"
print(str[2])
"""
"""
#slicing in string
str = "jagadeesh"
print(str[0:3])
print(str[1:])
print(str[-9:-1])
"""
"""
# #string function
# #1)endswith
# str = "Apna college"
# print(str.endswith("ego"))
# 2)captalize
str = "saijaggu"
print(str.capitalize())
"""
"""
str = "sai is doing well"
str = str.capitalize()
print(str.capitalize())
print(str)
"""
"""
#Replace
str = "My name is sai"
print(str.replace("sai","Jaggu"))
"""
"""
#find
str = "My name is Sai"
print(str.find("is"))
"""
"""
#count
str = "Sai Venky Jaggu"
print(str.count("a"))
"""

#list slicing
"""
marks = [94,96,99.5,"Sai"]
print(marks[-4:])
"""
#list features
# list.append()
"""
list1 = [1,3,5,4]
list1.append(7)
print(list1)
"""
#list.sort
"""
list1 = [1,3,2,4,6]
list1.sort()
print(list1)
"""
#list.reverse
#here split function works in the strings not on list
"""
list1 = "Sai is doing well in exams"
word = list1.split()
word.sort()
print(word)
"""
# list1 = ['g','h','t']
# print(list1.pop(0))
# print(list1)  
# list1 = [1,3,2,4,6]
# print(list1.index(2))
# info = {
#     "key" : "value",
#     "name" : "apnacollege",
#     "learner" : "Sai",
#     "age" : "18",
#     "is_adult" : "True",
#     "marks" : "94.3",
#     "subjects" : ["python", "c", "java"],
#     12 : 29 #we can change our key value into integer 
# }
# info["name"] = "SaiJaggu"   #we can change the value 
# info["surname"] = "khapra"  #we can add the value
# print(info["name"])
# print(info["age"])
# print(info["marks"])
# print(info)

"""
student = {
    "name" : "Sai",
    "Subjects" : {
       "phy" : 94,
        "math" : 99,
        "eng" : 90
}
}
print(list(student.keys()))
print(len(student.keys()))
print(type(list(student)))
print(student)
"""
"""
i = 0
n = 1
while (i<=10) :
    n = i + n
    i = i+1
total = n/2
print(total)
"""
"""
i = 0
total = 0

while i <= 10:
    total = total + i
    i = i + 1

average = total / 2

print("Total =", total)
print("Average =", average)
"""
"""
a = 0
b = 1
i = 1
d = 0
while (i<=10) :
    print(a)
    d = d + a         #At last the total value comes with this
    c = a + b
    a = b
    b=c
    i = i+1
print(d)
"""
"""
class Solution(object):
    nums = [1,2,1]
    def getConcatenation(self, concat, nums):
        self.concat = nums*2
        print("The array ans is formed :")

s1 = Solution()
print(s1.concat)
"""
"""
class Solution(object):
    def __init__(self):
        self.nums = [1, 2, 1]
        self.concat = None

    def getConcatenation(self):
        self.concat = self.nums * 2
        print("The array ans is formed :", self.concat)

s1 = Solution()
s1.getConcatenation()
print(s1.concat)





class Solution(object):
    def __init_(self,nums):
        self.nums = [1,2,3]
        self.concat = none

    def getConcatenation(self,nums):
        self.concat = self.nums * 2
        print("The array ans is formed :")

s1 = Solution()
s1.getConcatenation()
print(s1.concat)




class Solution(object):
    def findWordsContaining(self, words, x):
       self.words = words
       self.x = x
       print("It contains in :")

s1 = Solution()
s1.findWordsContaining(["sai","jaggu","suraj","oma"],'a')
print(s1.words.index())



"""




"""
class Solution(object):
    x = 0
    def finalValueAfterOperations(self, operations):
        self.operations = operations
        
        for op in self.operations:
            if '+' in op:
                self.x += 1
            else:
                self.x -= 1
        
        return self.x
    
s1 = Solution()
s1.finalValueAfterOperations(["++X","++X","X++"])
print(s1.x)
"""

class Solution:
    def isPalindrome(self, x):
        list1 = list(str(x))
        copy_list = list1[:]
        copy_list.reverse()
        return copy_list == list1
    
s1 = Solution()
print(s1.isPalindrome(121))

#dynamic time complexity means taking a same variable and doing operations of loop in it.