'''
Created on Feb 18, 2022

@author: Mcrye
'''
import pandas as pd
import numpy as np
from pprint import pprint
import Thermo.MacroMicro_States as th

A1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
A2 = A1
A3 = A1
B1 = A1
B2 = A1
B3 = A1
B4 = A1
B5 = A1

df1 = pd.DataFrame(columns = ['N_a', 'q_a', '\omega_a', 
                              'N_b', 'q_b', '\omega_b', '\omega_t'])


micro_A = th.microstates(A1, A2, A3)
micro_B = th.microstates(B1, B2, B3, B4, B5)

i = 0
while i < 9: 
    energy_sort = th.add_energies(micro_A, energy = i)
    print('\nEnergy of oscillator A with ' + str(i) + 'quanta: ')
    #print(energy_sort)
    #print('\n')
    df1.loc[i, 'q_a'] = i
    df1.loc[i, '\omega_a'] = len(energy_sort)
    i += 1
    
n = 8
while n >= 0:
    energy_sort = th.add_energies(micro_B, energy = 8-n)
    df1.loc[n, 'q_b'] = 8-n
    df1.loc[n, '\omega_b'] = len(energy_sort)
    n -= 1
    

#print('\nthere are ' + str(len(macro)) + ' Macrostates.\n')

df1.loc[:, 'N_a'] = 3
df1.loc[:, 'N_b'] = 5

j = 0
while j < 9:
    df1.loc[j, '\omega_t'] = df1.loc[j, '\omega_a']*df1.loc[j, '\omega_b']
    j += 1
    
pprint(df1)

multiplicity_total = df1['\omega_t'].to_numpy()
print('\nArray of multiplicities: \n' + str(multiplicity_total))
mult_sum = np.sum(multiplicity_total)
print('\nSum of all multiplicities: ' + str(mult_sum))

k = 0
total_prob = []
while k < 9:
    p = multiplicity_total[k]/mult_sum
    total_prob.append(p)
    k += 1
    
total_prob = np.array(total_prob)
prob_sum = np.sum(total_prob)
   
print('\nArray of probabilities: \n' + str(total_prob))
print('\nSum of probabilities: should equal 1.0: ' + str(prob_sum))

#####Note: Here we merge two data frames *side-by-side* preserving the *left
#####DataFrame. We have matched the indicies since they both start at 0. 
#####The excel file has the microstates on the left and the macrostates on the 
#####right. 
#df3 = pd.merge(df1, df2, left_index = True, right_index = True, how = 'left')    
#pprint(df3)

#####Practice writing to Excel...#####
s = (r'C:\Users\Mcrye\Documents\Personal\School' +
     r'\Spring2022\Thermal\Homeworks\Homework 14\Homework_14.xlsx')

#####df.to_excel(s)#####
#####Same As#####

with pd.ExcelWriter(s) as writer:
    df1.to_excel(writer)






