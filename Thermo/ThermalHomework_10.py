# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 17:38:54 2022

@author: Mcrye
"""

import matplotlib.pyplot as plt 
import scipy.integrate as scp
import numpy as np


x_vals = [0.5, 4.0, 4.5, 1.5, 0.5]
y_vals = [3.0, 3.5, 1.5, 1.5, 3.0]

fig, ax = plt.subplots()
fig.set_size_inches(18,8)
fig.suptitle("Homework 10: Thermal Cycles", fontsize = 20)
#ax.plot(x_vals, y_vals)

process_a = np.linspace(0.5, 4.0, 10)
a = (process_a/7) + (41/14)
work_a = scp.simps(a, process_a)

process_b = np.linspace(4.0, 4.5, 10)
b = (-4*process_b) + (39/2)
work_b = scp.simps(b, process_b)

process_c = np.linspace(1.5, 4.5, 10)
c = 1.5*(process_c/process_c)
work_c = scp.simps(c, process_c)


process_d = np.linspace(0.5, 1.5, 10)
d = -(3*process_d/2) + (15/4)
ad = (process_d/7) + (41/14)
work_d = scp.simps(d, process_d)

work_total = work_a + work_b - work_c - work_d

ax.plot(process_a, a, color = 'r', alpha = 0.4)
ax.plot(process_b, b, color = 'r', alpha = 0.4)
ax.plot(process_c, c, color = 'r', alpha = 0.4)
ax.plot(process_d, d, color = 'r', alpha = 0.4)

ax.plot(x_vals, y_vals, linestyle = (0, (5, 10)) , color = 'b')

ac = np.linspace(1.5, 4.0, 10)
new_a = (ac/7) + (41/14)
new_c = 1.5*(ac/ac)

ab = np.linspace(4, 4.5, 10)
new_cc = 1.5*(ab/ab)
new_b = (-4*ab) + (39/2)

ax.fill_between(process_d, ad,d, color = 'g', alpha = 0.1)
ax.fill_between(ac, new_a, new_c, color = 'g', alpha = 0.1)
ax.fill_between(ab, new_cc, new_b, color = 'g', alpha = 0.1)

major_xticks = np.arange(0, 7, 1)
minor_xticks = np.arange(0,7, 0.25)

major_yticks = np.arange(0,6, 1)
minor_yticks = np.arange(0,6, 0.5)

ax.set_xticks(major_xticks)
ax.set_xticks(minor_xticks, minor = True)
ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor = True)

ax.set_ylim(0, 5)
ax.set_xlim(0, 6)
ax.set_xlabel("Volume")
ax.set_ylabel("Pressure")

ax.grid(which = 'minor', alpha = 0.2)
ax.grid(which = 'major', alpha = 0.5)

total_work = str('Total Work: ' + str(round(work_total, 2)) 
           + " " + r'$\mathrm{ V_{0}P_{0}}$'
           + "\n Work_A: " + str(round(work_a, 2)) + " " + r'$\mathrm{ V_{0}P_{0}}$'
           + "\n Work_B: " + str(round(work_b, 2)) + " " + r'$\mathrm{ V_{0}P_{0}}$'
           + "\n Work_C: -" + str(round(work_c, 2)) + " " + r'$\mathrm{V_{0}P_{0}}$'
           + "\n Work_D: -" + str(round(work_d, 2)) + " " + r'$\mathrm{V_{0}P_{0}}$')


prop = dict(boxstyle = 'round', facecolor = 'wheat', alpha = 0.5)

ax.text(0.05, 0.95, total_work, transform=ax.transAxes, fontsize=12, 
        verticalalignment='top', bbox=prop)



plt.show()
