# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 23:55:44 2021

@author: Mcrye
"""

import numpy as np
import matplotlib.pyplot as plt
imag = complex(0,1)
k = 2
a = 2
x = np.linspace(0,10, 1000).astype(complex).reshape(1000,1)
n = 500
nn = np.arange(1,n+1).reshape(1,n)
L = x[-1]

psi_x0 = np.exp(1*imag*k*x-a*x**2).reshape(len(x),1)
#A = np.trapz(np.conj(psi_x0[:,0])*psi_x0[:,0], x[:,0])

#print(psi_x0)
print("Psi_x0 Size " + str(psi_x0.shape))

A = ( 1/(np.sqrt(np.trapz((np.conj(psi_x0[:,0])
            *psi_x0[:,0]), x[:,0]))))
Psi_N = A*psi_x0
print(A)
#print(str(Psi_N.shape))

Cn = np.zeros((n,1),dtype=complex)
#Cn = Cn.reshape(1,n)
def Phi():
    phi = (np.sin( (nn * np.pi * x) /L) )
    return phi
for i in range(0,n):
    Cn[i,0] = np.trapz((np.conj(Phi())* Psi_N)[:,i], x[:,0])
Cn = Cn.reshape(1,n)
print("Phi Size " + str(Phi().shape))    
print("nn Size " +str(nn.shape))
print("Cn Size " + str(Cn.shape))
print("Psi_N Size " + str(Psi_N.shape))

        

