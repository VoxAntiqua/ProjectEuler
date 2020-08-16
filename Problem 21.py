# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:26:11 2019

@author: Andrew's Laptop
"""

#Euler Project problem 21

facdic = {}
sumdic = {}
amicables = []


def ProperDivisors(n):
    factors = []
    for f in range(int(n/2),0,-1):
        if f not in factors:
            if n%f == 0:
                factors.append(f)
                if f in facdic:
                    for x in facdic[f]:
                        if x not in factors:
                            factors.append(x)
                
    facdic[n] = factors
    return factors
        
def SumDivisors():
    for key in facdic:
        if key not in sumdic:
            sumdic[key] = sum(facdic[key])
        
for n in range(2,10001):
    ProperDivisors(n)

SumDivisors()

for n in range(2,10001):
    if n not in amicables:
        for m in range(n+1,10001):
            if sumdic[n] == m and sumdic[m] == n:
                if n not in amicables:
                    amicables.append(n)
                if m not in amicables:
                    amicables.append(m)
            
print(sum(amicables))

