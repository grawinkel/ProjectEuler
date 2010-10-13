#Project Euler Problem 19 solution in python

#http://projecteuler.net/index.php?section=problems&id=19




numdays={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,
}

d=1
numsundays = 0

for year in range (1900,2001):
    
    for month in range (1,13):
        days = numdays[month]
        
        #A leap year occurs on any year evenly divisible by 4, 
        #but not on a century unless it is divisible by 400.
        if month == 2:
            if year % 400 == 0:
                days +=1
            elif year % 4 == 0 and not year % 100 == 0:
                days +=1
            
        d+=days
        print year, month,days,d
        if year > 1900 and d % 7 == 0:
            numsundays +=1
        
print numsundays