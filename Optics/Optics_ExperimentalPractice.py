# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 00:12:36 2021

@author: Mcrye
"""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import pandas as pd
import numpy as np

plt.style.use('Solarize_Light2')

fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax1 = fig.add_axes([0,800,0,200])

Solarintensity = pd.read_excel(r'C:\Users\Mcrye\Documents\Personal\School\Fall_2021\Optics\Experimental Project\FinalDesign\FinalAnalysis.xlsx' , 
                               sheet_name = 'SolarIrradiance', engine = 'openpyxl')

wavelength = pd.read_excel(r'C:\Users\Mcrye\Documents\Personal\School\Fall_2021\Optics\Experimental Project\FinalDesign\FinalAnalysis.xlsx', 
                           sheet_name = 'SolarWavelength', engine = 'openpyxl')

IncandescentWavelength = pd.read_excel(r'C:\Users\Mcrye\Documents\Personal\School\Fall_2021\Optics\Experimental Project\FinalDesign\FinalAnalysis.xlsx' , 
                                       sheet_name = 'IncandescentWavelength', engine = 'openpyxl')

print(Solarintensity)
print(wavelength)
cF = 0.0

ax1.plot(wavelength, Solarintensity)
plt.xlim(375, 700)
plt.ylim(-5,160)
plt.title("Solar Intensity vs " + '$\lambda$')
plt.xlabel('Wavelength ' + '$\lambda$')
plt.ylabel('Intensity')
plt.grid(True)

plt.axvline(687.7-cF, c='r', linewidth = 1)
plt.axvline(656.3-cF, c='r', linewidth = 1)
plt.axvline(589.0-cF, c='r', linewidth = 1)
plt.axvline(526.96-cF, c='r', linewidth = 1)
plt.axvline(517.3-cF, c='r', linewidth = 0.8)
plt.axvline(518.4-cF, c='r', linewidth = 0.8)
plt.axvline(486.1-cF, c='r', linewidth = 1)
plt.axvline(427.18-cF, c='r', linewidth = 1)



plt.show()
