'''
Created on Feb 18, 2022

@author: Mcrye

Using Pandas DataFrames to plot in matplotlib
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import warnings

warnings.filterwarnings('ignore')

plt.style.use('Solarize_Light2')

fig, ax = plt.subplots(2, 2)
fig.set_size_inches(10, 6)

def ax_lims(a = 0, b = 0):
    major_xticks = (np.arange(45, 49, 1))
    minor_xticks = (np.arange(45, 49, 0.25))

    major_yticks = (np.arange(420, 780, 50))
    minor_yticks = (np.arange(420, 780, 25))
    
    ax[a, b].set_xlim(45, 49)
    ax[a, b].set_ylim(420, 780)

    ax[a, b].set_xlabel(r'$\Delta \theta$ $\degree$')
    ax[a, b].set_ylabel(r'$\lambda$ nm')
    ax[a, b].set_title('Wavelength vs Change in Angle')

    ax[a, b].set_xticks(major_xticks)
    ax[a, b].set_xticks(minor_xticks, minor = True)

    ax[a, b].set_yticks(major_yticks)
    ax[a, b].set_yticks(minor_yticks, minor = True)

    ax[a, b].grid(which = 'major', color = 'k', alpha = 0.2)
    ax[a, b].grid(which = 'minor', color = 'k', alpha = 0.05)

    ax[a, b].legend()
    
    return ax[a, b]

file_location = r'C:\Users\Mcrye\workspace\Python\ModernLab\prism_Data.xlsx'

x = np.linspace(45, 49, 1000)

complete_df = pd.read_excel(file_location, 
                       sheet_name = 'Complete_rawData', 
                       names = ['delta theta', 'wavelength'], 
                       engine = 'openpyxl')

print('\nRawData' + str(complete_df))

complete_df.plot.scatter('delta theta', 'wavelength', ax = ax[0,0], 
                         color = 'darkred', s = 8)

polyLine = np.polyfit(complete_df['delta theta'], 
                       complete_df['wavelength'], 2)
def actualLine(e = 0):
    actualLine = polyLine[0]*((x+e)**2) + polyLine[1]*(x+e) + polyLine[2]
    return actualLine

def cauchy(x):
    w = np.sqrt(0.00459/((1/np.sin(x*np.pi/180)) - (1.522)))
    return w

#mean = complete_df['delta theta'].rolling(4).mean()
#sd = complete_df['delta theta'].rolling(2).std()

#print(mean)
#print(sd)

print(polyLine)
equation = (str(round(polyLine[0], 2)) + r'$x^{2}$' +
            str(round(polyLine[1], 2)) + r'x' + 
            str(round(polyLine[2], 2)))
#ax.scatter(mean, complete_df['wavelength'], color = 'darkgreen')
ax[0, 0].plot(x, actualLine(), color = 'darkblue', 
                       linewidth = 1.5, alpha = 0.5, label = equation)

ax[0, 0].fill_between(x, actualLine(e= -0.25), actualLine(e = 0.25), 
                color = 'blue', alpha = 0.2)
new_x = np.linspace(0, 180, 1000)
ax[0, 1].plot(new_x, cauchy(new_x), label = 'Cauchy Formula')

ax_lims(a = 0, b = 0)
#ax_lims(a = 0, b = 1)

max_x = complete_df['delta theta'].max()
min_x = complete_df['delta theta'].min()

max_y = complete_df['wavelength'].max()
min_y = complete_df['wavelength'].min()

print('Theta range:  \n' + str(min_x) + ' -- ' + str(max_x))
print('Wavelength:  \n' + str(min_y) + ' -- ' + str(max_y))


print(polyLine)
print(type(polyLine))

plt.show()
