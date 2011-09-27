# Project Euler Problem 40
"""
python fun ;-)

1) build sieve
2) until eleven are found, check all stripped versions of the prime...
"""

sieveSize=10000000

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

def isPrime(n):
    return n in ps
    
def isSpecial(n):
    #n is prime as it's stored in ps
    for i in range(1,len(str(n))):
        # print "i=%d" % (i)        
        if not isPrime(int(str(n)[i:])) or not isPrime(int(str(n)[:-i])):
            return False
    return True
    
pslist = primes(sieveSize)
ps= set()

for x in pslist:
    ps.add(x)
    
print "created sieve with size %d, start checking..." %(len(ps))

result = 0
cnt = 0
for x in pslist:
    if x > 7 and isSpecial(x):
        print x
        cnt +=1
        result+=x
        if cnt == 11:
            break
        
        
print "sieveSize: %d, cnt: %d, result: %d" %(sieveSize, cnt, result)