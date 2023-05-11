# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 01:05:43 2022

@author: Mcrye
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats as scp
import warnings

plt.style.use('Solarize_Light2')

warnings.filterwarnings('ignore')

fig, ax = plt.subplots()
fig.set_size_inches(10,5)

n = 1000  # How many iterations
nn = 100
#area = np.zeros((n+1,n+1), dtype='float')



def random(num):
    a = np.random.randint(0,num)
    return a

j=0

averages = []

while j < nn:
    
    yes = 0
    no = 0
    i = 0
    while i < n:
    
        prizes = [0,0,0]
        prizes[random(3)] = 1
    
        randIndex = random(3)   #create a random index
        guess = prizes[randIndex]
    
        if guess == 1: 
            prizes.remove(1)
            prizes.remove(0)
            newIndex = random(1)
            newGuess = prizes[newIndex]
            if newGuess == 1:
                yes += 1
            else:
                no += 1
        else:
            prizes.pop(randIndex)
            prizes.remove(0)
            newIndex = random(1)
            newGuess = prizes[newIndex]
            
            if newGuess == 1:
                yes += 1
            else: 
                no += 1
 
        i += 1
    
    try:
        average = yes/(yes + no)
        averages.append(average)
    except ZeroDivisionError:
        print("Division by Zero foo!")
    #print("j loop iteration: " + str(j))
    j += 1

mean = round(np.mean(averages), 4)
print("mean: " + str(mean))
sd = round(np.std(averages), 3)
print("standard deviation: " + str(sd))
x = np.linspace(0,1, 1000)
y = scp.norm.pdf(x, mean, sd)
ax.plot(x,y)
plt.show()
        
input("Press Enter to Continue...")
