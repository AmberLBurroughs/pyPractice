# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    big = biggest(a,b,c)
    if a == big:
        return bigger(b,c)
    if b == big:
        return bigger(a,c)
    else: 
        return bigger(a,b)












