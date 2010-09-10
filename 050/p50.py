# Project Euler Problem 50
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
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



#generate the list of primes
for p in eras(1000000):
    primes.add(p)


pa=[]
maxsum=0
maxnum=0

limit=1000000
for x in sorted(primes):
    pa.append(x)
    
l = len(pa)

for i in range (0, l):
    if i % 1000 == 0:
        print "iteration %d/%d" % (i,len(pa))

    lsum=0
    lnum=0
    for j in range (i,l):
        lsum+=pa[j]
        lnum+=1
       
        if lsum > limit:
            break
        if lsum >= maxsum:
            if lnum >= maxnum and lsum in primes:
                maxnum = lnum
                maxsum=lsum
                print "maxnum %d, maxsum %d, iteration %d" % (maxnum, maxsum, i)

print maxnum, maxsum
# 997651