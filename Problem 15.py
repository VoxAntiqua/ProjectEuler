# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:30:25 2019

@author: Andrew's Laptop
"""

#Euler Project problem 15

import math

def bincoeff(a,b):
    return (math.factorial(a))/(math.factorial(b)*math.factorial(a-b))

print(bincoeff(40,20))