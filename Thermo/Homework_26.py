'''
Created on Apr 8, 2022

@author: Mcrye
'''
import numpy as np
import matplotlib.pyplot as plt
import Processes as th

plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()
fig.set_size_inches(12, 6)
fig.suptitle('Thermo Homework 26')

th.linear_heating([0.2, 0.4], [3.0E5, 3.5E5], 7, 1.64)

th.isochoric_heating([0.4, 0.4], [3.5E5, 1.5E5], 7)

th.isobaric_heating([0.4, 0.15],[1.5E5, 1.5E5], 7)

th.linear_heating([0.15, 0.2], [1.5E5, 3.0E5], 7, 1.64)

th.linear_plot(ax, [0.2, 0.4], [3E5, 3.5E5], 'darkred')
th.isochoric_plot(ax, [0.4, 0.4], [3.5E5, 1.5E5], 'darkred')
th.isobaric_plot(ax, [0.4, 0.15], [1.5E5, 1.5E5], 'darkred')
th.linear_plot(ax, [0.15, 0.2], [1.5E5, 3.0E5], 'darkred')

ax.text(0.30, 334500, 'A')
ax.text(0.404, 250000, 'B' )
ax.text(0.30, 142000, 'C')
ax.text(0.17, 225000, 'D')
ax.text(0.195, 305500, 'I')
ax.text(0.404, 350000, 'II')
ax.text(0.404, 145000, 'III')
ax.text(0.145, 155000, 'IV')
plt.show()