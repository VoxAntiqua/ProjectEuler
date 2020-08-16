# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:47:25 2019

@author: Andrew's Laptop
"""

import math

def PrimeGen(n):
    primedic = {1:False, 2:True}
    primes = [2]
    for evens in range(4,n+1,2):
        primedic[evens] = False
    for i in range(3,n+1,2):
        if i not in primedic:
            for j in range(2,int(math.sqrt(i))+1):
                if i%j == 0:
                    primedic[i] = False
                    break
        if i not in primedic:
            primedic[i] = True
            primes.append(i)
            for k in range(3*i, n+1, 2*i):
                primedic[k] = False
    return primes


def Rotation(n):
    digits = list(str(n))
    rotations = [n]
    while True:
        firstdigit = digits.pop(0)
        newdigits = digits + [firstdigit]
        if newdigits == list(str(n)):
            break
        rotations.append(int("".join(newdigits)))
        digits = newdigits
    return rotations
    
primelist = PrimeGen(1000000)

circulars = []
for n in primelist:
    print(n)
    if n not in circulars:
        rots = Rotation(n)
        rotsinlist = True
        for rot in rots:
            if rot not in primelist:
                rotsinlist = False
                break
        if rotsinlist:
            for rot in rots:
                circulars.append(rot)
                
print(circulars)
print(len(circulars))