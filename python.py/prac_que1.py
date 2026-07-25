#variables and data types

# Write a program to input 2 numbers & print their sum.
"""

num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))
sum = num1 + num2
print(sum)
"""


#input side of a square and print its area
"""

side = int(input("Enter the side"))

Area = side*side 
print( "Area is :",Area)
"""


#input 2 floating num and print their average
"""

num1 = float(input("Enter the first num"))
num2 = float(input("Enter the second num"))
Average = (num1+num2)/(2)
print("The average of the two num are:", Average)
"""

#strings and conditional statements

#input 2 num and print is num 1 s greater than or equal to num 2 or print false
"""

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
if num1>=num2 :
    print(True)
else :
    print(False)
    """
#input the name and print its length
"""
name = input("Enter your name")
print("Length of your name is:",len(name))
"""

#find the occurance of $ in a string
"""
str = "Hi i $ am the $ symbol"
print(str.count("$"))
"""

#check if a number entered by the user is odd or even
"""
num = int(input("Enter the number"))
if (num%2==0):
    print("Number is even")
else :
    print("Number is odd")
    """

#find the greatest of 3 numbers entered by the user 
"""
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))
if (num1>num2 and num1>num3) :
    print("num1 is the greatest number")
elif (num2>num1 and num2>num3) :
    print("num2 is the greatest number")
elif (num3>num1 and num3>num2) :
    print("num3 is the greatest number")
else :
    print("numbers are equal")
    """

#check if a number is a multile of 7 or not
"""
num = int(input("Enter the number"))
if (num%7 == 0)  :
    print("Number is multiple of seven")
else :
    print("Number is not a multiple of seven")
    """
"""
#lists and tuples
#enter names of their 3 favorite movies and store them in a list
#1st method
movies = []
mov1 = input("Enter the first movie")
mov2 = input("Enter the second movie")
mov3 = input("Enter the third movie")
print(movies.append(mov1))
print(movies.append(mov2))
print(movies.append(mov3))
print(movies)

#2nd method
movies = []
mov = input("Enter the first movie")
print(movies.append(mov))
mov = input("Enter the second movie")
print(movies.append(mov))
mov = input("Enter the third movie")
print(movies.append(mov))
print(movies)

#third method
movies = []
movies.append(input("Enter the first movie"))
movies.append(input("Enter the second movie"))
movies.append(input("Enter the third movie"))
print(movies)
"""
"""
#check if a list contains a palindrome of elements    (palindrome = racecar) #first to last order is same
#corrected method
list = [1, 2, 3, 2, 1]
copy_list = list.copy()
copy_list.reverse()
if (copy_list == list):
    print("The numbers are palindrome")
else:
    print("The numbers are not a palindrome")
"""
#easier way
"""
list = [1,2,1]
copy_list = list.copy()
copy_list.reverse()
if (copy_list == list):
    print("Palindrome")
else :
    print("Not a palindrome")
"""
#write a prog to count the number of students with the a grade in the following tuple
"""
tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))

#store the above values in a list and sort them from a to d
list = ["C", "D", "A", "A", "B", "B", "A"]
print(list.sort())
print(list) 
"""

#dictionary and sets

#store the following word meanings in a python dictionary
"""
mean = {
    "table" : ["a piece of furniture , list of facts & figures"],
    "cat" : "a small animal"
    }
print(type(mean))
print(mean)
"""

#you are given a list of subjects for students assume one classroom is required for 1 subject. How many classrooms are needed by all students .
#"python three times","java three times","c++ two times","c one time","javascript one time"
"""
list1 = {"python","python","python","python","java","java","java","c++","c++","c","javascript"}
print(type(list1))
print(len(list1))
"""

#wap to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
#my own
"""
dict = {}
dict.update({"eng":"92"})
dict.update({"math":"98"})
dict.update({"science":"94"})
print(dict)
print(type(dict))
"""
#correct and easy
""" 
marks = {}
x = int(input("Enter physics marks :"))
marks.update({"physics" : x})
x = int(input("Enter maths marks :"))
marks.update({"maths" : x})
x = int(input("Enter english marks :"))
marks.update({"english" : x})
print(marks)
"""

#figure out a way to store 9 & 9.0 as separate values in the set.
#method1
"""
values = {9,"9.0"}
print(values)
"""
#method2(by build-in data types)
"""
set1 = {
    ("float",9.0),
      ("int", 9)
      }
print(set1)
"""

#loops 
#while loop
#print numbers from 1 to 100
"""
count = 1
while count<=100:
    print(count)
    count+=1
    """
#print numbers from 100 to 1
"""
count = 100
while count>=1:
    print(count)
    count -= 1
    """

#print the multiplication of table of q number n.
"""
i = 1
n = int(input("Enter the number))
while i<=10:
    print(n,"*",i,"=", i*n)
    i+=1
"""
#print the elements of the following list using a loop.
"""
count = 1
while count <=10:
    print(count*count)
    count+=1
    """

#search for a number x in this tuple using loop.
"""
tup = (1,4,9,16,25,36,49,63,81,100,36) #traverse (travel)
x = 36
i = 0
while i < len(tup):
    if(tup[i] == x) :
        print("Found at idx", i)
        i += 1
    else:
        print("finding...")
    i += 1
    """

#using for loop 
#print the elements of the following list using a loop
#[1,4,9,16,25,36,63,81,100]
"""
num = [1,4,9,16,25,36,63,81,100]
for el in num :
    print(el)
    """
#search for a number x in this tuple using loop 
#[1,4,9,16,25,36,63,81,100]
#this type of problem called as linear search
"""
num = [1,4,9,16,25,36,63,81,100]
x = 25
idx = 0

for el in num:
    if (el == x):
        print("number found at index",idx)
    idx += 1

else:
    print("end")
    """

#range()
#print numbers from 1 TO 100.
"""
for i in range(1,101):
    print(i)
    """
#print numbers from 100 to 1.
"""
for i in range(100,0,-1):
    print(i)
    """
#print the multiplication table of a number n.
#8 table
"""
for i in range(8,81,8):
    print(i)
"""
    #method 2
"""
n = int(input("Enter number:"))
for i in range(1,11):
        print(n*i)
"""

#main questions
#WAP to find the sum of first n numbers.(using while)
#using for in range
"""
n = 5

sum = 0
for i in range(1,n+1):
    sum = sum + i

print("total sum =",sum)
"""
"""
#using while loop
n = 3
sum = 0
i = 1
while i<=n:
    sum += i
    i+=1

print("total sum :",sum)
"""

#WAP to find the factorial of first n numbers.(using for loop)

"""
n = 5
fact = 1
i = 1
for i in range(1,n+1):
    fact *= i


print("Factorial is:",fact)
"""

"""
#using while loop

n = 5
fact = 1
i = 1
while i<=n:
    fact*=i
    i+=1

print("factorial is :", fact)
"""

#functions
#average of three values
#method1
"""

def avg_val(a,b,c):
    return (a+b+c)/(2)

value1=avg_val(1,2,3)
print(value1)
value2=avg_val(4,2,3)
print(value2)
value3=avg_val(1,5,3)
print(value3)
"""
#method 2(simple and reliable)
"""
def avg_val(a,b,c):
    avg = (a+b+c)/(2)
    print(avg)
    return avg

avg_val(1,2,3)
avg_val(4,2,3)
avg_val(1,5,3)

"""
"""
#functions problems
#WAF to print thhe length of a list . (list is the parameter)
cities = ["delhi","pune","mumbai","chennai","ladakh"]
fruit = ["banana","apple","mango","cheeko"]
def print_len(list):
    print(len(list))

print_len(cities)
print_len(fruit)
"""
#WAF to print the element of a list in a single line.
"""
fruit = ["banana","apple","mango","cheeko"]
def print_list(list):
   for ele in list:
       print(ele,end = " ")

print_list(fruit)
"""
#WAF to find the factorial of n.
"""
def calc_fact(n):
    fact = 1
    for i in range(1,n+1) :
        fact *= i
    print(fact)

calc_fact(5)
calc_fact(9)
print_list(fruit)
"""
"""
 #WAF to convert usd to inr
def con_currency(usd_val):
    inr_val = usd_val*90.89  

con_currency(10)
con_currency(100)
con_currency(1000)
"""
"""
def nat_num(i) :
    if i%2==0:
        str1 = "EVEN"
        print(str1)
    else :
        str2 = "ODD"
        print(str2)

nat_num(1385)
"""

   # recursions
   #write a recursive function to calculate the sum of the first n natural numbers.
"""
def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)
"""
#write a recursive function to print all element in a list. 
"""
fruit = ["banana","apple","mango","cheeko"]
def print_list(list , idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

print_list(fruit)
"""

"""
num1 = float(input("Enter the number 1:"))
num2 = float(input("Enter the number 2:"))
Average = (num1 + num2)/(2)
print("The average of two numbers is :", Average)
"""

"""

Age = int(input("Enter your age :"))

if (Age<=18) :
    print("Not Eligible for voting")
else :
    print("Eligible for voting")
"""
"""
num1 = int(input("Enter the number 1:"))
if (num1%2==0) :
    print("Even")
else :
    print("Odd")
"""
"""
# Program to find the largest of three numbers
# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Checking the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Display the result
print("The largest number is:", largest)
"""