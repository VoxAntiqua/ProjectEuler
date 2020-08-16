# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:03:30 2019

@author: andre
"""

#Project Euler problem 39

def IsRightTriangle(sides):
    """
    Input: list of integers
    Output: True if input side lengths form a right triangle, False otherwise.
    """
    hypot = max(sides)
    sides.remove(hypot)
    return sides[0]**2 + sides[1]**2 == hypot**2

def GenerateTriangles(perim):
    """
    Input: integer perimeter
    Output: list of length 3 lists of integers that add up to the input
    perimeter, with the following constraints:
        -No list is a permutation of another
        -No value in a list is greater than the sum of the other 2 values
        -No value in a list is greater than half the perimeter
    """
    triangles = []
    c = int(perim/2)
    while c >= int(perim/3):
        b = c
        a = perim - b - c
        while b >= a:
            if a != 0:
                triangles.append([a,b,c])
            a += 1
            b -= 1
        c -= 1
        
    return triangles

def PerimeterTest(n):
    """
    Input: integer n
    Output: number of distinct right triangles with perimeter n 
    """
    triangletest = GenerateTriangles(n)
    righttriangles = 0
    for triangle in triangletest:
        if IsRightTriangle(triangle):
            righttriangles += 1
    return righttriangles
        

best = 3
bestp = 120
for p in range(120,1001):
    test = PerimeterTest(p)
    if test > best:
        bestp = p
        best = test
print(bestp)