# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 22:30:29 2019

@author: Andrew's Laptop
"""

#Euler Project problem 12

def FindPrimeFactors(T):
    dic = {}
    i = 2
    while i <= T:
        if T%i == 0:
            T = T/i
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            i += -1
        i += 1
    return dic

def FindNumFactors(dic):
    powers = dic.values()
    product = 1
    for x in powers:
        product *= x+1
    return product

tri = 1
iter = 2

while True:
    tri = tri + iter
    iter += 1
    NumFactors = FindNumFactors(FindPrimeFactors(tri))
    print(tri,NumFactors)
    if NumFactors > 500:
        break