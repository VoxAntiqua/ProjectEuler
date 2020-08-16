# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 23:48:39 2019

@author: Andrew's Laptop
"""

def Expansion(n):
    """
    Returns the number of repeating digits in the decimal expansion of 1/n
    """
    
    digits = []
    r = 1
    remainders = []
    remainders2 = []
    
    while True:
        dig = int((r*10)/n)
        r = (r*10)%n
        digits.append(dig)
        if r in remainders2:
            break
        elif r in remainders:
            remainders2.append(r)
        else:
            remainders.append(r)

     
    return len(remainders)

maxrepeats = 1
maxdem = 1

for n in range(2,1000):
    if Expansion(n) > maxrepeats:
        maxrepeats = Expansion(n)
        maxdem = n
        
print(maxdem)