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

file_location = r'C:\Users\Mcrye\workspace\Python\ModernLab\Calibration_03.xlsx'

helium_Data = pd.read_excel(file_location, 
                       sheet_name = 'Tracker_Calibration_03', 
                       header = 1,
                       usecols = [1, 2], 
                       engine = 'openpyxl')

mercury_Data = pd.read_excel(file_location, 
                       sheet_name = 'Tracker_Calibration_03', 
                       header = 1,
                       usecols = [5, 6], 
                       engine = 'openpyxl')
"""
hydrogen_Data = pd.read_excel(file_location, 
                       sheet_name = 'Tracker_Calibration_2.0', 
                       header = 1,
                       usecols = [3, 4], 
                       engine = 'openpyxl')
"""
print(helium_Data)
print(mercury_Data)
#print(hydrogen_Data)
"""
ax[0] = helium_Data.plot(x = 'x', y = 'luma', xlabel = 'pixel location', 
                      ylabel = 'luma', kind = 'line', linewidth = 1,
                      color = 'darkred')

ax[1] = helium_Data.plot(x = 'x', y = 'luma', xlabel = 'pixel location', 
                      ylabel = 'luma', kind = 'line', linewidth = 1,
                      color = 'darkblue')
"""
ax.plot(helium_Data['wavelength'], helium_Data['luma'],
           linewidth = 1, color = 'darkred')
ax.set_title('Helium Spectra')
ax.set_xlabel('Wavelength')
ax.set_ylabel('Luma')
ax.set_xlim(330, 800)
"""
ax[1].plot(hydrogen_Data['x.1'], hydrogen_Data['luma.1'],
           linewidth = 1, color = 'darkblue')
ax[1].set_title('Hydrogen Spectra')
ax[1].set_xlabel('Pixel Location')
ax[1].set_ylabel('Luma')
"""
#He_Spectra = [402.61914, 412.08154, 447.14802, 471.31457, 501.56783, 
#              587.56210, 667.81510]
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
plt.show()

fig, ax = plt.subplots()
fig.set_size_inches(12, 6)

ax.plot(mercury_Data['wavelength.1'], mercury_Data['luma.1'],
           linewidth = 1, color = 'darkred')
ax.set_title('Mercury Spectra')
ax.set_xlabel('Wavelength')
ax.set_ylabel('Luma')

Hg_Spectra = [398.3931, 407.7837, 435.83363, 546.07498, 576.96095]
ax.axvline(Hg_Spectra[0], color = 'darkblue', linewidth = 1, 
           label = str(Hg_Spectra[0]))
ax.axvline(Hg_Spectra[1], color = 'darkblue', linewidth = 1, 
           label = str(Hg_Spectra[1]))
ax.axvline(Hg_Spectra[2], color = 'darkblue', linewidth = 1, 
           label = str(Hg_Spectra[2]))

ax.axvline(Hg_Spectra[3], color = 'darkblue', linewidth = 1, 
           label = str(Hg_Spectra[3]))
ax.axvline(Hg_Spectra[4], color = 'darkblue', linewidth = 1, 
           label = str(Hg_Spectra[4]))
ax.legend(title = 'Expected Wavelengths (nm)', framealpha = 0.5, 
          loc = 'upper right')
plt.show()