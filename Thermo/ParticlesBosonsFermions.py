'''
Created on Apr 4, 2022

@author: Mcrye
'''

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('Solarize_Light2')

x = np.linspace(-4, 4, 1000)
xx = np.linspace(0.00001, 4, 1000)

q = 0

boltzman = 1/np.exp(x + q)

bose = 1/(np.exp(xx + q) - 1)

fermi = 1/(np.exp(x + q) + 1)

fig, ax = plt.subplots()

ax.plot(x, boltzman, color = 'darkred', linewidth = 1, label = 'Maxwell-Boltzman')
ax.plot(x, fermi, color = 'darkblue', linewidth = 1, label = 'Fermi-Dirac')
ax.plot(xx, bose, color = 'darkorange', linewidth = 1, label = 'Bose-Einstein')

ax.legend()

ax.set_ylim(-0.2, 2)
ax.set_xlim(-1, 3)

ax.axvline(0, color = 'k', linewidth = 0.5)
ax.axhline(0, color = 'k', linewidth = 0.5)

ax.set_ylabel(r'$\overline{N}$')
ax.set_xlabel('Energy (*hf)')
fig.suptitle('Thermo Exam03 \nQuestion 01.d')
plt.show()