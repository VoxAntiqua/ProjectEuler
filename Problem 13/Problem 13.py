# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 00:00:12 2019

@author: Andrew's Laptop
"""

with open('p13.txt', 'r') as file:
    numbers = file.read().splitlines()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    sum = sum(numbers)
    sumstr = str(sum)
    

print(sumstr[0:10])