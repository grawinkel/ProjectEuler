# # Project Euler Problem 23
# """
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
# """

maxx=28123
abundantNumbers=[]


def getFactorSum(n):
    fsum=0
    for i in range(1,(n/2)+1):
        if n % i == 0:
            # print n,i
            fsum+=i
    return fsum
    

#create a list of all abundant numbers up to maxx
for i in range (1,maxx+1):
    fsum = getFactorSum(i)
    print i, fsum
    if i < fsum:
        abundantNumbers.append(i)

# print abundantNumbers
# print len(abundantNumbers)

#now create a set of all numbers that might fall in to the category "cannot be written as the sum of two abundant numbers"
allNumbers=set()
for i in range(1,maxx+1):
    allNumbers.add(i)
    
#check all combinations of two abundant numbers and remove them from the set of all numbers
for n in abundantNumbers:
    print n
    for m in abundantNumbers:
        allNumbers.discard(n+m)

#allNumbers now contains only those numbers, that cannot be written as the sum of two abundant numbers.
print len(allNumbers)
print allNumbers
result = 0
for x in allNumbers:
    result +=x
#bazinga!
print "Result:" + str(result)