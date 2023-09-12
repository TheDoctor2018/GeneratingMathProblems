"""_summary_
Functions that deal with verifying numbers and print out math problems.
"""

#Library imports
import random

#list of bad values
bad_values =[420,32,69,666]



## value check funtions
def value_checks2(a,b):
    """_summary_
    Returns true that the values generated are unique,
    if they arent then they are regenerated.

    Args:
        a (int): generated number from 1-1000
        b (int): generate number form 1-1000

    Returns:
        bool: true if unique 
    """
    while( a == b):
        a = random.randrange(1,1000)
    return True



"---!Phase 2 focus, add check for multi, sub, and division!---"

## addtion, subtraction, multiplication, and division checks
def addtion_check(a,b):
    """_summary_
    Checks if the values when added will not return any of the bad values.
    If it does it will change up the values

    Args:
        a (int): generated number from 1-1000
        b (int): generate number form 1-1000

    Returns:
        bool: true if added numbers are not in the bad values list
    """
    tem_result = a+b
    if (tem_result) in bad_values:
         a = a + 1
         #Temporary
         return True
    return True
             
def subtraction_check(a,b):
    """_summary_ WIP
    Checks if the values when added will not return any of the bad values.
    If it does it will change up the values

    Args:
        a (int): generated number from 1-1000
        b (int): generate number form 1-1000

    Returns:
        bool: true if added numbers are not in the bad values list
    """
    tem_result = a+b
    if (tem_result) in bad_values:
         a = a + 1
         #Temporary
         return True
    return True
"--------------------------------------------------------------------------------------"


def printValues(t, x, y):
    """_summary_
    Prints out the math problems if only it has been checked 

    Args:
        t (bool): generated true value from the + */ - funtions.
    """
    if t == True:
        print( "Math problem 1: " + str(x) +" + "+ str(y))


## Main funtion
def genMathProblems(x,y,a):
    """_summary_
    calls the funtion to check if numbers generated are unique.
    calls the funttion to check if numbers when added will not 

    Args:
        x (int): generated number
        y (int): generated number
        a (int): used in switch statement, 0-3 values 0-addition, 1-multiplication, 2-subtraction, 3-division
    """
    ## switch statement would be better but issues
    if a == 0:
        if(value_checks2(x,y)) == True:
                printValues(addtion_check(x,y))
    if a == 1: #WIP
        if(value_checks2(x,y)) == True:
                printValues()
    if a == 2: #WIP
        if(value_checks2(x,y)) == True:
                printValues()
    if a == 3: #WIP
        if(value_checks2(x,y)) == True:
                printValues()

            
        


