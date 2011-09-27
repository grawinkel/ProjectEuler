# Project Euler Problem 31
"""
Quick and dirty brute forcing
"""

coins = [1,2,5,10,20,50,100,200]

max_value=200

count=0

def coinv(val,c):
    global count
    
    for x in coins:
        if x >= c:
            if x + val < max_value:
                coinv ( x+val,x)
            elif x + val == max_value:
                count+=1
                print count
                break
            else:
                break        
coinv(0,1)