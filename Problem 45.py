# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:04:54 2019

@author: andre
"""

#Project Euler Problem 45

import numpy as np

def triangle(n):
    return n*(n+1)/2
    
def isPentagonal(n):
    """
    Checks if a number n is pentagonal
    """
    penTest = (np.sqrt(24*n+1)+1)/6
    return penTest == int(penTest)

def isHexagonal(n):
    hexTest = (np.sqrt(8*n+1)+1)/4
    return hexTest == int(hexTest)

i = 285
notFound = True

while notFound:
    i += 1
    if isPentagonal(triangle(i)) and isHexagonal(triangle(i)):
        notFound = False
        print(triangle(i))
    