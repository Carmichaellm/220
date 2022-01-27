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
rms_acc = 0
hrmnc_acc = 0
gmtrc_acc = 1 #must start as 1 for multiplication

#first computations
for i in range(values_entered): #place repeated math in the accumulator
    value = eval(input("enter value: "))
    rms_acc = rms_acc + (value**2)
    hrmnc_acc = hrmnc_acc + (1/value)
    gmtrc_acc = gmtrc_acc * value

#second computations
rms_acc = math.sqrt(rms_acc/values_entered)
hrmnc_acc = (values_entered/hrmnc_acc)
gmtrc_acc = gmtrc_acc**(1/values_entered)

#rounding
rms_acc = round(rms_acc,3)
hrmnc_acc = round(hrmnc_acc,3)
gmtrc_acc= round(gmtrc_acc,3)

#print final values
print("RMS Average:", rms_acc)
print("Harmonic Mean:", hrmnc_acc)
print("Geometric Mean:", gmtrc_acc)

