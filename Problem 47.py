# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:51:13 2019

@author: andre
"""

#Project Euler Problem 47

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

def findDistinctPrimeFactors(n):
    factors = []
    for i in range(2, int(n/2) + 1):
        if n%i == 0 and isPrime(i,PRIME_DICTIONARY) and i not in factors:
            factors.append(i)
    return factors

targetNumber = 646


while True:
    if len(findDistinctPrimeFactors(targetNumber)) == 4: 
        if len(findDistinctPrimeFactors(targetNumber + 1)) == 4:
            if len(findDistinctPrimeFactors(targetNumber + 2)) == 4:
                if len(findDistinctPrimeFactors(targetNumber + 3)) == 4:
                    print(targetNumber)
                    break
    targetNumber += 1