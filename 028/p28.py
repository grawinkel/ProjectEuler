#Project Euler Problem 28 solution in python

#http://projecteuler.net/index.php?section=problems&id=28

 # 73                      81
 #    43 44 45 46 47 48 49 50
 #    42 21 22 23 24 25 26
 #    41 20  7  8  9 10 27
 #    40 19  6  1  2 11 28 
 #    39 18  5  4  3 12 29
 #    38 17 16 15 14 13 30
 #    37 36 35 34 33 32 31
 # 65                      57
 # 
 # 
 # 3,5,7,9       2
 # 13,17,21,25   4
 # 31,37,43,49   6
 
sum=1
for x in xrange (3,1002,2):
    r=x**2
    for y in xrange (4):
        sum+=r
        r-= (x-1)
print sum
        
