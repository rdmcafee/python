'''
Created on Feb 18, 2022

@author: Mcrye
'''
import pandas as pd
import numpy as np
from pprint import pprint
import Thermo.MacroMicro_States as th

L1 = [0, 1, 2, 3]
L2 = L1
L3 = L1
L4 = L1
L5 = L1

df1 = pd.DataFrame(columns = [1, 2, 3, 4])
df2 = pd.DataFrame(columns = [7, 8, 9, 10])

micro = th.microstates(array1 = L1, array2 = L2, array3 = L3, array4 = L4)

energy_sort = th.add_energies(micro, energy = 3)

macro = energy_sort

print('\nthere are ' + str(len(macro)) + ' Macrostates.\n')

n = 0

while n < len(micro):
    series1 = pd.Series(micro[n], index = df1.columns)
    df1 = df1.append(series1, ignore_index = True)
    n += 1

df1[6] = "||"


j = 0
while j < len(macro):
    series2 = pd.Series(macro[j], index = df2.columns)
    df2 = df2.append(series2, ignore_index = True)
    j += 1
#####Note: I here we merge two data frames *side-by-side* preserving the *left
#####DataFrame. We have mached the indicies since they both start at 0. 
#####The excel file has the microstates on the left and the macrostates on the 
#####right. 
df3 = pd.merge(df1, df2, left_index = True, right_index = True, how = 'left')    
pprint(df3)

#####Practice writing to Excel...#####
s = (r'C:\Users\Mcrye\Documents\Personal\School' +
     r'\Spring2022\Thermal\Homeworks\Homework 13\Homework_13.xlsx')

#####df.to_excel(s)#####
#####Same As#####

with pd.ExcelWriter(s) as writer:
    df3.to_excel(writer)







