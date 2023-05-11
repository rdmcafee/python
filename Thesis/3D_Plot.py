'''
Created on May 3, 2023

@author: Mcrye
'''

'''
this maple import was found in various examples, but doesn't appear to be 
necessary here
'''

#from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import matplotlib.pyplot as plt

class sphere():
    
    def __init__(self, center, r):
        self.center, self.r = center, r
        
        self.Setup()
        
    def Setup(self):
            
        '''
            Must take in array representing the position and length of
            radius, 'r' and convert to spherical equation
            center[0] = x; center[1] = y; center[2] = z
        '''
        self.theta = np.linspace(0, 2*np.pi, 100)
        self.rho = np.linspace(-np.pi, np.pi, 100)
            
        self.T, self.P = np.meshgrid(self.theta, self.rho)
            
        self.X = self.r*np.cos(self.T)*np.sin(self.P) + self.center[0]
        self.Y = self.r*np.sin(self.T)*np.sin(self.P) + self.center[1]
        
        self.Z = self.r*np.cos(self.P) + self.center[2]
        
''' Create sphere objects from the sphere class'''
           
sphere_1 = sphere([0, 0, 0], 2)
sphere_2 = sphere([2, 2, 2], 1)
sphere_3 = sphere([5, 5, 5], 3)
sphere_4 = sphere([5, 5, -5], 5)
sphere_5 = sphere([-5, 5, 10], 3)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

'''surface plot the sphere objects'''

ax.plot_surface(sphere_1.X,sphere_1.Y, sphere_1.Z, color = 'darkred', alpha = 0.5)
ax.plot_surface(sphere_2.X, sphere_2.Y, sphere_2.Z, color = 'darkblue', alpha = 0.5)
ax.plot_surface(sphere_3.X, sphere_3.Y, sphere_3.Z, color = 'darkgreen', alpha = 0.5)
ax.plot_surface(sphere_4.X, sphere_4.Y, sphere_4.Z, color = 'darkblue', alpha = 0.5)
ax.plot_surface(sphere_5.X, sphere_5.Y, sphere_5.Z, color = 'darkred', alpha = 0.5)
'''keep limits equal for 1:1 aspect ratio'''

ax.set_zlim(-10, 15)
ax.set_xlim(-10, 15)
ax.set_ylim(-10, 15)

plt.tight_layout()
plt.show()

            