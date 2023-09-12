"""
Summary: Create a program that will generate 2 or more unique number values with a range of (1-1000) that when added, 
subtracted, multiplied, or divided will not result in the following list of values bad_values= [420,34,69,666]

Developer:  Carlos Vasquez

Phase 1: Create a program that will generate 2 numbers between 1 and 1000 that when added will not result in any of the bad values.
Phase 1 Start/Completion Date:9/4/2023-9/12/2023                      ex.9/4/2023

Phase 2: Extend functionality by create a class to deal with multiplication, subtraction, and division. 
Create main function and call it using funtion in mathgen file/class.
Phase 1 Start/Completion
"""

## Class File: MathGen

#import MathGen funtions
import MathGen
import random


# generate values
x = random.randrange(1,1000)
y = random.randrange(1,1000) 


# print values
print( x, y)
print("Workspace working?")

