'''
Created on Feb 23, 2022

@author: Mcrye
'''
import numpy as np
from itertools import product
import warnings

warnings.filterwarnings('ignore')
#modified for coin toss can change lists to array of integers for dice roll

def microstates(array1 = [], array2 = [], 
                array3 = [], array4 = [], 
                array5 = [], array6 = [], 
                array7 = []):
    
    if (len(array7) == 0 and len(array6) != 0): 
        micro = np.array(list(product(array1, array2, array3, array4, 
                                  array5, array6)))
    elif (len(array6) == 0 and len(array5) != 0):
        micro = np.array(list(product(array1, array2, array3, array4, 
                                  array5)))
    elif (len(array5) == 0 and len(array4) != 0):
        micro = np.array(list(product(array1, array2, array3, array4)))
        
    elif (len(array4) == 0 and len(array3) != 0): 
        micro = np.array(list(product(array1, array2, array3)))
        
    elif (len(array3) == 0 and len(array2) != 0): 
        micro = np.array(list(product(array1, array2)))
        
    elif (len(array2) == 0 and len(array1) != 0): 
        print('Must input at least two arrays')
        micro = np.array([])
        
    elif len(array1) == 0:
        print('Must input at least two arrays')
        micro = np.array([])
        
    else:
        micro = np.array(list(product(array1, array2, array3, array4,
                                      array5, array6, array7)))
    
    
    print('There are ' + str(len(micro)) + ' microstates \n')
    #print(np.shape(micro))
    #print(micro)

    return micro

def sortArray(array):
    holder = []
    for x in array:
        holder.append(np.sort(x))
    holder = np.array(holder)
    return holder


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
    mult.reshape((-1,1))
    
    print('\nThere are ' + str(len(mult)) + ' items in the multiplicity list.')

    print(mult)
    
    print('\nMultiplicity list length SHOULD equal # of macrostates: ' + 
      str(len(mult)) + ' = ' + str(len(macro)))

    return mult

def add_energies(microstates, energy = 0):
    n = 0
    new_sort = []
    while n < len(microstates):
        if np.sum(microstates[n]) == energy:
            new_sort.append(microstates[n])   
        n += 1
    new_sort = np.array(new_sort)
    print('\nThere are ' + str(len(new_sort)) + ' energy microstates:')
    print('\nHere is the energy sorted array \n')
    print(new_sort) 
    return new_sort

 
def macrostates(sorted_array):
    
    macro = np.unique(sorted_array, axis = 0)
    
    print('\nThere are ' + str(len(macro)) + ' macrostates \n')
    print(macrostates)
    
    return macro



        