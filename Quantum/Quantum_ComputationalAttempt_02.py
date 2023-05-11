# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 20:32:07 2021

@author: Mcrye
"""
"""Heres an attempts to make things run a little faster"""

import matplotlib
matplotlib.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc
import sys

x = np.linspace(0, 100, 1000).astype(complex).reshape(1000,1)

fig = plt.figure(figsize=(10,5))

n = 200 #quantum number
h = 1
m = 2
L = x[-1]
k = 40
a = 0.1
nn = np.arange(1,n+1).reshape(1,n)

time = 200
dt = 1

#A = np.sqrt(3)*(2/np.pi)**3
#imag = complex(0, 1)
global z
global y

z = (np.pi+L*(k-1j*L))/(2*L)
y = 0.5*(k+1j-(np.pi/L))   
def En():
    En = (((nn*np.pi)**2 * h)/ (2*m*(L**2)))
    return En
#print(imag)


def Phi():
    phi = (np.sin( (nn * np.pi * x) /L ) )
    return phi
    
def Cn_Constants():
    Cn = np.zeros((n,1),dtype=complex)
    global A
    A = np.exp(((k**2)*a)/4)*((a*np.pi)/(8*(L**(6))))**(1/4)
    
    for i in range(0,n):
        Cn[i,0] = A*(np.exp((-1*np.pi * h*i)*(((2*a*k*L) + (np.pi*h*i))/(4*a*(L**2)))))*((sc.erfi(z)-sc.erfi(z))+(np.exp(np.pi*k/L)*(sc.erfi(y)-sc.erfi(y))))
    Cn = Cn.reshape(1,n)
    #print(str(Cn.shape))
    return Cn

#Psi_xt = 0

En()
Phi()
Cn_Constants()
print("Program should start here")

for i in range(0, time, dt): 
    
    t = i
    Psi_xt = np.zeros((len(x),1),dtype=complex)
    for j in range(1, n):
        Psi_xt[:,0] = Psi_xt[:,0] + (Cn_Constants()[:,j]*Phi()[:,j]*np.exp(-1j*En()[0,j]*1*t))
  
    print("Pass " + str(i))
    print("Phi = " + str(Phi().shape))   
    print("Psi = " + str(Cn_Constants().shape))
    print(A)
    print(np.abs(Psi_xt))
    #print(str(np.trapz(Psi_xt[i:1000,0]*np.conj(Psi_xt[i:1000,0]), x[i:1000,0])))
    #plt.plot(x, np.real(Psi_xt))
    #plt.plot(x, np.imag(Psi_xt))
    plt.plot(x, 1E10*Psi_xt*np.conj(Psi_xt))
    plt.xlim(-5,105)
    plt.ylim(-1, 1)
    left_wall_line = plt.axvline(0, c='k', linewidth=1)
    right_well_line = plt.axvline(100, c='k', linewidth=1)
    plt.pause(0.01)   
    plt.draw()
    plt.clf()
    plt.cla()
    
    #print(Psi_xt)
   #print(np.conjugate(Psi_xt))

#print("Calculating Cn " + str(Cn_Constants().shape))
#print("Calculating Eigenenergies " + str(En().shape))

sys.exit("program concluded")