#A build-in data types that lets us create immutable sequence of values called as tuples
"""
tup = (2,4,3,2,7)
print(type(tup))
print(len(tup))

tup[0] = 3
print(tup[0])      #it will not change the value of index 0 because it is immutable
print(tup)

tup = (1) 
print(tup)
print(type(tup))
tup = ("hello")
print(tup)
print(type(tup))
tup = (2.6)
print(tup)
print(type(tup))

#tuple slicing
tup = (2,4,3,2,7)
print(tup[1:4])

#tuple function
#tup.index
tup = (2, 4, 2, 8)
print(tup.index(8))  #it will show the index of the element
#tup.count
print(tup.count(2))
"""