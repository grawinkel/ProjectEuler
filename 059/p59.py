'''
Created on 20.04.2011

http://projecteuler.net/index.php?section=problems&id=59

@author: meatz
'''

if __name__ == '__main__':
    
    cipher = open("cipher1.txt",'r')
    ct = cipher.read().split(',')
    
    validCnt = 0
    for x in xrange (ord('a'),ord('z')+1):
        for y in xrange (ord('a'),ord('z')+1):
            for z in xrange (ord('a'),ord('z')+1):
                
                sum=0
                s=0
                msg=""
                key=[x,y,z]
                isOK = True
                for p in range(0,len(ct)):
                    val = int (ct[p]) ^ key[s%3]
                    if val >= 32 and val <= 122:
                        msg = msg + chr(val)
                        s = s + 1
                        sum = sum + val
                    else:
                        isOK = False
                        break
                if isOK:
                    print sum, chr(x),chr(y),chr(z),msg
                    validCnt = validCnt +1
    print "#valid messages: %d" % (validCnt)