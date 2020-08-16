# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:28:42 2019

@author: Andrew's Laptop
"""

#Project Euler problem 37

import math
primedicvar = {1:False, 2:True, 3:True}

def IsPrime(n,primedic):
    if n not in primedic:
        if n%2 == 0:
            primedic[n] = False
        else:
            for j in range(2,int(math.sqrt(n))+1):
                if n%j == 0:
                    primedic[n] = False
                    break
                elif n%j != 0:
                    primedic[n] = True
        if primedic[n] == True:
            for k in range(1,100):
                primedic[n+k*n] = False
    return primedic[n]

def Truncate(x):
    numlist = []
    xstr = str(x)
    for i in range(1,len(xstr)):
        numlist.append(int(xstr[i:]))
    for j in range(0,len(xstr)):
        numlist.append(int(xstr[0:(len(xstr)-j)]))
        
    return numlist


n = 11
results = []

while len(results) != 11:
    if IsPrime(n, primedicvar):
        print(n)
        truncs = Truncate(n)
        truncsprime = True
        for ele in truncs:
            if IsPrime(ele, primedicvar) == False:
                truncsprime = False
                break
        if truncsprime:
            results.append(n)
    n += 2
            
print(results)
print(sum(results))