# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:06:08 2019

@author: Andrew's Laptop
"""

#Euler Project problem 22

f= open("p022_names.txt","r")
if f.mode == "r":
    contents = f.read()

contents = contents.replace("\"","")
names = contents.split(",")
names.sort()

alphavalues = {
        "A":1,
        "B":2,
        "C":3,
        "D":4,
        "E":5,
        "F":6,
        "G":7,
        "H":8,
        "I":9,
        "J":10,
        "K":11,
        "L":12,
        "M":13,
        "N":14,
        "O":15,
        "P":16,
        "Q":17,
        "R":18,
        "S":19,
        "T":20,
        "U":21,
        "V":22,
        "W":23,
        "X":24,
        "Y":25,
        "Z":26}

totalscore = 0
for i in range(len(names)):
    score = 0
    for letter in names[i]:
        score += (i+1)*alphavalues[letter]
    totalscore += score
    
print(totalscore)