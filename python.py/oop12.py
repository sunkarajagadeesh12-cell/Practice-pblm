#to map with real world scenarios, we started using objects in code.
# This is called object oriented programming.

#class is a blueprint for creating objects.
#ex-mobile - to make a mobile we have to know about their features and we have to add the features
#therefore in class we have input the features
#creating class
"""
class Student:
    name = "Sai"
    #creating an object(instance)  #ex-mobile
s1 = Student() #see the tab spaces clearly
print(s1.name)
"""
"""
class Car: #class define
    colour = "Blue"
    brand = "Porche"
car1 = Car() #object
print(car1.colour)
print(car1.brand)
"""
"""
__init__ function 
Constructor:-
All classes have a function called __init__(),which is always executed when the object is being initiated.
#syntax
#creating class
class Student:
def  __init__(self,fullname):#def space__
self.name = fullname 
#creating object
s1 = Student("karan")
print(s1.name)
"""
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs
"""
class Student:
    def __init__(self): # automatically invoke or call
        print("My name is sai")
    
s1 = Student()#here () it will call to (self) automatically
"""
"""
class Student:
    def __init__(self,fullname):
        self.name=fullname
        print(" i am sai")

s1 = Student("Jaggu")
print(s1.name)
s2 = Student("suraj")
print(s2.name)
# The data stored inside the classor variables are called as attributes
"""
"""
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks = marks
        print("prossessing your marks")
"""
"""
s1 = Student("kiran",97)
print(s1.name,s1.marks)
s2 = Student("Sai",99)
print(s2.name,s2.marks)
"""
"""
class Student:#we have to use tab and the write the def code
    def  __init__(self):#def space__
        pass
    #parameterized constructors
    def __init__(self, name, marks):
        self.name=name  # it's a reference of object (self.)
        self.marks = marks
        print("prossessing your marks")
        """
#class & instance Attributes
# 1) class.Attr
# 2)obj.attr
# self.name , self.marks are different for different students so it is called as class & Instance attributes
"""
class Student:
    college_name = ("sri viswa")
    name = "anonymous" #class attr
    def __init__(self,name,marks):
        self.name=name #obj attr > class attr
        self.marks = marks
        print("prossessing your marks")

s1 = Student("kiran",97)
print(s1.name,s1.marks)
s2 = Student("Sai",99)
print(s2.name,s2.marks)
#if we access name then we will use s1.name etc
# print(s2.college_name)  #method1
print(Student.college_name)
"""
#class is a collection of attributes and methods
"""
class Student:#class
    def __init__(self,name,marks):#conatructor
        self.name=name
        self.marks = marks
        
    def welcome(self):#
        print("Welcome students", self.name)

    def get_marks(self):#methods
        return self.marks

s1 = Student("kiran",97)#object
s1.welcome()
print(s1.get_marks())
"""
# static method - methods that don't use the self parameter (work at class level)
# it uses in class level
"""
class Student:
    @staticmethod  #decorator
    def college():
        print("ABC College")
"""
#example
"""
class Student:
    def __init__(self): # automatically invoke or call
        print("My name is sai")
    @staticmethod# if it is not there it will throw error
    def hello():
        print("hello")

s1 = Student()
s1.hello()
"""
# Four pillers of oops
# 1)Abstraction , 2)Encapsulation , 3) inheritance ,4) Polymorphism 
# 1)Abstraction : Hiding the implementation details of a class and only showing the essential features to the user.
#ex-
"""
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True  #here it will ignore the unnessesary details
        self.acc = True
        print("car started..")


car1 = Car()
car1.start()

#Encapsulation-Wrapping data and function into a single unit (object).
"""
"""
class Solution() :
    college_name = "Sri Viswa"
    name = "anonymous"
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
        print("adding new student in Database...")

s1 = Solution("Sai",95) 
print(s1.name)
print(s1.marks)
s2 = Solution("surya",85) 
print(s2.name)
print(s2.marks)
"""
"""
class Solution():
    def __init__(self,name,phy,eng,math):
        self.name = name 
        self.marks1 = phy 
        self.marks2 = eng 
        self.marks3 = math
    def welcome(self):
        print("welcome student:",self.name)
    def mark(self):
        print("your marks in phy,eng,math are:",self.marks1,self.marks2,self.marks3)
    def average(self):
        Average = (self.marks1+self.marks2+self.marks3)/3
        print("The average of the student is :",Average)

s1 = Solution("Sai",99,98,97)
s1.welcome()
s1.mark()
s1.average()
s2 = Solution("prakhar",87,86,85)
s2.welcome()
s2.mark()
s2.average()
s3 = Solution("Surya",77,76,75)
s3.welcome()
s3.mark()
s3.average()
#we can change the value of name directly 
"""

"""
#account balance 
class Solution():
    def __init__(self,balance,accountno):
        self.bal = balance
        self.acc = accountno
    def debit(self,amount):
        self.deb -= amount
        p
      """   
""" 
class Solution(object):
    def __init__(self, num1, num2):
       return num1+num2           # check once
s1 = Solution()
""" 
""" 
class Solution(object):
    def convertTemperature(self, celsius):
        self.celsius = celsius
        Fahrenheit = celsius * 1.80 + 32.00
        Kelvin = celsius + 273.15
        return [Kelvin,Fahrenheit]

s1=Solution()
val = float(input("celsius="))
result=(s1.convertTemperature(val))
print(result)
""" 
