# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:12:25 2018

@author: Utkarsh
"""

""" *A Vector is a one dimmensional array
      A Matrix is a two dimmensional array
"""
import numpy as np

m= np.matrix([[1,2],[3,4]])
print(m)

a= np.array(m)
print(a)

#Transpose of a matrix
print(a.T)

#Vector of zeroes
m1= np.zeros(10)
print(m1)

#matrix of zeroes and ones
print(np.zeros((4,4)))

print(np.ones((4,4)))

#matrix of random numbers
m2= np.random.random((4,4))
print(m2)

#mean and variance of matrix of random numbers
print(m2.mean())
print(m2.var())

