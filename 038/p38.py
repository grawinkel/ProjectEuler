# Project Euler Problem 38
"""
python fun ;-)
"""


digits=["1","2","3","4","5","6","7","8","9"]

maxv = 0

def getN(c,n):
    s=""
    for x in range(1,n+1):
        s += str(x*c)
    # print c,n,s
    return s
    
def isPandigital(s):
    if len (s) != 9:
        return False
    for d in digits:
        if d not in s:
            return False
    return True
    

for a in range (1,500000):
    for b in range (1,10):
        x = getN(a,b)
        if isPandigital(x):
            if int(x) > maxv:
                maxv = int(x)
                print x
        else:
            if len (x) > 9:
                break
                
print "result:" + str(maxv)


#print getN(192,3) 
# print getN(9,5)
