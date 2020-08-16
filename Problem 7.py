# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:40:55 2019

@author: Andrew's Laptop
"""

#Project Euler problem 7

import math

def nthprime(n):
    primes = [2,3]
    p = 5
    #Checks to see if p is a multiple of any primes less than its square root.
    #If not, adds to list of primes. Loops until nth prime is reached.
    while len(primes) < n:
        for f in primes:
            prime = True
            if f > math.sqrt(p):
                break
            elif p%f == 0:
                prime = False
                break
        if prime == True:
            primes.append(p)
        p += 2
    print(primes[n-1])