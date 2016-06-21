# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

def biggest(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c
    
def smallest(a, b):
    if a < b:
        return a
    return b
    
def set_range(a,b,c):
    biggest_num = biggest(a, b, c)
    smallest_num = smallest(a, b)

    if biggest_num == a:
        smallest_num = smallest(b, c)
    if biggest_num == b:
        smallest_num = smallest(a, c)

    return biggest_num - smallest_num
