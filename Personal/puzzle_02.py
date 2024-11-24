import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from decimal import *

style.use('Solarize_Light2')

fig, ax = plt.subplots()
fig.set_size_inches(10, 3)

A = 1
B = 36

i = 0
n = 120

elements = []
sol = []

while i < n:
    if (i % 2) == 0:
        elements.append(A)
    else:
        elements.append(B)
    i +=1

#print(elements)


eq = Decimal(36 + 15)
getcontext().prec = 75
j = 0
while j < n:
    eq = eq**(-1)
    eq = eq * 15
    eq = eq + elements[j]
    if j % 2 == 0:
        sol.append(eq)

    j +=1
cleanSol = np.zeros_like(sol)
solSize = len(sol)

for x in range (0, solSize):cleanSol[x] = sol[x]

print(cleanSol)

iterations = np.linspace(1, solSize, solSize)
print(iterations)
ax.plot(iterations, cleanSol)
plt.show()
