# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:20:14 2019

@author: Andrew's Laptop
"""

#Project Euler problem 10
import math

def primeslessthann(n):
    primes = [2,3]
    p = 5
    #Checks to see if p is a multiple of any primes less than its square root.
    #If not, adds to list of primes. Loops until prime exceeds n.
    while p < n:
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
    return primes

print(sum(primeslessthann(2000000)))
