'''
Created on Apr 13, 2022

@author: Mcrye
'''
import numpy as np

def entropy(state = 'A', P = 1.0E5, V = 0.5, n = 1.0, amu = 1.00797):
    pi = np.pi
    R =8.314                            #J/mol*K
    k = 1.38E-23                        #N*m/K
    h = 6.626E-34                       #N*m*s
    N = 6.022E23 * n                    #No of particles
    
    m = amu*n * (1/1000)                #kg                           #
    
    T = (P*V)/(n*R) 
                        #K
    S = N*k*(np.log((k*T/P)*(2*pi*m*k*T/(h**2))**(3/2))+(5/2))
    
    print('Entropy, S, at state ' + state + ' = ' + 
          str(np.format_float_scientific(S, 4)) + ' J/K \n')
    return S

    