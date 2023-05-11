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

plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()
fig.set_size_inches(8, 4)
n = 1
x = np.linspace(0,40, 1000)
theta = np.linspace(0, np.pi*10, 1000)
time = 500 #seconds
style.use('Solarize_Light2')
def Sin(t):
    I = np.sin((n*theta/2)-t) + np.sin((n*theta/2)-2*t)
    return I
def Wave(x):
    I = np.sin(x)
    return I
#for i in range(0, time):
i = 0
while i < time:
    plt.ylim(-2,2)
    plt.xlim(0,np.pi * 10)
    plt.axhline(0, color = 'k', linewidth = 2)
    plt.plot(x, Wave(x-(i/20)), label = r'$\Psi(x,t)$')
    plt.legend(loc = 'upper right', frameon = True)
    plt.pause(0.01)
    plt.clf()
    plt.cla()
    i += 1
    
plt.close()
sys.exit("Program concluded")
#plt.show()