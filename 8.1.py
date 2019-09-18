# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:04:14 2019

@author: Darshak
"""
# Brute Force
n = input("Enter Steps: ")
def countways(n):
    
    if(n<0):
        return 0
    if(n == 0):
        return 1
    else:
        return countways(n-1)+countways(n-2)+countways(n-3)
    
print(countways(n))

# Memoization
def countways(n):
    mem = [0]*(n+1)
    mem[0] = 1
    mem[1] = 1
    mem[2] = 2
    for i in range(3, n+1):
        mem[i] = mem[i-1]+mem[i-2]+mem[i-3]
    return mem[n]

print(countways(n))
