# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:37:57 2019

@author: Mcrye
"""

from pylab import *
from numpy import *
import matplotlib.pyplot as plt
import numpy as np

# f(x)= e^(-x^2)
x = linspace(-5,5,1000)
f = exp(-x**2)
plot(x,f), show()

# Now plot the derivative of the above function: f'(x)= (f(x+h)-f(x-h))/2h as
# h approaches 0
h = 0.001
df = zeros(1000,float)
for i in range(1000):
    df[i] = (exp(-(x[i]+h)**2)-exp(-(x[i]-h)**2))/(2*h)
plot(x, df, ':'), show()

# f(x) = e^(-xsin(x))

x=linspace(0,10,1000)
y=exp(-x)*sin(x)
plot(x,y,'r'), show()

# f(z,t) = Ae^(-b(z-vt)^2)
z=linspace(0,100,1000)
y= exp(10*(z-100)*(z-100))
plot(z,y,'r'), show()

x = [0.1, 0.2, 0.3, 0.4, 0.6, 1.0, 2.0, 3.02, 4.0, 5.0, 6.99, 9.0]
LaserY = [0.04, 0.02, 0.03, 0.02, 0.02, 0.03, 0.03, 0.05, 0.03, 0.02, 0.02, 0.03]
SolutionY = [0.04, 0.02, 0.02, 0.01, 0.02, 0.03, 0.03, 0.02, 0.01, 0.01, 0.01, 0.01]

LaserCoef = np.polyfit(x,LaserY,1)
LaserPoly1d_fn = np.poly1d(LaserCoef)

SolutionCoef = np.polyfit(x,SolutionY,e)
SolutionPoly1d_fn = np.poly1d(SolutionCoef)

plt.figure(figsize=(10,5), dpi=100)
plt.scatter(x,LaserY, s=25, marker="o", label="Baseline Laser Voltage")
plt.scatter(x,SolutionY, s=25, marker="o", color='r', label="Solution Voltage")
plt.xlabel("Solution Density [g/L]")
plt.ylabel("Voltage [V]")
plt.title("Voltage vs. Solution Density")

plt.plot(x,LaserPoly1d_fn(x), '--b', label="y = -0.00016646x + 0.02878568")
plt.plot(x,SolutionPoly1d_fn(x),'--r', label="y = -0.002007x + 0.02462069")

plt.xlim(left=0,right=9)
plt.ylim(bottom=0,top=0.06)

plt.xticks(np.arange(0,9,0.5))

plt.legend()
plt.show()
