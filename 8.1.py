# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:04:14 2019

@author: Darshak
"""
n = input("Enter Steps: ")
def countways(n):
    
    if(n<0):
        return 0
    if(n == 0):
        return 1
    else:
        return countways(n-1)+countways(n-2)+countways(n-3)
    
print(countways(n))