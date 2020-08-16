# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 23:33:51 2019

@author: Andrew's Laptop
"""

# Euler Project problem 24

def get_permutations(sequence):
    if len(sequence) <= 1:
        return [sequence]
    else:
        permutations = []
        firstchar = sequence[0]
        nextchars = sequence[1:]
        otherperms = get_permutations(nextchars)
        for seq in otherperms:
            for index in range(len(seq)+1):
                newperm = seq[0:index] + firstchar + seq[index:len(seq)+1]
                permutations.append(newperm)
        return permutations
    
perms = get_permutations("0123456789")

print(sorted(perms)[999999])