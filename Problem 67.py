# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 16:07:44 2019

@author: Andrew's Laptop
"""

#Euler Project problem 67
triangle = [ x.split() for x in open('p067_triangle.txt').read().split('\n') if x != '' ]
    
tri = []
for sublist in triangle:
    ints = []
    for numstr in sublist:
        ints.append(int(numstr))
    tri.append(ints)

pathdict = {}
    
def FindMaxTotal(triangle):
    maxtotal = 0
    for i in range(len(triangle[98])):
        if triangle[98][i]+triangle[99][i] > triangle[98][i]+triangle[99][i+1]:
            total = triangle[98][i]+triangle[99][i]
        else:
            total = triangle[98][i]+triangle[99][i+1]
        pathdict[(98,i)] = total
        
    row = 97
    while row >= 0:
        for i in range(len(triangle[row])):
            if triangle[row][i]+pathdict[(row+1,i)] > triangle[row][i]+pathdict[(row+1,i+1)]:
                total = triangle[row][i]+pathdict[(row+1,i)]
            else:
                total = triangle[row][i]+pathdict[(row+1,i+1)]
            pathdict[(row,i)] = total
            if total > maxtotal:
                maxtotal = total
        row -= 1
    print(maxtotal)
    
FindMaxTotal(tri)