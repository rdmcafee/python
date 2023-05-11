'''
Created on Apr 11, 2022

@author: Mcrye
'''
import numpy as np
import matplotlib.pyplot as plt

import Processes as th

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

fig.set_size_inches(12, 6)
fig.suptitle('Thermo Homework 27')

n = 1           ##mole
dof = 5         ##diatomic
gamma = 1.4     ##adiabatic exponent
R = 8.314       ##gas constant

adiabatic_A_volume = n*R*400/1E5
k_A = 1E5*(adiabatic_A_volume)**1.4

adiabatic_B_volume = n*R*600/25E5
k_B = 25E5*(adiabatic_B_volume)**1.4

isothermal_range_A = np.linspace(1.99536E-3, 12.06E-3, 1000)
isothermal_range_B = np.linspace(5.499E-3, 33.256E-3, 1000)
isothermal_A = (n*R*600)/isothermal_range_A
isothermal_B = (n*R*400)/isothermal_range_B

adiabatic_range_A = np.linspace(12.06E-3, 33.256E-3, 1000)
adiabatic_range_B = np.linspace(1.99536E-3, 5.499E-3, 1000)
adiabatic_A = k_A/(adiabatic_range_A**1.4)
adiabatic_B = k_B/(adiabatic_range_B**1.4)

intercept_x = [1.99536E-3, 33.256E-3, 5.499E-3, 1.206E-2]
intercept_y = [(n*R*600)/1.99536E-3, (n*R*400)/33.256E-3, 
               (4.14925E2/(5.499E-3)**1.4), (8.52135E2/(1.206E-2)**1.4)]

ax.plot(isothermal_range_A, isothermal_A, linewidth = 1, color = 'darkred')
ax.plot(isothermal_range_B, isothermal_B, linewidth = 1, color = 'darkred')

ax.plot(adiabatic_range_A, adiabatic_A, linewidth = 1, color = 'darkblue')
ax.plot(adiabatic_range_B, adiabatic_B, linewidth = 1, color = 'darkblue')

ax.scatter(intercept_x, intercept_y, s = 5, color = 'darkblue')

ax.set_ylim(0, 30E5)
ax.set_xlim(0, 35.0E-3)

ax.set_ylabel('Pa')
ax.set_xlabel(r'$m^3$')

ax.text(2E-3, 2.5E6, 'I')
ax.text(1.2E-2, 4.5E5, 'II')
ax.text(3.3E-2, 1.4E5, 'III')
ax.text(4.6E-3, 5.8E5, 'IV')

ax.text(5.4E-3, 1.0E6, 'A')
ax.text(2E-2, 2.5E5, 'B')
ax.text(1E-2, 1.67E5, 'C')
ax.text(1.9E-3, 1.5E6, 'D')

plt.show()
