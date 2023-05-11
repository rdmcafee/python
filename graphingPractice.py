# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 00:03:23 2019

@author: Mcrye
"""

from pylab import *
m = array([1.0, 2.0, 4.0, 6.0, 9.0, 11.0])
v = array([0.131, 0.261, 0.501, 0.771, 1.151, 1.361])

plot(m,v,'o')
xlabel('m (kg)')
ylabel('V (L)')