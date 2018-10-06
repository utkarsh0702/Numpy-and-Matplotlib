# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:58:59 2018

@author: Utkarsh
"""

import numpy as np

a= np.array([1,2])
b= np.array([2,3])
dot=0
# through dot methord

for e,f in zip(a,b):
    dot+= e*f
    
print(dot)

#sum function for calculating sum of elements of arrays
print(np.sum(a*b))

print((a*b).sum())

#calculate angle between a and b
amag= np.linalg.norm(a)
print(amag)

cos= a.dot(b)/(np.linalg.norm(a)*np.linalg.norm(b))
print(cos)