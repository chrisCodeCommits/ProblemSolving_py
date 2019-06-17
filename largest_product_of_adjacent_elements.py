'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The largest product of adjacent elements.

[Python3] Syntax Tips

Prints help message to the console

'''

# My algorithms to solve this problem

 def adjacentElementsProduct(array):
        operation = (array[n] * array[n + 1] for n in range(len(array)-1))
    return max(operation)
   
   
   
   ###### Alternative ####################################
   
   def adjacentElementsProduct(inputArray):
    
    operation = (
     inputArray[n] * inputArray[n + 1] for n in range(len(inputArray)-1)
    )
    
    return max(operation)
