# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:37:10 2019

@author: Andrew's Laptop
"""

import math

def IsCuriousFact(n):
    digits = [int(d) for d in str(n)]
    facts = [math.factorial(f) for f in digits]
    if sum(facts) == n:
        return True
    else:
        return False
    

for m in range(10,10000000):
    if IsCuriousFact(m):
        print(m)