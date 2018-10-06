# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:43:49 2018

@author: Utkarsh
"""

import numpy as np;

l= [1,2,3,4,5]
a= np.array([1,2,3,4])
l.append(3)
print(l)

#to insert elements in a new list for doubling elements
l1=[]
for i in l:
    l1.append(i+i)
    
print(l1)

# to double elements
print(a+a)

# squaring of elements
#list
l2=[]
for i in l:
    l2.append(i*i)
    
print(l2)
    
#array
print(a*a)

# square root of a cube
print(np.sqrt(a*a*a))

#log of a 
print(np.log(a))
