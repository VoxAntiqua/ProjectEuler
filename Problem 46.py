# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:07:20 2019

@author: andre
"""

#Project Euler Problem 46

import numpy as np

PRIME_DICTIONARY = {1:False,2:True,3:True,4:False}

def isPrime(n,primeDictionary):
    if n not in primeDictionary:
        if n%2 == 0:
            primeDictionary[n] = False
        else:
            for j in range(2,int(np.sqrt(n))+1):
                if n%j == 0:
                    primeDictionary[n] = False
                    break
                elif n%j != 0:
                    primeDictionary[n] = True
        if primeDictionary[n] == True:
            for k in range(1,100):
                primeDictionary[n+k*n] = False
    return primeDictionary[n]

def doubleSquare(n):
    return 2*n**2

oddComposite = 33
satisfiesGoldbach = True

while satisfiesGoldbach:
    if isPrime(oddComposite,PRIME_DICTIONARY):
        oddComposite += 2
    n = 1
    while doubleSquare(n) < oddComposite:
        primeFound = False
        if isPrime(oddComposite - doubleSquare(n),PRIME_DICTIONARY):
            oddComposite += 2
            primeFound = True
            break
        n += 1
    if not primeFound:
        satisfiesGoldbach = False
        
print(oddComposite)