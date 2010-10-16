# Problem 36
#http://projecteuler.net/index.php?section=problems&id=36

def isPalindrome(s):
    l=len(s)
    for x in xrange (l):
        if s[x] != s[l-x-1]:
            return False
    return True
    
def bin(x):
    sign = '-' if x < 0 else ''
    x = abs(x)
    bits = []
    while x:
            x, rmost = divmod(x, 2)
            bits.append(rmost)
    return sign + ''.join(str(b) for b in reversed(bits or [0]))
    
s=0
for x in xrange (1,1000001):
    if isPalindrome(str(x)) and isPalindrome(str(bin(x))):
        s+=x
        print x,bin(x)
print s