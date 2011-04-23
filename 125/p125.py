'''
Created on 23.04.2011

@author: meatz
'''

def isPalindrome(x):
    s = str(x)
    le=len(s)-1
    for i in range((le/2)+1):
#        print s[i],s[le-i]
        if s[i] != s[le-i]:
            return False
    return True


def doit(upperbound):
    lp = 0
    ops=0
    palims= set()
    while True:
        lp+=1
        print "lp=%d" %(lp)
        ops+=1
        if ( (lp ** 2)+((lp+1) ** 2) > upperbound ):
            break;
        
        cnt = 0
        testPalim = lp ** 2
        rp=lp
        while True:
            rp+=1
            testPalim += rp ** 2
            
            ops+=1    
            if testPalim > upperbound:
                print "break at lp=%d,rp=%d, #isPalindrom tests:%d, #ops: %d" %(lp, rp,cnt,ops)
                break
            else:
                cnt+=1
                if isPalindrome(testPalim):
                    print testPalim, lp,rp
                    palims.add(testPalim)                    
    
    result = 0
    for palim in palims:
        result +=palim
        
    print result, len(palims)
    
    

if __name__ == '__main__':
    doit(10**8)
#    doit(1000)
    
    