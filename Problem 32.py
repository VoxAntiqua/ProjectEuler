# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:09:50 2019

@author: Andrew's Laptop
"""

#Project Euler problem 32

def IsPandigital(a,b,c):
    strabc = str(a)+str(b)+str(c)
    if len(strabc) == 9:
        ispan = True
        for i in range(1,10):
            if str(i) not in strabc:
                ispan = False
    else:
        ispan = False
    return ispan

pandigitals = []

for n in range(1000,10000):
    for m in range(1,1000):
        if n%m == 0:
            if IsPandigital(n,m,int(n/m)):
                if n not in pandigitals:
                    pandigitals.append(n)
                    
print(pandigitals)
print(sum(pandigitals))
                