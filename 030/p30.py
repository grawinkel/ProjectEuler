# Project Euler Problem 30
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 64 + 34 + 44
8208 = 8^4 + 24 + 04 + 84
9474 = 9^4 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""

result = 0
    
cache=dict()
for x in range (0,10):
    cache[str(x)]=x**5
    
print cache    
    
for x in xrange (3,10000000):
    s=str(x)
    sum=0
    for y in s:
        sum +=  cache[y]
    if x == sum:
        print x
        result +=x
        
print "result: %d" % (result)