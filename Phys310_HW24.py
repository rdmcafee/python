# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:04:27 2021

@author: Mcrye
"""

from pylab import *
from numpy import *
import matplotlib.pyplot as plt
import numpy as np

figure, (ax1) = plt.subplots(1)

# f(x)= e^(-x^2)
x = linspace(2.4,40,1000)
t = linspace(0,2.4, 1000)
f = exp(-0.04*(x-2.398))*(0.178927*sin(1.57029*(x-2.398))+7.02416*cos(1.57029*(x-2.398)))+3.97584
g = 4.905*((t)**(2))-28.2
a = exp(-0.04*(x-2.398))*(0.178927+7.02416)+3.97584
b = -exp(-0.04*(x-2.398))*(0.178927+7.02416)+3.97584
ax1.plot(x,f,x,a, 'r',x,b, 'r', t,g, 'b')

ax1.set_ylim(-28.2,12)
ax1.set_xlim(-2, 50)

ax1.grid()
plt.show()