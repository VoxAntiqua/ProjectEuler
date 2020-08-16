# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:29:12 2019

@author: andre
"""

#Project Euler Problem 43

import numpy as np
from itertools import permutations

def generatePandigitals():
    """
    Generates all 10-digit pandigitals
    """
    return [int(''.join(p)) for p in permutations("1234567890")]

pandigitals = generatePandigitals()
substringPandigitalSum = 0

for pandigital in pandigitals:
    pandigitalString = str(pandigital)
    if len(pandigitalString) == 9:
        continue
    if int(pandigitalString[1]+pandigitalString[2]+pandigitalString[3])%2 != 0:
        continue
    if int(pandigitalString[2]+pandigitalString[3]+pandigitalString[4])%3 != 0:
        continue
    if int(pandigitalString[3]+pandigitalString[4]+pandigitalString[5])%5 != 0:
        continue
    if int(pandigitalString[4]+pandigitalString[5]+pandigitalString[6])%7 != 0:
        continue
    if int(pandigitalString[5]+pandigitalString[6]+pandigitalString[7])%11 != 0:
        continue
    if int(pandigitalString[6]+pandigitalString[7]+pandigitalString[8])%13 != 0:
        continue
    if int(pandigitalString[7]+pandigitalString[8]+pandigitalString[9])%17 == 0:
        print(pandigital)
        substringPandigitalSum += pandigital
        
print(substringPandigitalSum)
    