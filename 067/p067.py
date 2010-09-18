#Problem 67

#dynamic programming

#read in the triangle and populate the array
def getTriangle():
    values=[]
    t=open('triangle.txt','r')
    d=0
    for line in t.readlines():
        d+=1
        for n in line.split():
            values.append(int(n))
    return values,d

def getmax(d):
    global values
    p = len(values)-1
    for l in xrange(d-1,-1,-1):
        # print "================="
        for x in xrange (l,-1,-1):
            # print "p:%d, x:%d, value:%d" % (p, x, values[p])
            if x>0:
                # print "will check %d and %d with %d"% (values[p], values[p-1], values[p-l-1])
                values[p-l-1]= max( (values[p-l-1]+values[p]), (values[p-l-1]+values[p-1]))
            p -=1
        
    
values,d = getTriangle()
getmax(d)
print values[0]