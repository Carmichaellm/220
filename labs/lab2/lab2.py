"""
Name: Liam Carmichael
lab2.py

Problem:
Write a Python program designed to output
the RMS (root-mean-square) Average,
the Harmonic Mean, and the Geometric Mean

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math #needed for squareroot

#inital values
values_entered = eval(input("enter the values to be entered: "))
rms = 0
hrmnc_m = 0
gmtrc_m = 1 #must start as 1 for multiplication

#first computations
for i in range(values_entered): #place repeated math in the body
    value = eval(input("enter value: "))
    rms = rms + (value**2)
    hrmnc_m = hrmnc_m + (1/value)
    gmtrc_m = gmtrc_m * value

#second computations
rms = math.sqrt(rms/values_entered)
hrmnc_m = (values_entered/hrmnc_m)
gmtrc_m = gmtrc_m**(1/values_entered)

#rounding
rms = round(rms,3)
hrmnc_m = round(hrmnc_m,3)
gmtrc_m = round(gmtrc_m,3)

#print final values
print("RMS Average:", rms)
print("Harmonic Mean:", hrmnc_m)
print("Geometric Mean:", gmtrc_m)

