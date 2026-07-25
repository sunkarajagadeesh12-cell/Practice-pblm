# del keyword -
# sed to delete object properties or object itself.
"""
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Sai")
print(s1.name)
del s1.name
print(s1.name)
"""
#private (like)  attributes & methods
"""
Conceptual implementations in Python
private attributes & methods are meant to be used only within the class and are not accessible from outside the class.
"""
"""
class Account:
    def __init__(self,acc_no , acc_pass):
        self.acc_no = acc_no 
        self.__acc_pass = acc_pass  # private = __acc_pass
    def reset_pass(self):  # Because it is defined in the class so it will be printed without error
        print(self.__acc_pass)

acc1 = Account("112443","abcd")
print(acc1.acc_no)
print(acc1.reset_pass())
"""
"""
class Person:
    __name = "Sai"
    def __hello(self,name):
        print("hi user")

    def welcome(self):
        self.__hello(self.__name)

p1 = Person()
print(p1.welcome())   # it will show error
"""

# Inheritance
# Single inheritance
"""
 When one class (child/derived) derives the properties & methods of another class (parent/base).

class Car:
#start()
#stop()
#colour()
class ToyotaCar(Car):   #here we can delivers the functions of car in the function toyotacar
____________
"""
"""
class Car:
    colour = "Black"
    @staticmethod
    def start():
        print("Car starded..")

    @staticmethod
    def stop ():
        print("car stopped.")

class ToyotaCar(Car):  
     def __init__(self,name):
         self.name = name


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.colour)   # because we use inheritance(Car) it will run without error
print(car1.stop())   # because we use inheritance(Car) it will run without error
"""

# Multi level class Car:
"""
class Car():
    colour = "Black"
    @staticmethod
    def start():
        print("Car starded..")

    @staticmethod
    def stop ():
        print("car stopped.")

class ToyotaCar(Car):  
     def __init__(self,brand):
         self.brand = brand  #inheritance


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
print(car1.type)   #don't write like car1.type() or car1Fortuner() because it string obj is not callable
car1.start()  # we can call due to multi-level inheritance
"""
"""
# Multiple Inheritance
# all multiple parent classes can be stored in single derived class
"""
"""
class A:
    varA  = "Welcome to class A"
class B:
    varB = "Welcome to class B"
class C(A,B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)
"""

# Super method
#  Super () method is used to access methods of the parent class .

class Car:
    def __init__(self, car_type):
        self.type = car_type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped.")


class ToyotaCar(Car):
    def __init__(self, name, car_type):
        super().__init__(car_type)
        self.name = name
        super().start()


car1 = ToyotaCar("prius", "electric")
print(car1.type)
