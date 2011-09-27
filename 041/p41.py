# Project Euler Problem 41
import itertools

def isPrime(n):
    '''check if integer n is a prime'''
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True
    
nums = []
for i in range(6, 9):
    numList = range(1, i + 1)
    perms = itertools.permutations(numList)
 # loop over all the permutations
    for j in perms:
        nums.append(j)
    
nums.sort(reverse=True)
for x in nums:
    num=""
    for k in x:
        num += str(k)
    if isPrime(int(num)):
        print num
        break
