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
linReg_String = f'y = {round(linReg[0], 2)}*x^2 + {round(linReg[1], 2)}*x + {round(linReg[2], 2)}'

fig, ax = plt.subplots()
ax.scatter(sucrose_sol, percent_F, s = 5, color = 'darkblue')
ax.plot(sucrose_sol, percent_F, color = 'darkblue', linewidth = 2, alpha = 0.1, label = 'Collected Data')
ax.plot(x, ((linReg[0])*x**2) + (linReg[1]*x) + (linReg[2]), color = 'darkred', alpha = 0.5, label = '2nd Order Regression')
ax.axvline(8.42, 0, 100, color = 'darkgreen', linewidth = 1, alpha = 0.5)
ax.axhline(50, 0, 20, color = 'darkgreen', linewidth = 1, alpha = 0.5)
ax.text(8.5, 50.5, '8.4218%', fontsize = 'small', color = 'darkgreen' )
ax.text(9.75, 70, linReg_String, color = 'darkred', weight = 'bold' )
ax.grid(color = 'k', alpha = 0.05)
ax.set_xlabel(r'% Sucrose Solution')
ax.set_ylabel(r'% Larva Floating')
ax.set_title(r'% Floating Larva vs Sucrose Solution Concentration', fontsize = 12)
plt.legend()
plt.tight_layout()
plt.show()

'''
Ok so we have a curve representing the data; we can use this curve to estimate at what sucrose concentration
50% of the larva would float.
'''
target_float = 50
solution = solve((linReg[0]*z**2)+(linReg[1]*z)+(linReg[2]) - 50, z, dict = True)
print(f'{solution}')

print(linReg)

'''
Create a new plot of the DGRP strain studied by each student and the percent sucrose solution where 50% larva float
'''

DGRP = np.array([358, 555, 705, 786, 517, 21, 732, 208, 730])
FC50 = np.array([10.8, 10, 8.8, 8.8, 11.3, 8.42, 12.9, 8.8, 10.6])

cleanPlot_DGRP = np.array([358, 555, 705, 786, 517, 21, 208])
fig, ax = plt.subplots()
fig.set_size_inches(8, 5)

ax.scatter(DGRP, FC50, c = 'darkblue', s = 20, marker = "x")
ax.set_yticks(FC50)
ax.set_xticks(cleanPlot_DGRP)
ax.set_xlabel('DGRP Strain [RAL#]', weight = 'bold')
ax.set_ylabel('FC50 \n [% sucrose]', weight = 'bold')
ax.set_title('Class Data [DGRP vs FC50]', fontsize = 12)
ax.grid(color = 'k', alpha = 0.10)
#for _x in DGRP: ax.axvline(_x, color = 'darkgreen', linewidth = 1, alpha = 0.25) 
plt.tight_layout()
plt.show()