# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:47:58 2019

@author: andre
"""

#Project Euler Problem 40

def GenChampernowne(n):
    """
    Generates n digits of Champernowne's constant as a string
    """
    x = 1
    const = ""
    while len(const) < n:
        const += str(x)
        x += 1
    return const    

champ = GenChampernowne(1000000)
print(
      int(champ[0])
      *int(champ[9])
      *int(champ[99])
      *int(champ[999])
      *int(champ[9999])
      *int(champ[99999])
      *int(champ[999999])
      )
    