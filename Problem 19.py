# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:56:07 2019

@author: Andrew's Laptop
"""

#Euler Project problem 19

import datetime
from datetime import date,timedelta

testday = datetime.date(1901,1,1)
sundays = 0
d = timedelta(days=1)

while testday != datetime.date(2000,12,31):
    if testday.weekday() == 6 and testday.day == 1:
        sundays += 1
    testday += d

print(sundays)