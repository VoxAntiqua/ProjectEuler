# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 00:44:56 2019

@author: Andrew's Laptop
"""

#Euler Project problem 27

def IsPrime(n):
    if n<2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    prime = True
    for x in range(3, int(n**0.5)+1, 2):
        if n%x == 0:
            prime = False
    return prime

primedic = {}
maxprimes = 0
maxa = 0
maxb = 0

for a in range(-999,1000):
    for b in range(-1000,1001):
        i = 0
        while True:
            term = i**2 + a*i + b
            if term not in primedic:
                primei = IsPrime(term)
                primedic[term] = primei
            if term in primedic:
                primei = primedic[term]
            if primei:
                i += 1
            if not primei:
                break
        if i > maxprimes:
            maxprimes = i
            maxa = a
            maxb = b