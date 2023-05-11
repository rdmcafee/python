'''
Created on Feb 18, 2022

@author: Mcrye
'''
import numpy as np
import pandas as pd
from itertools import product
from pprint import pprint

L1 = ['H', 'T']
L2 = L1
L3 = L1
L4 = L1
L5 = L1

df1 = pd.DataFrame(columns = [1, 2, 3, 4, 5])
df2 = pd.DataFrame(columns = [7, 8, 9, 10, 11])

def microstates(array1 = [], array2 = [], array3 = [], 
                array4 = [], array5 = [], array6 = [], array7 = []):
    micro = np.array(list(product(array1, array2, array3, array4, array5)))
    
    print('There are ' + str(len(micro)) + ' microstates \n')
    print(np.shape(micro))
    print(micro)

    return micro
def sortArray(array):
    holder = []
    for x in array:
        holder.append(np.sort(x))
    holder = np.array(holder)
    return holder
def macrostates(sorted_array):
    
    macro = np.unique(sorted_array, axis = 0)
    
    print('\nThere are ' + str(len(macro)) + ' macrostates \n')
    print(macro)
    
    return macro

micro = np.array(microstates(L1, L2, L3, L4, L5))
sorted_micro = np.array(sortArray(micro))
macro = np.array(macrostates(sorted_micro))


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
     r'\Spring2022\Thermal\Homeworks\Test.xlsx')

#####df.to_excel(s)#####
#####Same As#####

with pd.ExcelWriter(s) as writer:
    df3.to_excel(writer)







