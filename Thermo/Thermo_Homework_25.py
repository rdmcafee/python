'''
Created on Apr 5, 2022

@author: Mcrye
'''

import matplotlib.pyplot as plt
import numpy as np
import Processes as th

plt.style.use('Solarize_Light2')

V = [2, 4]
P = [3, 1.5]

major_xticks = np.arange(0, 10, 1)
minor_xticks = np.arange(0,10, 0.25)

major_yticks = np.arange(0,6, 1)
minor_yticks = np.arange(0,6, 0.5)

fig, ax = plt.subplots()
fig.set_size_inches(12, 6)
fig.suptitle('Thermo 418: Homework 25')

ax.set_xticks(major_xticks)
ax.set_xticks(minor_xticks, minor = True)

ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor = True)

ax.grid(which = 'minor', color = 'k', alpha = 0.05)
ax.grid(which = 'major', color = 'k', alpha = 0.1)

ax.set_xlim(0, 6)
ax.set_ylim(0, 5)

ax.scatter(V, P, color = 'darkred', s = 10)

ax.text(1.9, 3.1, 'K')
ax.text(4.05, 1.55, 'Y')

ax.text(3, 3.1, r'$B_2$')
ax.text(4.1, 2.2, r'$B_1$')

ax.text(1.85, 2.2, r'$A_2$')
ax.text(3, 1.25, r'$A_1$')

ax.text(3.05, 2, 'Isotherm')
ax.text(3.55, 1.2, 'Adiabat')

ax.set_xlabel(r'$V(m^3)$')
ax.set_ylabel(r'$P(\frac{N}{m^2})$')

th.isobaric_plot(ax, [4, 2], [1.5, 1.5], 'darkblue')
th.isochoric_plot(ax, [2, 2], [1.5, 3], 'darkblue')

th.adiabatic_plot(ax, [2, 4], [3, 1.5], dof = 3, clr = 'darkorange')


th.isothermal_plot(ax, [2, 4], [3], 'darkgreen')


th.isochoric_plot(ax, [4, 4], [1.5, 3], 'darkred')
th.isobaric_plot(ax, [4, 2], [3, 3], 'darkred')
plt.show()

print('isobaric followed by isochoric, (Y to K) \n')

ProcessA_1 = th.isobaric_heating([4, 2], [1.5, 1.5])
ProcessA_2 = th.isochoric_heating([2, 2], [1.5, 3])

print('\nTotal Heating')
totalA = ProcessA_1 + ProcessA_2

print(str(totalA) + ' Joules')

print('\nNow for isochoric followed by isobaric (Y to K) \n')

ProcessB_1 = th.isochoric_heating([4, 4], [1.5, 3])
ProcessB_2 = th.isobaric_heating([4, 2], [3, 3])

print('\nTotal Heating')
totalB = ProcessB_1 + ProcessB_2

print(str(totalB) + ' Joules')

print('\nIsothermal Heating: ')

isothermalHeating = th.isothermal_heating([4, 2], [1.5, 3], 3, 5)
print(isothermalHeating)