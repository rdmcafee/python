'''
Created on Feb 23, 2022

@author: Mcrye
'''
import numpy as np
from itertools import product
import warnings

warnings.filterwarnings('ignore')
#modified for coin toss can change lists to array of integers for dice roll

list_1 = ['H', 'T']
list_2 = ['H', 'T']
list_4 = ['H', 'T']
list_5 = ['H', 'T']
list_6 = ['H', 'T']
list_3 = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = list_1 

def microstates(array): 
    micro = list(product(array[0], array[1]))
microstates = list(product(list_1, list_2, list_4, list_5, list_6))
microstates = np.array(microstates)

print(np.shape(microstates))
print('There are ' + str(len(microstates)) + ' microstates \n')


def sortArray(array):
    holder = []
    for x in array:
        holder.append(np.sort(x))
    holder = np.array(holder)
    return holder

sorted_array = sortArray(microstates)
print(sorted_array)

def multiplicity(macro, micro):
    mult = []
    i = 0 
    while i < len(macro): 
        j = 0
        counter = 0
        while j < len(micro):
            if ((macro[i] == micro[j]).all()): 
                counter += 1
            j += 1
        mult.append(counter)
        i += 1
    mult = np.array(mult)
    return mult
            

macrostates = np.unique(sorted_array, axis = 0)

mult = multiplicity(macrostates, sorted_array)
mult = mult.reshape((-1, 1))
print('\nThere are ' + str(len(mult)) + ' items in the multiplicity list.')

print(mult)

print('\nMultiplicity list length SHOULD equal # of macrostates: ' + 
      str(len(mult)) + ' = ' + str(len(macrostates)))

print('sum of multiplicities should equal # microstates: ' + 
      str(np.sum(mult)) + ' = ' + str(len(microstates)))

print('\nThere are ' + str(len(macrostates)) + ' macrostates \n')
print(macrostates)
        


        