# Project Euler Problem 40
"""
python fun ;-)
"""

f="."
c=0

while len(f) < 1000005:
    c +=1
    f += str(c)

print int(f[1]) * int(f[10]) * int(f[100]) * int(f[1000]) * int(f[10000]) * int(f[100000]) *int(f[1000000])