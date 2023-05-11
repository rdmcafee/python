'''
Created on Feb 24, 2022

@author: Mcrye
'''
import numpy as np
import MacroMicro_States as th
from itertools import product

array1 = [0, 1, 2]
array2 = [0, 1, 2]
array3 = [0, 1, 2]
array0 = [0, 1, 2]

def micro_test(a1 = [], a2 = [], a3 = [], a4 = []):
    
    if (len(a4) == 0 and len(a3) != 0):
        micro = np.array(list(product(a1, a2, a3)))
    elif (len(a3) == 0 and len(a2) != 0): 
        micro = np.array(list(product(a1, a2)))
    else: 
        micro = np.array(list(product(a1, a2, a3, a4)))
    return micro

#array4 = np.array(list(product(array1, array2)))
array4 = micro_test(array1, array2, array3, array0)
print(array4)

print(len(array2))
print(len(array1))

def sort(array):
    holder = []
    for x in array: 
        holder.append(np.sort(x))
    holder = np.array(holder)
    return holder

def arrays(array):
    n = 0
    list1 = []
    while n < len(array):
        list1.append(array[n])
        n += 1
    list1 = np.asarray(list1)
    return list1


    