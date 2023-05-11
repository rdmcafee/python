'''
Created on Feb 18, 2022

@author: Mcrye
'''
import pandas as pd
import sys
import numpy as np
from pprint import pprint
import MacroMicro_States as th

np.printoptions(threshold = np.inf)

L1 = ['1a', '2a', '3a', '4a']
L2 = ['1b', '2b', '3b', '4b']
L3 = ['1c', '2c', '3c', '4c']
L4 = ['1d', '2d', '3d', '4d']
L5 = ['1e', '2e', '3e', '4e']
L6 = ['1f', '2f', '3f', '4f']
L7 = ['1g', '2g', '3g', '4g']

LL1 = [1, 2, 3, 4]
LL2 = LL1
LL3 = LL1
LL4 = LL1
LL5 = LL1
LL6 = LL1
LL7 = LL1

df1 = pd.DataFrame(columns = [1, 2, 3, 4, 5, 6, 7])
df2 = pd.DataFrame(columns = [9, 10, 11, 12, 13, 14, 15])
df_sorted = pd.DataFrame(columns = [1, 2, 3, 4, 5, 6, 7])

micro = th.microstates(LL1, LL2, LL3, LL4, LL5, LL6, LL7)

sorted_array = th.sortArray(micro)

macro = th.macrostates(sorted_array)

mult = th.multiplicity(macro, sorted_array)

#print('\nMultiplicity\n')
#print(mult)
#print('\nSorted Array\n')

print('\n')
print(macro[13])
print(mult[13])
print(len(micro))

i = 0
while i < len(sorted_array):
    sorted_series = pd.Series(sorted_array[i], index = df_sorted.columns)
    df_sorted = df_sorted.append(sorted_series, ignore_index = True)
    i += 1



n = 0
while n < len(micro):
    series1 = pd.Series(micro[n], index = df1.columns)
    df1 = df1.append(series1, ignore_index = True)
    n += 1

df1[8] = "||"


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
     r'\Spring2022\Thermal\Homeworks\Homework 12\Homework_12.xlsx')

#####df.to_excel(s)#####
#####Same As#####

with pd.ExcelWriter(s) as writer:
    df3.to_excel(writer)







