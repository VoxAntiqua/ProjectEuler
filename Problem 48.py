# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:22:49 2019

@author: andre
"""

#Project Euler Problem 48

total = 0
for n in range(1,1001):
    total += n**n
totalString = str(total)
lastTenDigits = totalString[len(totalString)-10:]

print(lastTenDigits)