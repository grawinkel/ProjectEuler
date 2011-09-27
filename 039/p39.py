# Project Euler Problem 39
"""
python fun ;-)

Brute force ftw... runtime could be heavily optimized...
"""
import math


def getVariations(d):
    variations=0
     
    for a in range (1,d):
        for b in range (1,d):
            c = math.sqrt ((a**2) + (b**2))
            if a+b+c == d:
                variations+=1
    return variations
    

maxvars=0
maxd=0    
for d in range (3,1001):
    variations = getVariations(d)
    print d, variations
    if variations > maxvars:
        maxd = d
        maxvars = variations

print d,maxvars
    
