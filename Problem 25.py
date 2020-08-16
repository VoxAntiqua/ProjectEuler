# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 23:40:51 2019

@author: Andrew's Laptop
"""

#Euler Project problem 25

fibs = [1,1]

i = 2

while True:
    fibs.append(fibs[i-2]+fibs[i-1])
    if len(str(fibs[i-2]+fibs[i-1])) >= 1000:
        print(i+1)
        break 
    i += 1       