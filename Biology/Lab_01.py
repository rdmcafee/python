'''
Created Friday 06/01/23

Author @Mcrye
'''

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

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
plt.show()