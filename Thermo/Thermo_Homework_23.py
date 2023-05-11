'''
Created on Apr 2, 2022

@author: Mcrye
'''
import numpy as np
import matplotlib.pyplot as plt
import Thermo.MacroMicro_States as thermo
plt.style.use('Solarize_Light2')


s1 = [0, 1, 2, 3, 4]
s2 = s1
s3 = s1
s4 = s1

micro = thermo.microstates(s1, s2, s3, s4)

micro_en = thermo.add_energies(micro, 4)

sorted_micro = thermo.sortArray(micro_en)

print(sorted_micro)

macro = thermo.macrostates(sorted_micro)
print(macro)

mult = thermo.multiplicity(macro, sorted_micro)


p1 = [0.43, 0.29, 0.17, 0.09, 0.03]
n = [0, 1, 2, 3, 4]

fig, ax = plt.subplots()
fig.set_size_inches(12, 6)
fig.suptitle('Probability vs n', fontsize = 14)
ax.set_ylabel('P(n)')
ax.set_xlabel('n')

ax.set_ylim(0, 1)
ax.set_xlim(-0.2, 4.2)

ax.set_xticks(np.arange(0, 5, 1))

ax.grid(True)


ax.set_title('(Distinguishable Particles)', fontsize = 10)
ax.scatter(n, p1, color = 'darkred', s = 12, alpha = 0.75)
ax.plot(n, p1, color = 'darkblue', linewidth = 1, alpha = 0.5)
plt.show()

p2 = [0.40, 0.35, 0.15, 0.05, 0.05]

fig, ax = plt.subplots()
fig.set_size_inches(12, 6)
fig.suptitle('Probability vs n', fontsize = 14)
ax.set_ylabel('P(n)')
ax.set_xlabel('n')

ax.set_ylim(0, 1)
ax.set_xlim(-0.2, 4.2)

ax.set_xticks(np.arange(0, 5, 1))

ax.grid(True)


ax.set_title('(Indistinguishable Bosons)', fontsize = 10)
ax.scatter(n, p2, color = 'darkred', s = 12, alpha = 0.75)
ax.plot(n, p2, color = 'darkblue', linewidth = 1, alpha = 0.5)
plt.show()

p3 = [0.42, 0.25, 0.25, 0.08, 0.00]

fig, ax = plt.subplots()
fig.set_size_inches(12, 6)
fig.suptitle('Probability vs n', fontsize = 14)
ax.set_ylabel('P(n)')
ax.set_xlabel('n')

ax.set_ylim(0, 1)
ax.set_xlim(-0.2, 4.2)

ax.set_xticks(np.arange(0, 5, 1))

ax.grid(True)


ax.set_title('(Indistinguishable Fermions)', fontsize = 10)
ax.scatter(n, p3, color = 'darkred', s = 12, alpha = 0.75)
ax.plot(n, p3, color = 'darkblue', linewidth = 1, alpha = 0.5)
plt.show()

fig, ax = plt.subplots()
fig.set_size_inches(12, 6)
fig.suptitle('Probability vs n', fontsize = 14)
ax.set_ylabel('P(n)')
ax.set_xlabel('n')

ax.set_ylim(0, 1)
ax.set_xlim(-0.2, 4.2)

ax.set_xticks(np.arange(0, 5, 1))

ax.grid(True)


ax.set_title('(Indistinguishable Fermions)', fontsize = 10)

ax.scatter(n, p1, color = 'darkred', s = 12, alpha = 0.75)
ax.plot(n, p1, color = 'darkblue', linewidth = 1, alpha = 0.5)

ax.scatter(n, p2, color = 'darkred', s = 12, alpha = 0.75)
ax.plot(n, p2, color = 'darkgreen', linewidth = 1, alpha = 0.5)

ax.scatter(n, p3, color = 'darkred', s = 12, alpha = 0.75)
ax.plot(n, p3, color = 'darkorange', linewidth = 1, alpha = 0.5)
plt.show()