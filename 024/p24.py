# Problem 24

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import itertools

c = itertools.permutations("0123456789")
cnt=0
for x in c:
    cnt += 1
    if cnt==1000000:
        print x
        break