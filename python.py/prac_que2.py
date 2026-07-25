#file . i/o
# create a new file "practice.txt" using python . Add the following data in it:
"""
        Hi everyone
        we are learning File i/o
        using Java.
        I like programming in Java.
"""
"""
with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File i/o ")
    f.write("using Java.\nI like programming in Java.")
"""
# WAF that replace all occurances of "java" with "python" in the above file.
"""
with open("practice.txt","r") as f:
    data = f.read()
new_data = data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)
"""

#search if the word "learning" exists in the file or not.
"""
with open("practice.txt","r") as f:
    data = f.read()
    if (data.find("learning") != -1) :
        print("found")
    else:
        print("Not found")
"""
#writing in function
"""
def check_for_word():
    with open("practice.txt","r") as f:
        data = f.read()
    if (data.find("using") != -1) :
        print("found")
    else:
        print("Not found")

check_for_word()
"""
# WAF to find in which line of the file does the word "learning" occur first.
# print -1 if word not found.
"""
def check_for_line():
    word = "5"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1
print(check_for_line())
"""

#From a file containing numbers separated by comma , print the count of even numbers.
"""
def count_even_num():
    count = 0
    with open("practice.txt","r") as f:
            data = f.read()
            num1 = data.split(",")  #split() in python removes the white spaces like tabs, \n , spaces , etc.
            for num in num1:
                num = int(num) # converting string to integer
                if(num%2 == 0) :
                    count+=1
    return count
print(count_even_num())
"""

# Easier way
"""
count = 0
with open("practice.txt","r") as f:
    data = f.read()
    num = data.split(",")
    for val in num:
        if(int(val)%2 ==0):
            count += 1

print(count)
"""

#OOPS in python
#create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.
"""  #my own
class Student:
    def __init__(self ,name ,marks):
        self.name=name
        self.marks=marks

    def avg_marks(self):
        avg = sum(self.marks)/len(self.marks)
        print("hi",self.name," Your Average marks is:" , avg)
        


s1 = Student("Sai",[98,97,96])
s1.avg_marks()

s2 = Student("Suraj",[92,87,86])
s2.avg_marks()

s3 = Student("Shilu",[96,95,99])
s3.avg_marks()
"""

#easier way
"""
class Student:
    def __init__(self ,name ,marks):
        self.name=name
        self.marks=marks

    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg score is:",sum/3) # here we have to check the space or it will run three times 

s1 = Student("Sai",[98,97,96])
s1.avg_marks()

s1.name = "Jaggu" #we can change the value of name directly through this
s1.avg_marks()
"""


#Create Account class with 2 attributes - balance & account no.
#Create methods for debit , credit & printing the balance.

"""
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc              # Watch here i get indentation error
        #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance =",self.get_balance())
    #credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was created")
        print("total balance =",self.get_balance())
            #balance
    def get_balance(self):
        return self.balance


acc1 = Account(1000,123456789)
acc1.debit(500)
acc1.credit(500)
"""


"""
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        i=0
        j=0
        for i in range(len(list1)):
            for j in range(len(list2)):
                list3=list1[i]+list2[j]
                return list3
s1=Solution()
s1.mergeTwoLists([1,2,3],[1,3,4])
"""
"""
num1 = "122"
if num1==num1[::-1]:
    print("palindrome")

else:
    print("not a palindrome")
"""
"""
n = input("Enter a string:")
num1 = n[::-1]
print(num1)
"""
"""
n1 = input("Enter a string1:")
n2 = input("Enter a string2:")
if n1==n2 :
    print("Both are equal")
else :
    print("not equal ")
"""
"""
string = "SAi is a good boy"
substring = "god"
if substring in string :
    print("present")
else:
    print("not present")
"""
"""
str1 = "Hello goodmorning"
str2 = "o"
count = 0
for i in str1:
   if i == str2 :
      count+=1
print(count)
"""
"""
n = "Helloworld"
print(n[:5])
"""
"""
def fact(num):
    fact = 1
    while num>0:
        fact*=num
        num-=1
    print(fact)

fact(6)
"""
"""
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact

num1=int(input("Enter the number:"))
result  = fact(num1)
print("The Factorial is :",result)
"""
"""
def check(num):
    if num%2==0 :
        print("Even")
    else :
        print("Odd")


n=int(input("Enter the number:"))
res=check(n)
"""
"""
def swap(a,b):
    return b,a

x,y = swap(5,2)
print(x,y)
"""
"""
n = int(input("Enter the number"))
res = lambda x: n*x
for i in range(1,11):
    print(n,"x",i,"=",res(i))
"""
n1 = int(input("Enter the number"))
n2 = int(input("Enter the number"))
greatest = lambda x,y: x if x>y else y
print("The Greatest number is :",greatest(n1,n2))