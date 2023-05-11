# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:44:07 2021

@author: Mcrye
"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import scipy.integrate as sc
import sys
import warnings
import time as ti

#clearing any "casting" warnings from playing with arrays of different types
warnings.filterwarnings('ignore')

x = np.linspace(0, 100, 1000).astype(complex).reshape(1000,1)
xx = np.linspace(-50,50,1000).astype(complex).reshape(1000,1)

style.use('Solarize_Light2')

fig, ax = plt.subplots()
fig.set_size_inches(10, 5)


n = 500 #quantum number
h = 1.05E-34
m = 9.109E-31
L = x[-1] # grabs the final value of my x[] array
k = 2
#a =  ((1j*k*L/2)-1)*((2/L)**2) \\playing around with different values of a
a = 0.01
#creating an array to iterate the Sum of the Final expression. 
nn = np.arange(1,n+1).reshape(1,n)

time = 10000 

#defining the original wave equation
psi_x0 = (np.exp(((1j*k*(x-50)) - a*((x-50)**2))).reshape(len(x),1))

#ensuring that the normalization constant remains low error
A = 1/(np.sqrt(sc.simps((np.conj(psi_x0[:,0])*psi_x0[:,0]), xx[:,0])))
Psi_N = A*psi_x0
print("psi_x0: " + str(psi_x0.shape)) #monitoring array shapes
    
#Energy expression
En = ((((nn*np.pi)**2) *h)/ (2*m*((L/2)**2)))

#Fourier transporm expression
phi = np.sqrt(2/(L))*np.sin( (nn * np.pi * (x) /(L) )) 

#Defining an array to put all my (possibly) complex Cn values in, then 
#iterating their calculation.    
Cn = np.zeros((n,1),dtype=complex)
i = 0
while i < n:
    Cn[i,0] = (sc.simps((phi * Psi_N)[:,i], x[:,0]))
    i += 1
Cn = Cn.reshape(1,n)

#again, monitoring the array shapes to ensure compatability
print("Program should start here")
print("Cn shape = " + str(Cn.shape))
#print("Cn Array = " + str(Cn[:]))
print("Phi shape = " + str(phi.shape))
#print("Phi Array = " + str(phi[:]))
print("En shape = " + str(En.shape))
#print("En Array = " + str(En[:]))
 
#animation magic happens here. Iterative calculation of the final wave equation
#for each new time step, then clearing the old graph. Then we must draw() a new graph in the figure (for each step)
for i in range(0, time): 
    
    t = i
    Psi_xt = np.zeros((len(x),1),dtype=complex).reshape(len(x),1)

    for j in range(0, n):
        Psi_xt[:,0] = Psi_xt[:,0] + (Cn[0,j]*phi[:,j]*np.exp(-1j*En[0,j]*2000*t))

    print("Ensuring Normalization" + str(sc.simps((Psi_xt*np.conj(Psi_xt))[:,0], xx[:,0])))    
    #print(r'$\Psi(x,t)$ = ' + str(np.abs(Psi_xt[j,0])))
    #style.use('Solarize_Light2') #just making things look nice...
    # The following plots look cool, but are ultimately unecessary for our project...We're only concerned with the probability function
    #plt.plot(xx, np.real(Psi_xt),'r', label = r'$\Psi(x,t)$', linewidth = 0.5)
    #plt.plot(xx, np.imag(Psi_xt),'b', label = r'$\Psi^{*}(x,t)$', linewidth = 0.5)
    #plt.plot(xx, np.abs(Psi_xt), 'g', label = r'$|\Psi(x,t)|$', linewidth = 1)
    
    #creating axes, limits, legend, etc...
    plt.plot(xx, 1*np.conj(Psi_xt)*Psi_xt, 'g', label = '$\Psi^{*}(x,t)\Psi(x,t)$')
    plt.legend(loc = 'upper center', frameon = True, ncol = 1 )
    plt.xlim(-55,55)
    plt.ylim(-2E-1, 2E-1)
    plt.axvline(-50, c='k', linewidth = 2)
    plt.axvline(50, c='k', linewidth = 2)
    plt.axhline(0, c='k', linewidth = 1)
    plt.title('$Time$' +" "+ '$evolution$' + " " + '$of$' + " " + '$probability$' + " " + '$vs$' + " " + '$position$')
    plt.xlabel('$x$')
    plt.ylabel('$Probability$')
    
    plt.pause(0.0001)
    #ti.sleep(0.00001)
    plt.draw()
    plt.cla()
    plt.clf()

    
#after the last iteration, the program closes with a message explaining that the program has concluded.    
sys.exit("program concluded")
