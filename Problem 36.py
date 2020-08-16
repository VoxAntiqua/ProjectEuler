# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:18:17 2019

@author: Andrew's Laptop
"""

def IsPalindrome(x):
    return str(x) == str(x)[::-1]

def IntToBin(x):
    return bin(x)[2:]

doublepalindromes = []

for n in range(1,1000000):
    if IsPalindrome(n):
        if IsPalindrome(IntToBin(n)):
            doublepalindromes.append(n)
            
sumpal = sum(doublepalindromes)
print(sumpal)