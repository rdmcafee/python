"""
Created Wednesday 06/11/23

Author: @Mcrye
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.style.use("Solarize_Light2")

bandSize = [10E3, 8E3, 6E3, 5E3, 4E3, 3E3, 2E3, 1.5E3, 1E3, 0.5E3]
logBand = np.log10(bandSize)

#Pixel distance for ladder
distance = [283.8, 308.8, 341.8, 362.8, 397.8, 453.8, 528.8, 595.8, 678.8, 800.8]

lin_reg = np.polyfit(distance, logBand, 1)
line = stats.linregress(logBand, distance)

x = np.linspace(250, 850, 10000)

def basePairs (dist):
    return dist*lin_reg[0] + lin_reg[1]

print(f'\nLinear Regression: \ny = {round(lin_reg[0], 4)}x + {round(lin_reg[1], 4)}\n')

fig, ax = plt.subplots()

ax.scatter(logBand, distance, color = 'darkblue', alpha = 0.75, s = 6, label = 'Ladder Calibration')
ax.plot(lin_reg[0]*x + lin_reg[1], x, color = 'darkred', alpha = 0.5, linewidth = 2)
ax.set_xlabel('Log(Base Pairs)')
ax.set_ylabel('Distance Traveled (px)')
ax.text(3.4, 700, f'y = {round(lin_reg[0], 4)}*x + {round(lin_reg[1], 4)}', color = 'darkred')
ax.text(3.5, 670, f'R**2 = {round(line.rvalue**2, 4)}', color = 'darkred')
ax.set_title('DNA Ladder Calibration')
#ax.set_xlim(2.28, 3.22)
#ax.set_ylim(200, 600)
SampleData_y = [468.8, 542.8]
SampleData_x = [basePairs(SampleData_y[0]), basePairs(SampleData_y[1])]
ax.scatter(SampleData_x, SampleData_y, color = 'darkgreen', marker = 'x', s = 40, label = 'Sample Data')
plt.tight_layout()
plt.legend()
plt.grid(color = 'k', alpha = 0.1)
plt.show()

'''
Note: There are two peaks: one at 470.8 and the other at 542.8
'''

print(10**(basePairs(468.8)))
print(10**(basePairs(542.8)))