# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:55:34 2019

@author: Andrew's Laptop
"""

#Euler Project problem 17

numdic = {
        0:"",
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen",
        20:"twenty",
        30:"thirty",
        40:"forty",
        50:"fifty",
        60:"sixty",
        70:"seventy",
        80:"eighty",
        90:"ninety",
        100:"hundred"
        }

def numtostringones(n):
    assert (n >= 1 and n < 10)
    return numdic[n]

def numtostringtens(n):
    assert (n >= 10 and n <= 99)
    tens = n-n%10
    ones = n%10
    if n <= 19:
        return numdic[n]
    else:
        return numdic[tens]+numdic[ones]

def numtostringhundreds(n):
    assert (n >= 100)
    hundreds = int(n/100)
    tens = n%100
    if n%100 == 0:
        return numdic[hundreds]+"hundred"
    elif tens >= 10:
        return numdic[hundreds]+"hundredand"+numtostringtens(tens)
    else:
        return numdic[hundreds]+"hundredand"+numtostringones(tens)
    
def numtostring(n):
    if (n >= 1 and n < 10):
        return numtostringones(n)
    elif (n >= 10 and n < 100):
        return numtostringtens(n)
    else:
        return numtostringhundreds(n)
    
numstring = ""

for i in range(1,1000):
    number = numtostring(i)
    number.replace(" ","")
    numstring += number
    
numstring += "onethousand"
print(len(numstring))
    
