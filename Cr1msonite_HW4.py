# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:54:31 2021

@author: iabustan
"""

#Create functions where anything that's passed onto this function is added to this list.
MyUniqueList=[]
myLeftovers=[]

print(MyUniqueList)
print(myLeftovers)

#Function to add elements into list 
def AddtoList():
    if NewNumber not in MyUniqueList:
        MyUniqueList.append(NewNumber)
        print("True. Added to Unique list")
        print(MyUniqueList)       
    else:
        myLeftovers.append(NewNumber)
        print("False. Added to Leftovers")
        print(myLeftovers)

#Test first element if it can be added to the list.
NewNumber=4
print(AddtoList())

#Test to add the 2nd element to check for unique value
NewNumber=2
print(AddtoList())

#Test to add the 3rd element to check for duplicate value
NewNumber=2
print(AddtoList())
