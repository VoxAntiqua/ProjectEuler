# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:58:28 2019

@author: andre
"""

#Project Euler Problem 41

import numpy as np
from itertools import permutations

def GeneratePandigitals():
    """
    Generates all n-digit integers that contain the digits 1 through n with at
    least 4 digits, descending in value.
    """
    return (
            [int(''.join(p)) for p in permutations("1234")]
            +[int(''.join(p)) for p in permutations("12345")]
            +[int(''.join(p)) for p in permutations("123456")]
            +[int(''.join(p)) for p in permutations("1234567")]
            +[int(''.join(p)) for p in permutations("12345678")]
            +[int(''.join(p)) for p in permutations("123456789")]
            )
    
def IsPrime(n):
    """
    Determines if n is prime. Not very efficient, use to find the first prime
    in a list.
    """
    if n%2 == 0:
        return False
    else:
        prime = True
        for j in range(2,int(np.sqrt(n))+1):
            if n%j == 0:
                prime = False
                break
        return prime
    
pandigs = GeneratePandigitals()
pandigs.reverse()

for num in pandigs:
    if IsPrime(num):
        print(num)
        break