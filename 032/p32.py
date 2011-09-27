#!/usr/bin/env python
# encoding: utf-8
"""
p32.py
Created by Matthias Grawinkel on 2011-09-21.
"""
# Project Euler Problem 41
import itertools

def tuple2int(t):
    s=""
    for x in t:
        s+=str(x)
    return int(s)

def check(t):
    global cnt,results
    cnt+=1
    if cnt % 10000 == 0:
        print cnt
    tupleLength=len(t)
    for multiplicand in range(1,tupleLength-1):
        for multiplier in range(1,tupleLength-1):
            for product in range(1,tupleLength-1):
                if multiplicand + multiplier + product == tupleLength:
                    m=tuple2int(t[:multiplicand])
                    n=tuple2int(t[multiplicand:][:multiplier])
                    o=tuple2int(t[-product:])
                    # print t
                    # print multiplicand, multiplier, product
                    # print t[:multiplicand],t[multiplicand:][:multiplier], t[-product:]
                    # print "======"
                    if m * n == o:
                        print m,n,o
                        if not (n,m,o) in results:
                            results.add(o)


results=set()
cnt=0
perms = itertools.permutations(range(1, 10))
for j in perms:
    check(j)


result=0
print results
for rt in results:
    result+=rt
print result