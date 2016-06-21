# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# use as few total stamps as possible by first use as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.


def stamps(num):
    p5 = 0
    p2 = 0
    p1 = 0
    while num >= 5:
        p5 += 1
        num -= 5
    while num >= 2:
        p2 += 1
        num -= 2
    while num >= 1:
        p1 += 1
        num -= 1
    return p5, p2, p1 
    


print stamps(18)