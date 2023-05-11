# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:02:13 2020

@author: Mcrye
"""

from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

X = [3,-2]

Y = [2,4]

Z = [-4,3]

ax.scatter(X, Y, Z, c = 'r', marker = 'o')


ax.set_xlim(-5,5)
ax.set_xlabel('x axis')
ax.set_ylim(-2,5)
ax.set_ylabel('y axis')
ax.set_zlim(-5,5)
ax.set_zlabel('z axis')

ax.quiver(0,0,0,3,2,-4, length = math.sqrt(3**2 + 2**2 + 4**2), normalize = True)
ax.quiver(0,0,0,-2,4,3, length = math.sqrt(2**2 + 4**2 + 3**2), normalize= True)

ax.quiver(3,2,-4, -5,2,7, length = math.sqrt((3+2)**2 + (2-4)**2 +(-4-3)**2), color='r', normalize = True)
plt.show()