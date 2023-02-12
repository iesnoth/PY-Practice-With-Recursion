# Python function called mult_list() to multiply all the numbers in a list.
import math

def mult_list(*nums):
    result = math.prod(nums)
    return result

print(mult_list(1,2,7,3))
