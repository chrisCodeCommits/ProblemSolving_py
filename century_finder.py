'''
iven a year, return the century it is in. The first century spans 
from the year 1 up to and including the year 100, the second  
from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer year

A positive integer, designating the year.

Guaranteed constraints:
1 ≤ year ≤ 2005.

[output] integer

The number of the century the year is in.

[Python3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name

'''

# My algorithms to solove this problem

def centuryFromYear(year):
    data = str(year)
    formula_oneA = int(data[:2])+1
    formula_oneB = int(data[:2])

    formula_twoA = int(data[0])+1
    formula_twoB = int(data[0])
    
    

    if len(data) == 4 and data[2:] != '00':
        return formula_oneA
    elif len(data) == 4 and data[2:] == '00':
        return formula_oneB

    elif len(data) == 3 and data[1:] != '00':
        return formula_twoA
    elif len(data) == 3 and data[1:] == '00':
        return formula_twoB

    elif len(data) <= 2:
        return 1
    
