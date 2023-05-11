16# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:04:26 2021

@author: Mcrye
"""
import numpy as np
import math as ma
from decimal import Decimal

#Create two matricies which contain the numbers 0-9 and the frequency those
# numbers appear in the first 25 digits of pi. Then plot the probability 
# in a graph with a slide bar which adjusts the number of digits analyzed. 

#Creat matricies. 

digits = [0,1,2,3,4,5,6,7,8,9]; 
pi = [];

k = 1; 

stringPi = str(Decimal(ma.pi))
extraPi = []; 

#extraPi.append(pd.read_csv("Delimited_Pi.txt", sep=", ", header = 0)
extraPi = np.loadtxt("Delimited_Pi.txt", delimiter = ", ");
extraPi = extraPi.astype(int);

#extraPi = extraPi.tolist();

#Create a loop to handle 'n' number of digits in pi, and add these to a 
# matrix. 

i=0; 
while i <= 24:
        pi.append(extraPi[i])
        i += 1

print(pi); 
print('\n');
print(digits); 
#print('\n');
#print(Decimal(ma.pi));

#print(extraPi);


freq = []; 

j = 0;
while j <= 9:
    freq.append(pi.count(j))
    
    j += 1

print('\n');
print(freq);

# The next Task is to graph the probability and maybe add a slide widget
# To adjust the digits of pi and all array/data tables/graphs with updated
# information. 

