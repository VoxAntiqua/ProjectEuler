# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 09:09:50 2019

@author: Andrew's Laptop
"""

#Euler Project problem 29

terms = []

for a in range(2,101):
    for b in range(2,101):
        if a**b not in terms:
            terms.append(a**b)
            
print(len(terms))