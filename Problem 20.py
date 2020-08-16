# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:20:27 2019

@author: Andrew's Laptop
"""

#Euler Project problem 20

import math
bignum = math.factorial(100)

bigstr = str(bignum)
biglist = []

for dig in bigstr:
    biglist.append(int(dig))
    
print(sum(biglist))
    