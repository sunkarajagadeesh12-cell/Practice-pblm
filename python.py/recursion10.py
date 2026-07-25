#when a function calls itself repeatedly.
#recursive function
"""
def show(n):
    if(n==0) : #(base case (n==0))
        return
    print(n)
    show(n-1)
#function call
show(5)

# return n!
"""
"""
def fact(n):
if(n == 0 or n == 1):
return 1
else:
return n* fact(n-1)
"""