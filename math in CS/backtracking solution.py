# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:36:45 2020

@author: JingQIN
"""
from sys import exit

def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n):
    if len(perm) == n:
        print(perm)

#        exit()
        
    for k in range(n):
        if k not in perm:
            perm.append(k)
            
            if can_be_extended_to_solution(perm):
                extend(perm, n)
                
            perm.pop()
            
extend(perm=[], n = 8)

    