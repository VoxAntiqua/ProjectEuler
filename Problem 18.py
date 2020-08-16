# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:51:41 2019

@author: Andrew's Laptop
"""

#Euler Project problem 18

pathdict = {}

trianglestr = []
trianglestr.append("75".split())
trianglestr.append("95 64".split())
trianglestr.append("17 47 82".split())
trianglestr.append("18 35 87 10".split())
trianglestr.append("20 04 82 47 65".split())
trianglestr.append("19 01 23 75 03 34".split())
trianglestr.append("88 02 77 73 07 63 67".split())
trianglestr.append("99 65 04 28 06 16 70 92".split())
trianglestr.append("41 41 26 56 83 40 80 70 33".split())
trianglestr.append("41 48 72 33 47 32 37 16 94 29".split())
trianglestr.append("53 71 44 65 25 43 91 52 97 51 14".split())
trianglestr.append("70 11 33 28 77 73 17 78 39 68 17 57".split())
trianglestr.append("91 71 52 38 17 14 91 43 58 50 27 29 48".split())
trianglestr.append("63 66 04 68 89 53 67 30 73 16 69 87 40 31".split())
trianglestr.append("04 62 98 27 23 09 70 98 73 93 38 53 60 04 23".split())

tri = []
for sublist in trianglestr:
    ints = []
    for numstr in sublist:
        ints.append(int(numstr))
    tri.append(ints)
    


def FindMaxTotal(triangle):
    maxtotal = 0
    for i in range(len(triangle[13])):
        if triangle[13][i]+triangle[14][i] > triangle[13][i]+triangle[14][i+1]:
            total = triangle[13][i]+triangle[14][i]
        else:
            total = triangle[13][i]+triangle[14][i+1]
        pathdict[(13,i)] = total
        
    row = 12
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
