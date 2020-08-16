# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 23:24:42 2019

@author: Andrew's Laptop
"""

#Project Euler problem 38

def IsPandigital(nstr):
    if len(nstr) == 9:
        for dig in "123456789":
            if dig not in nstr:
                return False
                break
        return True
    return False

def StrMultiples(x):
    m = 2
    xstr = str(x)
    while len(xstr) < 9:
        xstr = xstr + str(x*m)
        m += 1
    return xstr

maxpandig = 123456789
for a in range(1,10000):
    testpandig = StrMultiples(a)
    if IsPandigital(testpandig):
        if int(testpandig) > maxpandig:
            maxpandig = int(testpandig)
            print(maxpandig)