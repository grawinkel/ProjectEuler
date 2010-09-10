# Project Euler Problem 21
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

primes = set()

#generate primes by sieving
def eras(n):
  siv=range(n+1)
  siv[1]=0
  sqn=int(round(n**0.5))
  for i in range(2,sqn+1):
    if siv[i]!=0:
        siv[2*i:n/i*i+1:i]=[0]*(n/i-1)
  return filter(None,siv)

#check if all rotations of the number are in the set of primes
#returns False if any rotation does not match  
def rotationsArePrimes(number):
    s=str(number)
    p = s
    for x in range(len(s)):
        p = p[1:] + p[:1]
        if int(p) not in primes:
            return False
    return True

#generate the list of primes
for p in eras(1000000):
    primes.add(p)

result = 0
for number in primes:
    if rotationsArePrimes(number):
        print number
        result+=1

print "result: %d"% (result)