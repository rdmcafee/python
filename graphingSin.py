# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 00:13:57 2019

@author: Mcrye
"""
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
x0 = 0.0
x1 = 10.0 
dx = 0.1
#n = int(ceil((x1-x0)/dx)+1)
#x = zeros((n,1),float)
#y = zeros((n,1),float)
#for i in range(n):
##    x[i] = x0 + i*dx
#    y[i] = sin(x[i])
#plot(x,y)
#show()

#Another Method for plotting sin with fewer lines of code
#x = linspace(0,10,10)
#y = sin(x)
#hold('on')
#plot (x,y)
#show()

#x=linspace (0,10,1000)
#y=sin(x)
fig = plt.figure()

i = 0
while i < 20:
    plt.plot(i, i, 'ro')
    plt.draw()
    print(str(i))
    plt.pause(2)
    i+=1
    
plt.show()
#hold('on')
#plot(x,y,':')
#hold('off')
#show()

