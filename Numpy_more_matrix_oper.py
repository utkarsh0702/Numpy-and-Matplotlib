# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:27:24 2018

@author: Utkarsh
"""

import numpy as np

a= np.array([[1,2],[3,4]])
print(a)

# inverse of a matrix
print(np.linalg.inv(a))

#determinant of a matrix
print(np.linalg.det(a))

#diagnol elements of matrix
print(np.diag(a))

#trace of matrix
print(np.trace(a))

# eign values and eign vectors
a1= np.random.randn(4,4)
print(a1)

# covariance of each element of matrix
cov= np.cov(a1)

print(np.linalg.eigh(cov))
print(np.linalg.eigvalsh(cov))


