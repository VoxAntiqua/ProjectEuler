# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:23:09 2019

@author: Andrew's Laptop
"""

#Euler Project problem 23


#facdic = {}
#sumdic = {}
#abundants = []
absum = []
notabsum = []
#
#def ProperDivisors(n):
#    factors = []
#    for f in range(int(n/2),0,-1):
#        if f not in factors:
#            if n%f == 0:
#                factors.append(f)
#                if f in facdic:
#                    for x in facdic[f]:
#                        if x not in factors:
#                            factors.append(x)
#                
#    facdic[n] = factors
#    return factors
#        
#def SumDivisors():
#    for key in facdic:
#        if key not in sumdic:
#            sumdic[key] = sum(facdic[key])
#        
#for n in range(2,28124):
#    ProperDivisors(n)
#    
#SumDivisors()
#
#for num in sumdic:
#    if sumdic[num] > num:
#        abundants.append(num)

sums = [0]*28124
for x in range (0, len(abundants)):
    for y in range (x, len(abundants)):
            sumOf2AbundantNums = abundants[x]+abundants[y]
            if (sumOf2AbundantNums<= 28123):
                if (sums[sumOf2AbundantNums] == 0):
                    sums[sumOf2AbundantNums] = sumOf2AbundantNums

total = 0
for x in range (1,len(sums)):
    if (sums[x] == 0):
        total +=x

print('\n', total)

#        
#print(sum(notabsum))
    
