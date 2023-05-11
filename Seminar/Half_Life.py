'''
Created on Apr 1, 2022

@author: Mcrye
'''
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')

position_cm = np.linspace(0, 39, 40)
print(position_cm)

measured = [4, 6, 5, 5, 6, 5, 5, 6, 8, 14, 15, 14, 14, 14, 13, 12, 12, 13, 13, 
            12, 12, 12, 12, 12, 13, 13, 14, 16, 13, 16, 15, 16, 15, 15, 15, 15, 
            15, 15, 16, 16]
actual = [5, 5, 5, 5, 5, 5, 20, 20, 20, 20, 20, 20, 20, 13, 13, 13, 13, 13, 13, 
          13, 13, 13, 13, 13, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 
          15, 15, 15]


fig, ax = plt.subplots()
fig.set_size_inches(12, 6)
"""
ax.plot(time_seconds, coin, color = 'darkblue', linewidth = 1)
ax.plot(time_seconds, baseline, color = 'darkred', linewidth = 1)
ax.set_ylabel('Radiation Counts')
ax.set_xlabel('Seconds')
ax.set_title('Radiation Counts VS Seconds')

plt.show()
"""