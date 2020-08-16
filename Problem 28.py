# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 08:49:40 2019

@author: Andrew's Laptop
"""

#Euler Project problem 28

term = 1
size = 1
terms = [1]
while size <= 1000:
    for i in range(4):
        term += size + 1
        print(term)
        terms.append(term)
    size += 2
        
print(sum(terms))