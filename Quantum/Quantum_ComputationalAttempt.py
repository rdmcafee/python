# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:44:07 2021

@author: Mcrye
"""
import matplotlib
matplotlib.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sc
import sys

x = np.linspace(0, 100, 1000).astype(complex).reshape(1000,1)
fig, ax = plt.subplots()
fig.set_size_inches(10, 5)

n = 100 #quantum number
h = 1
m = 2
L = x[-1]
k = 20
a = 0.1
nn = np.arange(1,n+1).reshape(1,n)

time = 100 
dt = 1

#A = np.sqrt(3)*(2/np.pi)**3
#imag = complex(0, 1)

def Psi_Normalized():
    psi_x0 = (np.exp(1j*k*x - a*(x**2))).reshape(len(x),1)
    global A
    A = 1/(np.sqrt(sc.simps((np.conj(psi_x0[:,0])*psi_x0[:,0]), x[:,0])))
    Psi_N = A*psi_x0
    return Psi_N
    print("psi_x0: " + str(psi_x0.shape))
    
def En():
    En = (((nn*np.pi)**2 * h)/ (2*m*(L**2)))
    return En

def Phi():
    phi = np.sqrt(2/L)*np.sin( (nn * np.pi * x) /L ) 
    return phi
    
def Cn_Constants():
    Cn = np.zeros((n,1),dtype=complex)
    
    #for i in range(0,n):
    i = 0
    while i < n:
        #print("Cn = " + str(Cn.shape))
        #print("Phi = " + str(Phi().shape))
        #print("Psi = " + str(Psi_Normalized().shape))
        Cn[i,0] = (sc.simps((Phi() * Psi_Normalized())[:,i], x[:,0]))
        i += 1
    Cn = Cn.reshape(1,n)
    return Cn

print("Program should start here")
print("Cn shape = " + str(Cn_Constants().shape))
print("Phi shape = " + str(Phi().shape))
print("En shape = " + str(En().shape))
    
for i in range(0, time, dt): 
    t = i
    Psi_xt = np.zeros((len(x),1),dtype=complex).reshape(len(x),1)
    for j in range(0, n):
                 
        Psi_xt[:,0] = Psi_xt[:,0] + (Cn_Constants()[0,j]*Phi()[:,j]*np.exp(-1j*En()[0,j]*10*t))
        print("working on things " + str(i) + " " + str(j))
    print(A)    
    print(Psi_xt)
    print("Working on things " + str(i) + str(j))
    ax.clear()
    plt.xlim(-5,105)
    plt.ylim(-0.2, 0.2)
    left_wall_line = plt.axvline(0, c='k', linewidth=1)
    right_well_line = plt.axvline(100, c='k', linewidth=1)
    ax.plot(x, 1E3*np.real(Psi_xt))
    ax.plot(x, 1E3*np.imag(Psi_xt))
    ax.plot(x, 1E3*np.abs(Psi_xt))
    plt.pause(0.001)
    plt.draw()
    #plt.clf()
    #plt.cla()
    
sys.exit("program concluded")