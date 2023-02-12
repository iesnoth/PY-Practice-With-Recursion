# Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.

def num_within(num,range_start,range_end):
    if num > range_start and num <= range_end:
        return True
    else: return False

print(num_within(1,4,6)) #returns false
print(num_within(6,4,6)) #resturns true
