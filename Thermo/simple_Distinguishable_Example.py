'''
Created on Feb 18, 2022

@author: Mcrye
'''
import pandas as pd
import numpy as np
from pprint import pprint
import Thermo.MacroMicro_States as th

L1 = ['1a', '2a']
L2 = ['1b', '2b']
L3 = ['1c', '2c']
L4 = ['1d', '2d']
L5 = ['1e', '2e']
L6 = ['1f', '2f']
L7 = ['1g', '2g']

L11 = [1, 2]
L12 = [1, 2]

df1 = pd.DataFrame(columns = [1, 2])
df2 = pd.DataFrame(columns = [4, 5])

micro = th.microstates(L1, L2, L3, L4)

sorted_array = th.sortArray(micro)

macro = th.macrostates(sorted_array)

n = 0

while n < len(micro):
    series1 = pd.Series(micro[n], index = df1.columns)
    df1 = df1.append(series1, ignore_index = True)
    n += 1

df1[3] = "||"


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
     r'\Spring2022\Thermal\Homeworks\Test.xlsx')

#####df.to_excel(s)#####
#####Same As#####

with pd.ExcelWriter(s) as writer:
    df3.to_excel(writer)







