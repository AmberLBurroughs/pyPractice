# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.
def factorial(n):
    ttl = 1
    while n >1:
        ttl = n * ttl
        n = n - 1
    return ttl
  
