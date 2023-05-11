# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:34:26 2019

@author: Mcrye
"""

from pylab import *

x = cumsum(2 * (randint(1, 7, 1000) <=3) -1)
#plot(x)
#show()
y = 2*(randint(1, 7, 1000) <=3) - 1
##### ok...there are 6 integers to choose from.
#####half are >3 half are <3. This essentially gives an array of + or - 1. 
#####Left vs Right step/walk
#print(y)
z = cumsum(y)
print(z)
#print(x)

plot(z)
show()