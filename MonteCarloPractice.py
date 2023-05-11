# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 01:05:43 2022

@author: Mcrye
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats as scp
import warnings

warnings.filterwarnings('ignore')
plt.style.use('Solarize_Light2')
fig, axs = plt.subplots(1, 2)
fig.set_size_inches(10,5)

n = 100  # How many iterations
nn = 1000
#area = np.zeros((n+1,n+1), dtype='float')


def random(minimum, maximum):
    a = round(np.random.uniform(minimum, maximum), 2)
    return a


j = 0

areas = []

while j < n:

    pointsIn = 0
    pointsOut = 0
    i = 0

    while i < nn:
        x = random(-1, 1)
        y = random(-1, 1)
        #print("now in i loop, iteration:" + str(i))

        if np.sqrt((x**2)+(y**2)) <= 1:
            axs[0].scatter(x, y, c='b', s=5)
            pointsIn += 1
        else:
            axs[0].scatter(x, y, c='r', s=5)
            pointsOut += 1

        try:
            sampleArea = round(((pointsIn*4)/(pointsOut+pointsIn)), 6)
            #print(sampleArea)

        except ZeroDivisionError:
            print("Div by Zero Foo")

        axs[0].set_xlim([-1, 1])
        axs[0].set_ylim([-1, 1])
        #plt.draw()
        #plt.pause(0.01)

        i += 1

    areas.append(sampleArea)
    #print(j)
    j += 1

print(areas[:])

mean = round(np.mean(areas), 4)
sd = round(np.std(areas), 2)
x_min = 0
x_max = 6

x = np.linspace(x_min, x_max, 1000)
y = scp.norm.pdf(x, mean, sd)

print("mean = "+ str(mean))
print("SD = " + str(sd))

axs[1].hist(areas, bins=10, density=True, histtype='bar', stacked=False)
axs[1].set_xlim([0, 6])
axs[1].plot(x,y)



plt.show()

input("Press Enter to Continue...")
