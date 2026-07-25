#loops are used to repeat instrections.
#while loop(iteration)
"""
count = 1
while count<=5 :
    print("hello")
    count+=1
"""
"""
i = 5  #iterator
while i >= 1:
    print(i)
    i -= 1
print("Loop ended")
  """
#break statement
"""
i = 1
while i <= 5:
    print(i)
    if(i==3):
        break
    i+=1

print("end of loop")
"""
#continue statement
"""
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1
    """
# loops are used for sequential traversal. For traversing list, string, tuples etc.
# for loop
#syntax-(for el in list:
#some work)
#for loop with else-
"""
for el in list :
some work
else:
work when loop ends
"""
#for loop
"""
num = [1,2,3,4,5]
for val in num:
    print(val)
"""
    #for loop in tuple
"""
tup = (1,2,3,4,5,6)
for num in tup:
    print(num)
""" 
#for loop with string
"""
str = "apnacollege"
for char in str :
    print(char)
else:
    print("end")


str = "apnacollege"
for char in str :
    if (char == 'o') :
        print("o found")
        break
    print(char)
else:
    print("end")
    """

#range()
#Range function returns a sequence of numbers , starting from 0
#by default,and increments by 1(by default),and stops before a specified number.

#range(start? , stop, step?)
"""
#method1
seq = range(5)
for i in seq:
    print(i)
    """
    #method2
"""
#type1
for i in range (10):#(range (stop))
        print(i)
        """
"""
#type2
for i in range (2,10):#(range (start,stop))
        print(i)
        """

#type3
"""
for i in range (2,10,2):
    print(i)
"""

#Pass statement
#Pass is a null statement that does nothing . It is used as a placeholder for future code.
#usually used in exceptions and try catch 
"""
for i in range(5):
    pass

print("work is processing")
"""
"""
total = 0
for i in range(1 ,366):
    total = total + i
print(total)
"""
