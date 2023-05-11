# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:27:04 2021

@author: Mcrye
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib import style
import warnings

warnings.filterwarnings('ignore')

#fig, ax = plt.subplots()
#fig.set_size_inches(8, 4)


# Ok Lets create some global variables
x = np.linspace(-10,10, 1000)
A_x = 5 # Amplitude of wave in x direction
A_y = 5 # Amplitude of wave in y direction. 
wavelength = 500E-9 # wavelength in nanometers.
k = 2*np.pi/wavelength # Wave-number K

theta = np.linspace(0, 2*np.pi, 1000) #preparing for polar coordinates. 

phi_x = 0 #Phase shift for x wave
phi_y = np.pi/2 #Phase shift for y wave

w_x = 0.05 #angular frequency
w_y = 0.05
T = (2*np.pi)/w_x #Period
time = T #seconds
z = np.zeros((len(x),1))

style.use('Solarize_Light2')

#for i in range(0, time):
print("Program initializing")
s = 1
i = 0
while i < time+1:
    plt.cla()
    plt.clf()
    plt.style.use('Solarize_Light2')
        
    #ax.set_rmax(A)
    #ax.grid(True)
    #ax.plot(theta, np.sqrt(((Psi_x(0.01*i)*np.cos(theta))**2) + (Psi_y(0.01*i)*np.sin(theta)**2)))
    #ax.legend(loc = 'upper right', frameon = True)
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    Psi_x = A_x*np.sin(-1*w_x*s*i + phi_x)

    Psi_y = A_y*np.sin(-1*w_y*s*i + phi_y)

    Sum = np.sqrt((Psi_x**2) + (Psi_y**2))
    
    plt.plot(Psi_x/Sum, Psi_y/Sum, color = 'k', marker = 'x', markersize = 5)

    plt.arrow(0,0, (Psi_x/Sum), (Psi_y/Sum))
    plt.axhline(y=0, color='k', linewidth = 0.5)
    plt.axvline(x=0, color='k', linewidth = 0.5)
    #plt.plot(x, Psi_y(0.1*i))
    #plt.plot(x,(Psi_x(0.01*i))**2 + (Psi_y(0.01*i)**2))
    plt.pause(0.2)
    plt.draw()
    print(str(Psi_x/Sum) +' '+str(Psi_y/Sum))
    #plt.cla()
    #plt.clf()
    i += 1
    

#sys.exit("Program concluded")
#plt.show()