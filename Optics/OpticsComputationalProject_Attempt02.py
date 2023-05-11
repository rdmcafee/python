# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:27:04 2021

@author: Mcrye
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import warnings

warnings.filterwarnings('ignore')

fig, ax = plt.subplots()
fig.set_size_inches(10, 8)
ax.set_title("Wave Equations")


# Ok Lets initialize some global variables

A_x = 5                     # Amplitude of wave in x direction
A_y = 5                     # Amplitude of wave in y direction.
 
wavelength = 500E-9         # wavelength in meters.
k = 2*np.pi/wavelength      # Wave-number, K
e_0 = 8.85E-12              #(A^2 * s^2 )/(N*m) Permitivity
mu_0 = 4*np.pi*1E-7         #(Kg * m) / (s^2 A^2) Permeability
c = np.sqrt(1/(e_0*mu_0))   #Speed of EM wave in a vacuum. 

phi_x = 0                   #Phase shift for x wave
phi_y = 0                   #Phase shift for y wave

w_x = k*c                   #angular frequency of x wave
w_y = k*c                   #angular frequency of y wave

T = (2*np.pi)/w_x           #Period
time = T                    #seconds

s = 1                       #This is just to adjust time step if needed

#Here I would just like to format some of the critical data for display

v = np.format_float_scientific(w_x/k, precision=3)
frequency = np.format_float_scientific(1/T, precision=3)
timeStep = np.format_float_scientific(T/(4**4), precision=3)                     

def Psi_x(A_x, phi_x, t):
    I = A_x*np.sin(-1*w_x*s*t + phi_x)
    return I

def Psi_y(A_y, phi_y, t):
    I = A_y*np.sin(-1*w_y*s*t + phi_y)
    return I

def Sum(A_x, A_y, phi_x, phi_y, t):
    I = np.sqrt((Psi_x(A_x, phi_x, t)**2) + (Psi_y(A_y, phi_y, t)**2))
    return I

print("Program initializing")

#Printing some of the critical data.
print("\nWave velocity: " + str(v) + " m/s")  #EM Wave velocity: w/k = c
print("\nWavelength: " + str(wavelength*1E9) + " nm") 
print("\nFrequency: " + str(frequency) + " Hz")
print("\nTime step: " + "T/256 = " + str(timeStep), " s\n")
print("\nDivide by zero investigation at t = 0 : " + str(Psi_x(10, 0, 0)/Sum(10, 5, 0, 0, 0)))

i = 0
while i < time*(1+(4**-4)):      #this just stops the graph right at 1 period.
    plt.cla()
    plt.clf()
    
    plt.style.use('Solarize_Light2')

    plt.xlim(-1.2,1.2)
    plt.ylim(-1.2,1.2)
    
    #Plotting the first condition
    plt.plot(Psi_x(10, 0, i)/Sum(10, 5, 0, 0, i), 
             Psi_y(5, 0, i)/Sum(10, 5, 0, 0, i), color = 'k', marker = 'x', 
             markersize = 5, label=r'$\Psi_{01}$')
    
    plt.arrow(0,0, (Psi_x(10, 0, i)/Sum(10, 5, 0, 0, i)), 
              (Psi_y(5, 0, i)/Sum(10, 5, 0, 0, i)), color='k')
    
    #Plotting the second condition
    plt.plot(Psi_x(10, 0, i)/Sum(10, 5, 0, np.pi/2, i), 
             Psi_y(5, np.pi/2, i)/Sum(10, 5, 0, np.pi/2, i), color = 'g', 
             marker = 'x', markersize = 5, label=r'$\Psi_{02}$')
    
    plt.arrow(0,0, (Psi_x(10, 0, i)/Sum(10, 5, 0, np.pi/2, i)), 
              (Psi_y(5, np.pi/2, i)/Sum(10, 5, 0, np.pi/2, i)), color='g')
    
    #Plotting the third condition
    plt.plot(Psi_x(10, 0, i)/Sum(10, 5, 0, -1*np.pi/2, i), 
             Psi_y(5, -1*np.pi/2, i)/Sum(10, 5, 0, -1*np.pi/2, i), 
             color = 'b', marker = 'x', markersize = 5, label=r'$\Psi_{03}$')
    
    plt.arrow(0,0, (Psi_x(10, 0, i)/Sum(10, 5, 0, -1*np.pi/2, i)), 
              (Psi_y(5, -1*np.pi/2, i)/Sum(10, 5, 0, -1*np.pi/2, i)), 
              color='b')
    
    #Plotting the fourth condition
    plt.plot(Psi_x(10, np.pi/4, i)/Sum(10, 5, np.pi/4, -1*np.pi/4, i), 
             Psi_y(5, -1*np.pi/4, i)/Sum(10, 5, np.pi/4, -1*np.pi/4, i), 
             color = 'r', marker = 'x', markersize = 5, label=r'$\Psi_{04}$')
    
    plt.arrow(0,0, (Psi_x(10, np.pi/4, i)/Sum(10, 5, np.pi/4, -1*np.pi/4, i)), 
              (Psi_y(5, -1*np.pi/4, i)/Sum(10, 5, np.pi/4, -1*np.pi/4, i)), 
              color='r')
    
    #Plotting the fifth condition
    plt.plot(Psi_x(10, 0, i)/Sum(10, 5, 0, -1*np.pi/4, i), 
             Psi_y(5, -1*np.pi/4, i)/Sum(10, 5, 0, -1*np.pi/4, i), 
             color = 'purple', marker = 'x', markersize = 5, 
             label=r'$\Psi_{05}$')
    
    plt.arrow(0,0, (Psi_x(10, 0, i)/Sum(10, 5, 0, -1*np.pi/4, i)), 
              (Psi_y(5, -1*np.pi/4, i)/Sum(10, 5, 0, -1*np.pi/4, i)), 
              color='purple')
    
    plt.axhline(y=0, color='k', linewidth = 0.5)
    plt.axvline(x=0, color='k', linewidth = 0.5)
    plt.legend(loc = 'upper left', frameon = True, ncol = 3 )
    plt.title("Time Evolution of Wave Equations at z = 0")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.pause(0.1)
    plt.draw()

    i += T/(4**4)           #Using a sufficiently small time step
    
print("Program concluded")


