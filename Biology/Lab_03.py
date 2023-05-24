"""
Created Wednesday 05/24/23

Author: @Mcrye
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.style.use("Solarize_Light2")

bandSize = [1517, 1200, 1000, 900, 800, 700, 600, 500, 400, 300, 200]
logBand = np.log10(bandSize)

distance = [247, 283, 310, 323, 342, 355, 387, 412, 444, 486, 524]

lin_reg = np.polyfit(distance, logBand, 1)
line = stats.linregress(logBand, distance)

x = np.linspace(0, 600, 10000)

print(f'\nLinear Regression: \ny = {round(lin_reg[0], 4)}x + {round(lin_reg[1], 4)}\n')

fig, ax = plt.subplots()

ax.scatter(logBand, distance, color = 'darkblue', alpha = 0.75, s = 6)
ax.plot(lin_reg[0]*x + lin_reg[1], x, color = 'darkred', alpha = 0.5, linewidth = 2)
ax.set_xlabel('Log(Base Pairs)')
ax.set_ylabel('Distance Traveled (cm)')
ax.text(2.8, 500, f'y = {round(lin_reg[0], 4)}*x + {round(lin_reg[1], 4)}')
ax.text(2.85, 475, f'R**2 = {round(line.rvalue**2, 4)}')
ax.set_title('DNA Ladder Calibration')
ax.set_xlim(2.28, 3.22)
ax.set_ylim(200, 600)
plt.tight_layout()
plt.show()

def basePairs (dist):
    return dist*lin_reg[0] + lin_reg[1]

print(f'Undigested: {round(10**basePairs(420), 4)}')
print(f'Digested 1: {round(10**basePairs(420), 4)}')
print(f'Digested 2: {round(10**basePairs(468), 4)}')
print(f'Average # of basepairs: {round(np.average([10**basePairs(420), 10**basePairs(468)]), 4)}')


Class_Genotypes = {'HOT': 86, 'HET': 36, 'HON': 57}

total_alleles = Class_Genotypes['HOT']*2 + Class_Genotypes['HET']*2 + Class_Genotypes['HON']*2
total_dom = Class_Genotypes['HOT'] * 2 + Class_Genotypes['HET']
total_rec = Class_Genotypes['HON']*2 + Class_Genotypes['HET']

p_dom = total_dom/total_alleles
p_rec = total_rec/total_alleles

print(f'\n*** Expected *** \np(dom)^2 = {round(p_dom**2, 4)} \np(rec)^2 = {round(p_rec**2, 4)} \n2*p(het) = {round(2*p_dom*p_rec, 4)}')

print(f'\n*** Observed *** \nHomozygous Taster = {round(Class_Genotypes["HOT"]*2/total_alleles, 4)}')
print(f'Heterozygous Taster = {round(Class_Genotypes["HET"]*2/total_alleles, 4)}')
print(f'Homozygous NonTaster = {round(Class_Genotypes["HON"]*2/total_alleles, 4)}')