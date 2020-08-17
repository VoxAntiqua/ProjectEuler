# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:28:12 2019

@author: andre
"""

#Project Euler Problem 49

import numpy as np

# Initialize prime dictionary
PRIME_DICTIONARY = {1:False,2:True,3:True,4:False}

# Given prime dictionary, check if n is prime
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
    

# Checks if two integers are digital permutations of one another
def isPermutation(x,y):
    return sorted(str(x)) == sorted(str(y))

# Iterate through all 4-digit integers. When a prime k is found, check
# k+3330 and k+6660 to see if they are primes as well as permutations of k.
# k=1487 is a known solution, so skip that one.
def findPrimeTriples(primeDictionary):
    for n in range(1000,10000):
        if isPrime(n,primeDictionary):
            if isPrime(n+3330,primeDictionary):
                if isPrime(n+6660,primeDictionary):
                    if isPermutation(n, n+3330) and isPermutation(n, n+6660):
                        if n != 1487:
                            return n
                            stop
                        
if __name__ == "__main__":
    n = findPrimeTriples(PRIME_DICTIONARY)
    print(str(n)+str(n+3330)+str(n+6660))