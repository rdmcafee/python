# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:27:49 2021

@author: Mcrye
"""

import numpy as np
#import scipy.integrate as scip
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

a = np.array([1,2,3])
b = np.array([2,3,4])
A = a.reshape(3,1)
c = np.zeros(shape = (1, 10))
#ab = A@b
AB = a*b
print(a)
print(A)
print(b)
print(c)
#print(B)
#print(ab)
print(AB)
x = np.linspace(0,10, 11)
y = np.linspace(0,10,11).reshape(11,1)
z = x*y
i = 0
print(z[:])
while i < 11:
    print(x[0,i])
    i += 1


"""
x = np.linspace(0,100,101).astype(complex).reshape(101,1) 
#creates an array from 0 to 100 spaced evenly appart and changes type of the matrix to include complex numbers. Then changes the shape of the matrix to have 101 rows and 1 column 
print("\n this is the general x array")
print(x[-1]) #this prints the last term in the x array
print(x[0:101,0]) 
#this takes the x array and prints out the first term of each row. x[start:stop:slice[position on that row]] Evaluating over the entire matrix can be acheived by the equivalent expression print(x[:0])

y = np.zeros((100,1),dtype="complex")
#creates a zero array of 100 rows and 1 column with the specified data type
print("\n this is the general y array")
print(y[:,0])
print(str(1j**2)) #1j is the complex i
t = np.linspace(0,5,100).astype(complex)
tt = np.linspace(1,4,100)
uu = tt**2
u = t**2
p = np.trapz(u,t)
q = scip.simps(u,t)
#This is supposed to give the trapezoidal approximation of the function. This is evaluated from 0 to 5... = 1/3 (t^3) = 41.66666 Both simpsons and trapezoid approaches give a good approximation. Simpsons approach seems to be more accurate. 

plt.plot(t,u)
plt.fill_between(tt,uu,color = 'g', alpha = 0.2)
#plt.show()
print("\n this is t")
print(t)
print("\n this is an index of t expression")
print(t[2])
print("\n this is p")
print(p)
print("\n this is q")
print(q)

d = [0,1,4,9,16,25]

e = np.trapz(d)
#this gives a really gross approximation of the integral of the above function
print("\n")
print(e)

#n = np.linspace(1,10,10).astype(complex).reshape(10,1)
n = 5

Cn = np.zeros((1, n), dtype="complex")
#printing Cn to see the shape of the array
print("\n printing Cn to see the shape of the array")
print(Cn)
plt.show()

print("\n Print the index to confirm cycle")
for i in range(0,n):
    
    #print the index
    print(i)
    
    print(t[i])
    
    Cn[i,0] = np.trapz(u*i, t)
    #where u*i is the iterative function to evaluate. The quantized energy level is associated with the index length while the spacial evaluation is related to (in this case) the t matrix. This then places each iterative evaluation into the Cn matrix to be used elsewhere. 
    print(Cn[i,0])
    print("\n")
    
print("\n this is the final Cn array")
print(Cn)
"""