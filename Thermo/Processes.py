'''
Created on Feb 15, 2022

@author: Mcrye
'''

import numpy as np
#import scipy as sc
from scipy import integrate
import matplotlib.pyplot as plt

plt.style.use('Solarize_Light2')

R = 8.314                       #Joules/mol*K

def isochoric_heating(xvals = [1, 1], yvals = [1, 4], dof = 3):
    #heating = round((dof/2)*(xvals[0]*(yvals[1]-yvals[0])), 4)
    process = (dof/2)*((xvals[0]*yvals[1])-(xvals[0]*yvals[0]))
    """
    heating = np.format_float_scientific(process, 
                                         precision = 10, min_digits = 4)
    """
    heating = round((process), 2)
    print('Energy exchanged via isochoric heating: ' + str(heating) + ' Joules')
    return heating

def isochoric_working(xvals = [1, 1], yvals = [1, 4]):
    working = 0.0
    
    print('Energy exchanged via isochoric working: ' + str(working) + ' Joules')
    return working

def isochoric_plot(ax, xvals = [1,1], yvals = [1,4], clr = 'darkred'):
    ax.plot(xvals, yvals, linewidth = 1, color = clr, alpha = 0.5)
    
    ax.scatter(xvals, yvals, c = 'darkblue', s = 1.5)
    
    ax.set_xlabel(r'Volume: $m^{3}$', labelpad = -5, fontsize = 10, 
                  fontweight = 'bold')
    ax.set_ylabel(r'Pressure: $\frac{N}{m^{2}}$', labelpad = 0, fontsize = 10, 
                  fontweight = 'bold')

def isobaric_heating(xvals = [1, 5], yvals = [1, 1], dof = 3):
    heating = round(((dof/2)+1)*yvals[0]*(xvals[1]-xvals[0]), 2)
    
    print('Energy exchanged via isobaric heating: ' + str(heating) + ' Joules')
    return heating

def isobaric_working(xvals = [1, 5], yvals = [1, 1]):
    #Note: (-1) = work done ON the gas
    bounds = np.linspace(np.min(xvals), np.max(xvals), 1000)
    if xvals[1]>xvals[0]:
        working = round(-1*integrate.simps(yvals[0]*bounds/bounds,bounds), 2)
    else:
        working = round(1*integrate.simps(yvals[0]*bounds/bounds,bounds), 2)
    
    print('Energy exchanged via isobaric working: ' + str(working) + ' Joules')
    return working

def isobaric_plot(ax, xvals = [1, 5], yvals = [1, 1], clr = 'darkred'):
    ax.plot(xvals, yvals, linewidth = 1, color = clr, alpha = 0.5)
    
    ax.scatter(xvals, yvals, c = 'darkblue', s = 1.5)
    
    ax.set_xlabel(r'Volume: $m^{3}$', labelpad = -5, fontsize = 10, 
                  fontweight = 'bold')
    ax.set_ylabel(r'Pressure: $\frac{N}{m^{2}}$', labelpad = 0, fontsize = 10, 
                  fontweight = 'bold')

def isothermal_working(xvals = [1, 1], yvals = [1]):
    #Note: (-1) = work done ON the gas
    bounds = np.linspace(np.min(xvals), np.max(xvals), 1000)
    x = xvals
    y = yvals
    y[1] = (xvals[0]*yvals[0]/xvals[1])
    if xvals[1]>xvals[0]:
        process = -1*(xvals[0]*yvals[0])/bounds
    else:
        process = (xvals[0]*yvals[0])/bounds
    #working = round(-1*(xvals[0]*yvals[0]*np.log(xvals[1]/xvals[0])), 4)
    working = round(integrate.simps(process, bounds), 2)
    
    print('Energy exchanged via isothermal working: ' + 
          str(working) + ' Joules')
    print('Final pressure: ' + str(y[1]))
    return working

def isothermal_heating(xvals = [1, 1], yvals = [1], dof = 3, n = 1):
    internal_Energy = dU(xvals, yvals, dof, n)
    working = isothermal_working(xvals, yvals)
    heating = internal_Energy - working
    
    print('Energy exchanged via isothermal heating: ' + 
          str(heating) + ' Joules')
    return heating

def isothermal_plot(ax, xvals = [1, 1], yvals = [1], clr = 'darkred'):
    bounds = np.linspace(np.min(xvals), np.max(xvals), 1000)
    process = (xvals[0]*yvals[0])/bounds
    
    x = xvals
    y = yvals
    y.append(x[0]*y[0]/x[1])
    
    ax.plot(bounds, process, linewidth = 1, color = clr, alpha = 0.5)
    ax.scatter(x, y, c = 'darkblue', s = 1.5)
    
    ax.set_xlabel(r'Volume: $m^{3}$', labelpad = -5, fontsize = 10, 
                  fontweight = 'bold')
    ax.set_ylabel(r'Pressure: $\frac{N}{m^{2}}$', labelpad = 0, fontsize = 10, 
                  fontweight = 'bold')
    return process

def dU(xvals = [1, 1], yvals = [1, 4], dof = 3, n = 1):
    internal_Energy = round((dof/2)*(xvals[1]*yvals[1]-xvals[0]*yvals[0]),
                             4)
    energy_Initial = round((dof/2)*(xvals[0]*yvals[0]),
                             4)
    energy_Final = round((dof/2)*(xvals[1]*yvals[1]),
                             4)
    
    energy_Proportion = round(energy_Final/energy_Initial, 4)
    
    print('Total internal energy change: ' + str(internal_Energy) + ' Joules')
    print('Proportion of initial energy: ' + str(energy_Proportion) +
          r' * U_initial = U_final.')
    return internal_Energy

def linear_working(xvals = [1, 1], yvals = [1, 4]):
    bounds = np.linspace(np.min(xvals), np.max(xvals), 1000)
    slope = (yvals[1]-yvals[0])/(xvals[1]-xvals[0])
    y_intercept = yvals[0] - xvals[0]*slope
    if xvals[1]>xvals[0]:
        working = round(-1*integrate.simps(slope*bounds + y_intercept, bounds),
                         4)
    else:
        working = round(1*integrate.simps(slope*bounds + y_intercept, bounds),
                         4)
    print('Energy exchanged via linear working: ' + str(working) + ' Joules')
    return working
    
def linear_heating(xvals = [1,1], yvals = [1, 4], dof = 3, n = 1):
    internal_Energy = dU(xvals, yvals, dof, n)
    working = linear_working(xvals, yvals)
    heating = round(internal_Energy - working, 4)
    
    print('Energy exchanged via linear heating: ' + str(heating) + ' Joules')
    return heating

def linear_plot(ax, xvals = [1, 1], yvals = [1, 4], clr = 'darkred'):
    bounds = np.linspace(np.min(xvals), np.max(xvals), 1000)
    slope = (yvals[1]-yvals[0])/(xvals[1]-xvals[0])
    y_intercept = yvals[0] - xvals[0]*slope
    process = slope*bounds + y_intercept
    
    ax.plot(bounds, process, linewidth = 1, color = clr, alpha = 0.5)
    ax.scatter(xvals, yvals, c = 'darkblue', s = 1.5)
    
    ax.set_xlabel(r'Volume: $m^{3}$', labelpad = -5, fontsize = 10, 
                  fontweight = 'bold')
    ax.set_ylabel(r'Pressure: $\frac{N}{m^{2}}$', labelpad = 0, fontsize = 10, 
                  fontweight = 'bold')
    
    return process

def adiabatic_working(xvals = [1, 1], yvals = [1, 4], dof = 3, n = 1):
    bounds = np.linspace(np.min(xvals), np.max(xvals), 1000)
    gamma = (dof+2)/dof
    K = yvals[0]*xvals[0]**gamma
    process = K/(bounds**gamma)
    working = round(integrate.simps(process, bounds), 2)
    
    print('Energy exchanged via adiabatic working: ' + str(working) + ' Joules')
    return working

def adiabatic_plot(ax, xvals = [1, 1], yvals = [1, 4], dof = 3, n = 1, 
                   clr = 'darkorange'):
    bounds = np.linspace(np.min(xvals), np.max(xvals), 1000)
    gamma = (dof+2)/dof
    K = yvals[0]*xvals[0]**gamma
    process = K/(bounds**gamma)
    
    x = xvals
    y = [yvals[0]]

    y.append(K/(x[1]**gamma))
    
    ax.plot(bounds, process, color = clr, linewidth = 1, alpha = 0.5)
    ax.scatter(x, y, c = 'darkblue', s = 1.5)
    
    ax.set_xlabel(r'Volume: $m^{3}$', labelpad = -5, fontsize = 10, 
                  fontweight = 'bold')
    ax.set_ylabel(r'Pressure: $\frac{N}{m^{2}}$', labelpad = 0, fontsize = 10, 
                  fontweight = 'bold')
    return process

