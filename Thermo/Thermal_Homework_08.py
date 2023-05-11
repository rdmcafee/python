# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 01:45:46 2022

@author: Mcrye
"""

import matplotlib.pyplot as plt
#import scipy as sc

plt.style.use('Solarize_Light2')

def plot (xVals, yVals, ax, c):
    ax.plot(xVals, yVals, color = c, linewidth = 1)
    
    
    ax.set_ylabel('Pressure: ' + r'$\frac{N}{m^2}$')
    ax.set_xlabel('Volume: ' + r'$m^3$')
    

def scatter(xVals, yVals, ax):
    ax.scatter(xVals, yVals, color = 'darkred', s = 8)
    