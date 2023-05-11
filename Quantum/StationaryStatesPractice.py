# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:57:01 2021

@author: Mcrye
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = np.linspace(0,10,1000)

y1 = (np.sqrt(2) * np.sin((np.pi * x) / 10))

y2 = (np.sqrt(2) * np.sin((2*x*np.pi) / 10))

y3 = (np.sqrt(2) * np.sin((3*x*np.pi) / 10))
for i in range (0, 10):
    ax.plot(i,(np.sqrt(2) * np.sin((np.pi * i) / 10)))
    plt.pause(0.005)
