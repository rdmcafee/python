"""
Created Monday 05/15/23

Author: @Mcrye
"""
import numpy as np 
from itertools import product

class parent ():

    def __init__(self, alleles = []):

        self.alleles = alleles
        self.between_set = []
        self.separated_alleles = [[]] * len(alleles)

        self.Setup()

    def Setup(self):
        #print(f' Length of alleles list = {len(self.alleles)}')
        #print(f' Parent alleles = {self.alleles}')

        i = 0
        while i < len(self.alleles):
            
            for gene in self.alleles[i]:
                self.separated_alleles[i] = self.separated_alleles[i] + [gene]
            i += 1
        pass
        

parent_A = parent(['Aa', 'Bb'])
parent_B = parent(['aa', 'Bb'])


def cross(parents):
    progeny = []
    new_prog = []
    i = 0
    while i < len(parents):

        progeny.append(list(product(parents[0].separated_alleles[i], 
        parents[1].separated_alleles[i])))

        i += 1
    new_prog.append(list(product(progeny[0], progeny[1])))
    #progeny = list(product(progeny[0], progeny[1]))
    return new_prog

prog = cross([parent_A, parent_B])

print(f'Parent A has Alleles {parent_A.separated_alleles}')
print(f'Parent B has Alleles {parent_B.separated_alleles}')

#reshape and sort the progeny (prog) array so all alleles are aligned
prog = np.array(prog).reshape(-1, 2)
prog = np.sort(prog)
prog = prog.reshape(-1, 4)
print(prog)

#Create a unique list of genotypes and also return its frequency
unique_list, counts = np.unique(prog, axis = 0, return_counts = True)

#Reshape the counts of genotypes array so it can be concatenated
counts = counts.reshape(-1, 1)

#Add counts to end of associated genotype
unique_list = np.concatenate((unique_list, counts), axis = 1)

print(f'\nUnique genotypes and their frequencies are displayed here: \
\n\n{unique_list}')
