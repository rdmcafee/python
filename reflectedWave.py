'''
Created on Oct 21, 2022

@author: Mcrye
'''
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('Solarize_Light2')
fig, axs = plt.subplots()

x = np.linspace(0, 10, 1000)
t = 0
step = 10
n = 100

def wave(amplitude, frequency):
    a = amplitude
    f = frequency
    
    p = a*np.cos(2*np.pi * f * t*step - x*2*np.pi*1/f)
    
    return p 

while(t<n):
    plt.plot(x, wave(1, 1), color = 'darkblue', linewidth = 1)
    
    plt.xlim(0, 10)
    plt.ylim(-2, 2)
    
    plt.show()
    
    #plt.clf()
    #plt.cla()
    
    plt.pause(0.1)
    
    t += 1
    
#plt.show()


