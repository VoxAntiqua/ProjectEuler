# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:36:23 2019

@author: Andrew's Laptop
"""

#Euler Project problam 16

import math
num = list(str(int(2**1000)))
intlist = []
for i in range(len(num)):
    intlist.append(int(num[i]))
print(sum(intlist))