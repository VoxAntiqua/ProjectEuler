# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:25:10 2019

@author: Andrew's Laptop
"""

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.denom = bottom
        
    def __str__(self):
        return str(self.num)+"/"+str(self.denom)
    
    def __eq__(self,other):
        firstnum = self.num * other.denom
        secondnum = self.denom * other.num
        return firstnum == secondnum
    
    def dumbsimp(self):
        numlist = list(str(self.num))
        denomlist = list(str(self.denom))
        intersect = list(set(numlist).intersection(set(denomlist)))
        if intersect != ['0'] and intersect != []:
            numlist.remove(intersect[0])
            denomlist.remove(intersect[0])
            newfrac = Fraction(int(numlist[0]), int(denomlist[0]))
        else:
            newfrac = Fraction(self.num,self.denom)
        return newfrac


for den in range(11,100):
    for num in range(10, den):
        frac = Fraction(num,den)
        simpd = frac.dumbsimp()
        if frac.num != simpd.num and frac.denom != simpd.denom:
            if frac == simpd:
                print(frac)
                
387296 38729600