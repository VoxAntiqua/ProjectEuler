# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:28:23 2019

@author: Andrew's Laptop
"""

#Project Euler problem 31

denoms = [1,2,5,10,20,50,100,200]

coincombs = []
target = 200
#Let n represent the number of denominations available to sum up.
#Ex. n=0 means only 1p coins are available, n=3 means 1, 2, 5, and 10p coins
#are available.

coindic = {}
def FindDenoms(n,target):
    if n == 0:
        coindic[denoms[n]] = target
        copydic = coindic.copy()
        coincombs.append(copydic)
    else:
        maxnum = int(target/denoms[n])
        for i in range(0,maxnum+1):
            coindic[denoms[n]] = i
            remainder = target - i*denoms[n]
            FindDenoms(n-1,remainder)
        
    
    return coincombs
    

print(len((FindDenoms(7,200))))