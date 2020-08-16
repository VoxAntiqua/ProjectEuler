# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:29:31 2019

@author: andre
"""

#Project Euler Problem 44

import numpy as np

def isPentagonal(n):
    """
    Checks if a number n is pentagonal
    """
    penTest = (np.sqrt(24*n+1)+1)/6
    return penTest == int(penTest)

result = 0
notFound = True
i = 1

while notFound:
    i += 1
    n = i*(3*i-1)/2
    
    for j in range(i-1,0,-1):
        m = j*(3*j-1)/2
        if isPentagonal(n+m) and isPentagonal(n-m):
            notFound = False
            result = n-m
            break
        
print(result)