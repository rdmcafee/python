'''
Created on Mar 18, 2022

@author: Mcrye
'''
import matplotlib.pyplot as plt
import matplotlib.table as tb
import numpy as np
import pandas as pd

plt.style.use('Solarize_Light2')
#fig, ax = plt.subplots(1, 2, sharey = True, sharex = True)
fig, ax = plt.subplots()
fig.set_size_inches(12, 6)

file_location = r'C:\Users\Mcrye\workspace\Python\ModernLab\Calibration_04.xlsx'

helium_Data = pd.read_excel(file_location, 
                       sheet_name = 'Tracker_Calibration_04', 
                       header = 1,
                       usecols = [1, 2], 
                       engine = 'openpyxl')

#print(helium_Data)

ax.plot(helium_Data['wavelength'], helium_Data['luma'],
           linewidth = 1, color = 'darkred')
ax.set_title('Helium Spectra')
ax.set_xlabel('Wavelength')
ax.set_ylabel('Luma')
ax.set_xlim(357, 727)

"""
He_Spectra = [706.5190, 587.5621, 388.8648, 402.61914, 501.56210, 
              471.31457, 447.14802]
ax.axvline(He_Spectra[0], color = 'darkblue', linewidth = 1, 
           label = str(He_Spectra[0]))
ax.axvline(He_Spectra[1], color = 'darkblue', linewidth = 1, 
           label = str(He_Spectra[1]))
ax.axvline(He_Spectra[2], color = 'darkblue', linewidth = 1, 
           label = str(He_Spectra[2]))

ax.axvline(He_Spectra[3], color = 'darkblue', linewidth = 1, 
           label = str(He_Spectra[3]))
ax.axvline(He_Spectra[4], color = 'darkblue', linewidth = 1, 
           label = str(He_Spectra[4]))
ax.axvline(He_Spectra[5], color = 'darkblue', linewidth = 1, 
           label = str(He_Spectra[5]))
ax.axvline(He_Spectra[6], color = 'darkblue', linewidth = 1, 
           label = str(He_Spectra[6]))
ax.legend(title = 'Expected Wavelengths (nm)', 
          framealpha = 0.5, loc = 'upper right')
          
"""
plt.show()