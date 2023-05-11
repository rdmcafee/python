'''
Created on Mar 18, 2022

@author: Mcrye
'''
import matplotlib.pyplot as plt
import matplotlib.table as tb
import numpy as np
import pandas as pd

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots(1, 2, sharey = True, sharex = True)
fig.set_size_inches(12, 6)

file_location = r'C:\Users\Mcrye\workspace\Python\ModernLab\Calibration_02.xlsx'

helium_Data = pd.read_excel(file_location, 
                       sheet_name = 'Tracker_Calibration_2.0', 
                       header = 1,
                       usecols = [0, 1], 
                       engine = 'openpyxl')

hydrogen_Data = pd.read_excel(file_location, 
                       sheet_name = 'Tracker_Calibration_2.0', 
                       header = 1,
                       usecols = [3, 4], 
                       engine = 'openpyxl')

print(helium_Data)
print(hydrogen_Data)
"""
ax[0] = helium_Data.plot(x = 'x', y = 'luma', xlabel = 'pixel location', 
                      ylabel = 'luma', kind = 'line', linewidth = 1,
                      color = 'darkred')

ax[1] = helium_Data.plot(x = 'x', y = 'luma', xlabel = 'pixel location', 
                      ylabel = 'luma', kind = 'line', linewidth = 1,
                      color = 'darkblue')
"""
ax[0].plot(helium_Data['x'], helium_Data['luma'],
           linewidth = 1, color = 'darkred')
ax[0].set_title('Helium Spectra')
ax[0].set_xlabel('Pixel Location')
ax[0].set_ylabel('Luma')

ax[1].plot(hydrogen_Data['x.1'], hydrogen_Data['luma.1'],
           linewidth = 1, color = 'darkblue')
ax[1].set_title('Hydrogen Spectra')
ax[1].set_xlabel('Pixel Location')
ax[1].set_ylabel('Luma')

plt.show()

#fig, ax = plt.subplots()
#plt.axis('off')

#table = plt.table(helium_Data.values, loc = 0, colLabels = helium_Data.columns)


#plt.show()