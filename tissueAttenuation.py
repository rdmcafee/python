'''
Created on Oct 6, 2022

@author: Mcrye
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats as scp
import warnings

warnings.filterwarnings('ignore')
plt.style.use('Solarize_Light2')
fig, axs = plt.subplots()
fig.set_size_inches(10,5)
t = 0

x = np.linspace(0, 30E-2, 100000);
#p = 3.2**(-2*t)*(1*t)*np.cos(z - t)

def attenuation(alpha, freq):
    #input frequency in Hz
    #w = freq
    l = 1540/freq           #average speed in soft tissue
    k = 2*np.pi/(l)
    p_0 = 1
    p = p_0 * (np.e**((-alpha*1E2)*(freq/10E6)*x)) * np.cos(-k*x)
    return p

def envelope(alpha, freq):
    p_0 = 1
    p = p_0 * (np.e**((-alpha*1E2)*(freq/10E6)*x))
    return p
    

        
plt.xlim(0, 30E-2)
plt.ylim(-1, 1)
plt.title('Pressure vs Penetration (2 MHz)')
plt.ylabel('Pressure (Pa)')
plt.xlabel('Penetration (m)')
plt.plot(x, attenuation(0.75, 2.0E6), color = 'darkblue', linewidth = 1)
plt.plot(x, envelope(0.75, 2.0E6), color = 'darkred', linewidth = 1)
plt.plot(x, -envelope(0.75, 2.0E6), color = 'darkred', linewidth = 1)
#plt.plot(x, np.e**(-0.8/(4.28E-3)*x)*np.cos(-(1/1.715E-4)*x))
#plt.plot(x, np.e**(-0.8/(4.28E-3)*x), linewidth = 1, color = 'darkred')
#plt.plot(x, -np.e**(-0.8/(4.28E-3)*x), linewidth = 1, color = 'darkred')
    
plt.show()

fig, axs = plt.subplots()
fig.set_size_inches(10,5)

plt.xlim(0, 5E-2)
plt.ylim(-1,1)
plt.title('Pressure vs Penetration (20 MHz)')
plt.ylabel('Pressure (Pa)')
plt.xlabel('Penetration (m)')

plt.plot(x, attenuation(0.75, 20E6), color = 'darkblue', linewidth = 1)
plt.plot(x, envelope(0.75, 20E6), color = 'darkred', linewidth = 1)
plt.plot(x, -envelope(0.75, 20E6), color = 'darkred', linewidth = 1)

plt.show()
 