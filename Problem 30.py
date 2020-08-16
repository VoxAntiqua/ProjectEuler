# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 09:27:20 2019

@author: Andrew's Laptop
"""

#Euler Project problem 30

def IsSumofPowers(n):
    if n < 2: 
        return False
    nstr = str(n)
    nlst = []
    for dig in nstr:
        nlst.append(int(dig))
    print(nlst)
    
    sumofpowers = 0
    for dig in nlst:
        sumofpowers += dig**5
        
    if n == sumofpowers:
        return True
    else:
        return False

sumpowerslist = []    
for n in range(64, 355000):
    if IsSumofPowers(n):
        sumpowerslist.append(n)
        
print(sum(sumpowerslist))

