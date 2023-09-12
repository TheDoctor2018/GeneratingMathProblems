"""
Summary: Create a program that will generate 2 or more unique number values with a range of (1-1000) that when added, 
subtracted, multiplied, or divided will not result in the following list of values bad_values= [420,34,69,666]

Developer:  Carlos Vasquez

Phase 1: Create a program that will generate 2 numbers between 1 and 1000 that when added will not result in any of the bad values.
Phase 1 Start/Completion Date:                      ex.9/4/2023


"""

#Library imports
import random

#Values
x = random.randrange(1,1000)
y = random.randrange(1,1000)

#Extra scope added: 
"""_summary_
    All values generated should be unique from each other x and y cannot be the same.
"""
def value_checks(a,b):
    
    if( a == b | b == a):
        a = random.randrange(1,1000)
        b = random.randrange(1,1000)
        return print("a is " + a + ", b " + b + ".")
    


#print values generated
print( x,": ", y)


