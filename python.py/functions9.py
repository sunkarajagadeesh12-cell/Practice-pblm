#block of statement that performs a specific task.(repeat,redundant)
#  function defination-def
#due to functions redundancy decreases and reusability increases.
"""
def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum
"""
"""
#syntax of function
def func_name(param1,param2) :
return val
#function defination

#function call
func_name(arg1,arg2...)
"""
"""#in this programer redundency decreases
#method1
def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum

calc_sum(5,10)
calc_sum(2,10)
calc_sum(12,17)
"""
#method2
"""
def calc_sum(a,b): #( a,b are parameters)
    return a+b

sum = calc_sum(1,3) #(1,3 are arguments)
print(sum)
"""
"""
def print_hello():  #there is no return value and parameters in this function and it is possible to create these type of function
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()
"""
"""
def print_hello():#it will return no value because it does not has nay return value
    print("hello")
output = print_hello()
print(output)
"""
"""
function in python(types of python)
there are two types of python
1)built-in functions   2) User defined functions
1)built-in function:
print(),len(),type(),range()

1st case:
print("apnacollege","shradhakhapra")  #sep = " "
2nd case:
print("apnacollege")
print("sai") #end = "\n"
"""
#3rd case:
"""
print("apnacollege" , end = " ")
print("sai")


def cal_prod(a,b):
    print(a*b)
    return a*b

cal_prod()  #it will show me an error of missing twoo arguments
"""
#then we will give the default values or default parameters
#assigninng a default value to parameter, which is used when no argument is passed.
"""
def cal_prod(a=1,b=1):
    print(a*b)
    return a*b #by default values

cal_prod()
"""
"""
def cal_prod(a,b=1):
    print(a*b)  
    return a*b #by single default values it does not show error

cal_prod(4)
#if the default parameter is comes first and second is empty the it will raise error
"""
