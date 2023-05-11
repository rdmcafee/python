# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:56:15 2021

@author: Mcrye
"""
from pylab import *
from numpy import *
import matplotlib.pyplot as plt
import numpy as np

D = 10
E = 0.6

theta = linspace(0, 2*np.pi, 1000)

r = E*D/(1+E*cos(theta))
plt.polar(theta, r, 'b')
plt.show()