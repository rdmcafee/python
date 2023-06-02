'''
Created Friday 06/01/23

Author @Mcrye
'''

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sympy.solvers import solve
from sympy import Symbol
z = Symbol('z')
'''
create an array of data representing the density of the larva in sucrose solution -- % floating larva is independent variable
'''
plt.style.use('Solarize_Light2')
Ral = 21, 
total_larva = 58, 

floaters = np.array([37, 37, 50, 52, 53, 54, 55, 56])
percent_F = (floaters/total_larva)*100

sucrose_sol = np.array([8.8, 9.3, 9.8, 10.2, 10.6, 11.0, 11.3, 11.6])
x = np.linspace(8, 12, 100)
print(percent_F)

linReg = np.polyfit(sucrose_sol, percent_F, 2)
print(linReg[2])
fig, ax = plt.subplots()
ax.plot(sucrose_sol, percent_F)
ax.plot(x, ((linReg[0])*x**2) + (linReg[1]*x) + (linReg[2]), color = 'darkred', alpha = 0.5)
ax.axvline(8.42, 0, 100, color = 'darkgreen', linewidth = 1, alpha = 0.5)
ax.axhline(50, 0, 20, color = 'darkgreen', linewidth = 1, alpha = 0.5)
ax.text(8.5, 50.5, '8.4218%', fontsize = 'small', color = 'darkgreen' )
ax.grid(color = 'k', alpha = 0.05)
ax.set_xlabel(r'% Sucrose Solution')
ax.set_ylabel(r'% Larva Floating')
ax.set_title(r'% Floating Larva vs Sucrose Solution Concentration', fontsize = 12)
plt.show()

'''
Ok so we have a curve representing the data; we can use this curve to estimate at what sucrose concentration
50% of the larva would float.
'''
target_float = 50
solution = solve((linReg[0]*z**2)+(linReg[1]*z)+(linReg[2]) - 50, z, dict = True)
print(f'{solution}')