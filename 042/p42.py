#!/usr/bin/env python
# encoding: utf-8
"""
p42.py
Created by Matthias Grawinkel on 2012-10-05.
"""

from sets import Set

result = 0
triangles = Set()

for x in xrange(0,10000):
    t = 0.5 * x * (x+1)
    print t
    triangles.add(int(t))


with open('words.txt') as f:
    content = f.readlines()[0].split(',')
    for word in content:
        word = word.replace('"','')

        ws = 0
        for x in xrange(0,len(word)):
            ws += (ord(word[x]) - 64)
        if ws in triangles:
            result += 1
print result

