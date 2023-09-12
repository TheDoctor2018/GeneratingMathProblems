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

#list of bad values
bad_values =[420,32,69,666]

#Extra scope added: 
"""_summary_
    All values generated should be unique from each other x and y cannot be the same.
"""
def value_checks(a,b):
    while( a == b):
        a = random.randrange(1,1000)
    return True

# checks if the result of adding both numbers will result in any of the bad values
def addtion_check(a,b):
    tem_result = a+b
    if (tem_result) in bad_values:
         a = a + 1
         #Temporary
         return True
    return True
             
        
#print values generated
def printValues(t):
    if t == True:
        print( "Math problem 1: " + str(x) +" + "+ str(y))


## Main program

if(value_checks(x,y)) == True:
    printValues(addtion_check(x,y))

