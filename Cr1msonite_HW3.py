# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:20:09 2021

@author: iabustan
"""

#First Function: if

DedicatedRequest = True
DevHrs = 320
Applications = 2
ProjectType = "Complicated"

#print(Request,DevHrs,Applications)

if DedicatedRequest == True and ProjectType == "Complicated":
    Manpower = Applications * DevHrs / 160
print(Manpower)

#Second Function: elif

a = 1
b = 2
c = a+b
Argument = True
print(a+b)

if Argument == True and a + b == 3:
     c = 3

elif c > 3:
    Argument = False

print(c,Argument)

#Third Function: else

PlayerHeight = 6.8
BBallRequirement = 7.0
PassApplication = "Yes"

if PlayerHeight >= BBallRequirement:
    PassApplication = "Yes"
    
else: PassApplication ="No"

print(PassApplication)
