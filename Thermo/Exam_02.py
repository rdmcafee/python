'''
Created on Mar 24, 2022

@author: Mcrye
'''

import matplotlib.pyplot as plt
import numpy as np
import Thermo.MacroMicro_States as mm

d1 = [1, 2, 3, 4]
d2 = d1
d3 = d1
d4 = d1

micro = mm.microstates(d1, d2, d3, d4)

print(micro)

energySorted = mm.add_energies(micro, 7)

print(energySorted)

macro = mm.macrostates(energySorted)

print(macro)

mult = mm.multiplicity(macro, micro)

print(mult)


