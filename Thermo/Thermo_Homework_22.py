'''
Created on Mar 31, 2022

@author: Mcrye
'''
import numpy as np
from decimal import *


## Question 2 ##

ratio23 = np.format_float_scientific(Decimal(np.exp(387.6)), precision = 3)

print('ratio P(2)/P(3) = ' + str(ratio23))

## Question 3 ##

kbT = 0.0258

B1 = Decimal(np.exp(-5/kbT))
B2 = Decimal(np.exp(-10/kbT))
B3 = Decimal(np.exp(-20/kbT))
Z = np.format_float_scientific(Decimal(B1+B2+B3), precision = 3)
p1 = np.format_float_scientific(Decimal((B1/(B1+B2+B3))), precision = 3)
print('\nB1 = ' + str(np.format_float_scientific(B1, precision = 3)))
print('\nB2 = ' + str(np.format_float_scientific(B2, precision = 3)))
print('\nB3 = ' + str(np.format_float_scientific(B3, precision = 3)))
print('\nZ = ' + str(Z))
print('\nP(1) = ' + str(p1))
