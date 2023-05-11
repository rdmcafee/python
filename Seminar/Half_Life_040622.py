'''
Created on Apr 1, 2022

@author: Mcrye
'''
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')

time_seconds = np.linspace(0, 22*10, 22)
baseline = [7, 3, 3, 3, 3, 6, 0, 1, 1, 3, 4, 4, 0, 0, 0, 5, 2, 2, 3, 5, 2, 3]
coin =     [1, 5, 3, 1, 1, 6, 5, 1, 3, 4, 4, 6, 2, 5, 5, 1, 4, 1, 1, 6, 5, 3]

fig, ax = plt.subplots()
fig.set_size_inches(12, 6)

ax.plot(time_seconds, coin, color = 'darkblue', linewidth = 1, label = 'coins')
ax.plot(time_seconds, baseline, color = 'darkred', linewidth = 1, label = 'baseline')
ax.set_ylabel('Radiation Counts')
ax.set_xlabel('Seconds')
ax.set_title('Radiation Counts VS Seconds')

ax.legend()

plt.show()