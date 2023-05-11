# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 21:25:34 2022

@author: Mcrye
"""

from sympy import *
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

points_x = [0.06, 0.18, 0.06, 0.18, 0.06, 0.06]
points_y = [2, 4, 4, 2, 12, 18.6]

fig, ax = plt.subplots()
fig.set_size_inches(8,5)

ax.scatter((points_x), (points_y), alpha = 0.2)

ad_Bounds = np.linspace(0.06, 0.18, 10)
ad_Equation = 2*(ad_Bounds/ad_Bounds)
ax.plot(ad_Bounds, ad_Equation)
ax.plot((0.06, 0.06), (2,18.6))
ax.plot((0.06, 0.18), (4, 4))
ax.plot((0.18, 0.18), (2, 4))

ab_Bounds = np.linspace(0.06, 0.18, 10)
ab_Equation = (2/(0.18-0.06))*ab_Bounds + 1
ax.plot(ab_Bounds, ab_Equation)

ab_intercept = 4 - (2/(0.18-0.06))*0.18
print('A-B (linear process) y-intercept = ' + str(ab_intercept))

eb_Bounds = np.linspace(0.06, 0.18, 100)
eb_Equation = (12*0.06)/eb_Bounds
ax.plot(eb_Bounds, eb_Equation)

fb_Bounds = np.linspace(0.06, 0.18, 100)
fb_Equation = ((0.18**(7/5)*4)/(fb_Bounds**(7/5)))
ax.plot(fb_Bounds, fb_Equation)
ax.grid(True, alpha = 0.1)

P, V = sp.symbols('P V')
adiabatic = ((0.18**(7/5)*4)/(V**(7/5)))
adiabatic_work = round(-1*integrate(adiabatic, (V, 0.06, 0.18)), 6)
work_alternate =round( ( ( (0.18*4) - (0.06*18.6) ) * (5/2) ), 6)
print('Adiabatic Process' + '\n' + 'Adiabatic Work: ' + str(adiabatic_work))
print('Adiabatic Work another way...: ' + str(work_alternate))
#display(Integral(adiabatic, (V, 0.06, 0.18)))


isothermal = (12*0.06)/V
#display(Integral(isothermal, (V, 0.06, 0.18)))
isothermal_work = round(integrate(isothermal, (V, 0.06, 0.18)), 6)
print('Isothermal Process' + '\n' + 'Isothermal Work: ' + str(isothermal_work))

plt.show()