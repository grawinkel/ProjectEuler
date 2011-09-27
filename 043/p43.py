#!/usr/bin/env python
# encoding: utf-8
"""
p43.py
Created by Matthias Grawinkel on 2011-09-22.
"""

import itertools

def tuple2int(t):
    s=""
    for x in t:
        s+=str(x)
    return int(s)
    
def divisible(d1,d2,d3,divisor):
     return ((d1*100) + (d2 * 10) + d3) % divisor == 0
     
def check(d):
    if divisible (d[1],d[2],d[3],2) and divisible (d[2],d[3],d[4],3) and divisible (d[3],d[4],d[5],5) and divisible (d[4],d[5],d[6],7) and divisible (d[5],d[6],d[7],11) and divisible (d[6],d[7],d[8],13) and divisible (d[7],d[8],d[9],17):
        return True
    return False
                
result=0
perms = itertools.permutations(range(0, 10))
for j in perms:
    if check (j):
        result+=tuple2int(j)
print result