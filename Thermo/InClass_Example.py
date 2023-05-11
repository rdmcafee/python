'''
Created on Apr 14, 2022

@author: Mcrye
'''
import Entropy as S
import numpy as np
import Processes as th
import matplotlib.pyplot as plt

gamma = 1.4
def adiabatic(V = 2, P = [1E3, 1], gamma = 1.4):
    K = P[0]*(V**gamma)
    V2 = (K/P[1])**(1/gamma)
    print('K = ' + str(K))
    print('V2 = ' + str(V2))
    return V2

def isothermal(V = 1, P = [1E3, 5E2]):
    V2 = P[0]*V/P[1]
    print('V2 = ' + str(V2))
    return V2

V2 = isothermal(P = [1E3, 100])

state1 = S.entropy('1', P = 1E3, V = 1)
state2 = S.entropy('2', P = 100, V = 1E1)

total_S = state2 - state1

print('\nTotal Entropy = ' + str(total_S))

print(8.314*np.log(1E1))

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

th.isothermal_plot(ax, [1, 10], [1E3])

plt.show()