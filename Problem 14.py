# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 08:58:00 2019

@author: Andrew's Laptop
"""

#Project Euler problem 14

dic = {}

def collatz(n):
    seq = []
    seq.append(n)
    term = n
    while term > 1:
        if term%2 == 0:
            term = int(term/2)
            if term in dic:
                seq += dic[term]
                break
            else:
                seq.append(term)
        else:
            term = int(term*3+1)
            if term in dic:
                seq += dic[term]
                break
            else:
                seq.append(term)
    dic[n] = seq
    return len(seq)

maxiter = 0
maxnum = 0

for i in range(1000000):
    iter = collatz(i)
    if iter > maxiter:
        maxiter = iter
        maxnum = i

print(maxnum,maxiter)