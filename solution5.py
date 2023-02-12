# function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print

# this solution is based on using the powers of 11 to build the triangle
#doesn't do all the fancy math, but it is a lot easier for me to understand
def pascal(n):
    for i in range(n):
        print(' '.join(map(str, str(11**i))))
        # 11**i multiplies 11 to the power of the number(i)
        # that number is then turned into a string by str
        # that string is then mapped. The map() receives two arguments:
            # the function to which the iterable object is passed
            # the iterable variable.
        #In this instance, the integer had to become a string first, because it wasn't iterable. The map then returns an object.
        #.join combines all the object items into a string. In this instance, it's using the ' ' as a separator, but anything could be there.
            #.join /has/ to have a separator

pascal(5)
