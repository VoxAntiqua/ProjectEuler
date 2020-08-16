# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:28:12 2019

@author: andre
"""

#Project Euler Problem 49

import numpy as np
from itertools import permutations

def generatePermutations(n):
    return [int(''.join(p)) for p in permutations(str(n))]

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

candidate = 1001
primeTriples = []

while candidate < 10000:
    if isPrime(candidate, PRIME_DICTIONARY):
        candidatePermutations = generatePermutations(candidate)
        primePerms = [candidate]
        for perm in candidatePermutations:
            if isPrime(perm, PRIME_DICTIONARY) and perm > 1000:
                primePerms.append(perm)
        if len(primePerms) >= 3:
            primePerms.sort()
            if primePerms not in primeTriples:
                primeTriples.append(primePerms)
                
    candidate += 2

sequences = []
for triple in primeTriples:
    if triple[2] - triple[1] == triple[1] - triple[0]:
        sequences.append(triple)
        
print(sequences)