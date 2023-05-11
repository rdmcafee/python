'''
Created on Apr 13, 2022

@author: Mcrye
'''
import numpy as np
import matplotlib.pyplot as plt
import Entropy as S
import Processes as th

state_I = S.entropy('I', P = 3.0E5, V = 0.15, n = 1.64)
state_II = S.entropy('II', P = 3.5E5, V = 0.4, n = 1.64)
state_III = S.entropy('III', P = 1.5E5, V = 0.4, n = 1.64)
state_IV = S.entropy('IV', P = 1.5E5, V = 0.15, n = 1.64)

process_A = state_II - state_I
process_B = state_III - state_II
process_C = state_IV - state_III
process_D = state_I - state_IV

print('\n Delta S for process A = ' + 
      str(np.format_float_scientific(process_A, 3)))
print('\n Delta S for process B = ' + 
      str(np.format_float_scientific(process_B, 3)))
print('\n Delta S for process C = ' + 
      str(np.format_float_scientific(process_C, 3)))
print('\n Delta S for process D = ' + 
      str(np.format_float_scientific(process_D, 3)))

total_S = process_A + process_B + process_C + process_D

print('\n Total Entropy change for the gas = ' + 
      str(np.format_float_scientific(total_S, 3)))
