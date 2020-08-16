# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:12:32 2019

@author: Andrew's Laptop
"""

#Project Euler problem 9

for a in range(1,1000):
    for b in range(a, 1000-a):
        c = 1000-a-b
        if a**2 + b**2 == c**2:
            print(a,b,c)
            print("Product:", a*b*c)