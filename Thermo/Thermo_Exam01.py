# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 00:55:07 2022

@author: Mcrye
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 17:38:54 2022

@author: Mcrye
"""

import matplotlib.pyplot as plt 
import scipy.integrate as scp
import numpy as np

plt.style.use('Solarize_Light2')

coe_Labels = [r'$\mathrm{U_{i}}$', r'$\mathrm{\Delta E_{\omega}}$',
           r'$\mathrm{\Delta E_{Q}}$', r'$\mathrm{U_{f}}$']
coe_xvals = [i for i, _ in enumerate(coe_Labels)]

coe_Energies =[20, 10.69, 4-(20+10.69), 4]

major_xticks = np.arange(0, 10, 1)
minor_xticks = np.arange(0,10, 0.25)

major_yticks = np.arange(0,40, 2)
minor_yticks = np.arange(0,40, 1)


##### Question 1 #####
q1_Energies = [4, -2, -1, 1]
fig, ax = plt.subplots()
fig.suptitle("Exam 1: Question 1.c")
fig.set_size_inches(4,4)

ax.bar(coe_xvals, q1_Energies, tick_label = coe_Labels, color = 'darkred',
       width = 0.5, alpha = 0.8)
ax.set_xlabel('Energy Category')
ax.set_ylabel('Energy Quantity ' + r'$\mathrm{\beta V_{0}P_{0}}$')

ax.set_xticks(np.arange(-0.25, 4.25, 0.5), minor = True)

ax.set_ylim(-10.5, 10.5)
ax.set_xlim(-0.3, 3.3)
ax.axhline(0, color = 'k', linewidth = 0.5)


ax.set_yticks(np.arange(-10,10,1), minor = True)
ax.set_yticks(np.arange(-10,10, 4))

ax.grid(which = 'major', color = 'k', alpha = 0.1)
ax.grid(which = 'minor', color = 'k', alpha = 0.05)

plt.show()


##### Question 2 #####
fig, ax = plt.subplots()
fig.suptitle("Exam 1: Question 2 \nPV _Graph: 2 moles of a Diatomic Gass")
fig.set_size_inches(4, 4)

q2_xscatter = [0.45, 0.45*(1/4), 0.45*4, 0.45*4]
q2_yscatter = [8.5, 8.5, 8.5/16, 8.5]

q2_boundsA = np.linspace((0.45/4), 0.45, 10)
q2_processA = 8.5 *q2_boundsA/q2_boundsA

q2_boundsB = np.linspace((0.45/4), 0.45*4, 100)
q2_processB = (1/q2_boundsB)*(8.5*(0.45/4))

ax.set_xlabel('Volume: $m^3$')
ax.set_ylabel('Pressure: $10^4$ ' + r'$\frac{N}{m^2}$')

ax.set_xticks(major_xticks)
ax.set_xticks(minor_xticks, minor = True)
ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor = True)

ax.set_ylim(0, 10)
ax.set_xlim(0, 2)

ax.grid(which = 'minor', color = 'k', alpha = 0.05)
ax.grid(which = 'major', color = 'k', alpha = 0.1)

ax.scatter(q2_xscatter, q2_yscatter, color = 'darkred', s = 10)

ax.plot(q2_boundsA, q2_processA, color = 'darkred')

ax.plot(q2_boundsB, q2_processB, color = 'darkred')

ax.plot((0.45*4, 0.45*4), ((1/(0.45*4))*8.5*(0.45/4), 8.5), color = 'darkred')

ax.arrow(0.45/2, 8.5, -0.04, 0.0, shape = 'full', lw = 0.5, 
         length_includes_head = True, head_width = 0.1, color = 'darkred', 
         overhang = 0.3)

ax.arrow(0.5, (1/(0.5))*8.5*(0.45/4), 0.05, 
         ((1/(0.55)))*8.5*(0.45/4)-(1/(0.5))*8.5*(0.45/4), shape = 'full', 
         lw = 0.5, length_includes_head = True, head_width = 0.05, 
         color = 'darkred', overhang = 0.3)

ax.arrow(0.45*4, 4, 0.0, 0.08, shape = 'full', lw = 0.5, 
         length_includes_head = True, head_width = 0.05, color = 'darkred', 
         overhang = 0.3)

dof = 5

moles = 2.5

R = 8.314

question2a_Vi = 0.45
question2a_Vf = question2a_Vi/4
question2a_dV = question2a_Vf - question2a_Vi

question2a_P = 8.5

question2a_Q = ((dof/2)+1)*question2a_dV*question2a_P

question2a_W = scp.simps(q2_processA, q2_boundsA)

question2a_dU = (dof/2)*question2a_P*question2a_dV

print('*****')
print('Question 2')
print('Process A Heating: ' + str(round(question2a_Q, 4)) + ' Joules')
print('Process A Working: ' + str(round(question2a_W, 4)) + ' Joules')
print('Total energy exchanged with surroundings: ' + 
      str(round(question2a_Q + question2a_W, 4)) + ' Joules')
print('Total energy change calculated direction from PV change: ' + 
      str(round(question2a_dU, 4)) + ' Joules')

question2b_Vi = 0.1125
question2b_Vf = question2a_Vi * 4

question2b_Pi = 8.5
question2b_Pf = (1/question2b_Vf)*(8.5*(0.45/4))

##print('question2b_Pf: ' + str(round(question2b_Pf, 4)) + 
##      ' Vs: ' + str(round(8.5/16, 4))) ## Just making sure i have the right Pf

question2b_W = -1*scp.simps(q2_processB, q2_boundsB)
print('#####')
print('Process B Working: ' + str(round(question2b_W, 4)) + ' Joules')

question2c_V = 0.45
question2c_Pi = question2b_Pf
question2c_Pf = 8.5

question2c_dP = question2c_Pf-question2c_Pi

question2c_Q = (dof/2)*question2c_V*question2c_dP

print('#####')
print('Process C Heating: ' + str(round(question2c_Q, 4)) + ' Joules')

plt.show()


##### Question 3 #####
x_vals = [(2.0, 5.0)]
y_vals = [(2.0, 4.0)]

fig, ax = plt.subplots(2,1)
fig.set_size_inches(4,4)
fig.suptitle("Exam 01: \nQuestion 3: Work...", fontsize = 12)
#ax.plot(x_vals, y_vals)

print('\n*****')
print("Question 3: ")
process_a = np.linspace(2.0, 2.5, 1000)
a = 2*process_a - 2
work_a = 1*scp.simps(a, process_a)

process_b = np.linspace(2.5, 3.0, 1000)
b = process_b + (1/2)
work_b = 1*scp.simps(b, process_b)

process_c = np.linspace(3.0, 15/4, 1000)
slope_c = (4.0-3.5)/((15/4)-3)
c_yintercept = 3.5 - slope_c*3
print("Process C: (3.0 - 3.75)" + "\nSlope: " + str(round(slope_c, 2)) 
      + "\nY_Intercept: " +str(round(c_yintercept, 2)))
c = slope_c*process_c + c_yintercept
work_c = 1*scp.simps(c, process_c)


process_d = np.linspace(15/4, 5.0, 1000)
d = 4*(process_d/process_d)
work_d = 1*scp.simps(d, process_d)


work_total = work_a + work_b + work_c + work_d

print("\nQuestion 3a: \nTotal work done ON the gas BY the surroundings: " + 
      str(round(work_total, 2)) + " Joules")

ax[0].set_xticks(major_xticks)
ax[0].set_xticks(minor_xticks, minor = True)
ax[0].set_yticks(major_yticks)
ax[0].set_yticks(minor_yticks, minor = True)

ax[0].set_ylim(0, 5.0)
ax[0].set_xlim(1, 6.0)
ax[0].set_xlabel("Volume")
ax[0].set_ylabel("Pressure")

ax[0].grid(which = 'minor', color = 'k', alpha = 0.05)
ax[0].grid(which = 'major', color = 'k', alpha = 0.1)

total_work = str('Total Work: ' + str(round(work_total, 2)) 
           + " " + r'$\mathrm{ V_{0}P_{0}}$'
           + "\n Work_A: " + str(round(work_a, 2)) + " " 
           + r'$\mathrm{ V_{0}P_{0}}$'
           + "\n Work_B: " + str(round(work_b, 2)) + " " 
           + r'$\mathrm{ V_{0}P_{0}}$'
           + "\n Work_C: " + str(round(work_c, 2)) + " " 
           + r'$\mathrm{ V_{0}P_{0}}$'
           + "\n Work_D: " + str(round(work_d, 2)) + " " 
           + r'$\mathrm{V_{0}P_{0}}$')


prop = dict(boxstyle = 'round', facecolor = 'w', alpha = 0.2)

 
ax[0].plot(process_a, a, color = 'darkred', alpha = 0.4)
ax[0].plot(process_b, b, color = 'darkred', alpha = 0.4)
ax[0].plot(process_c, c, color = 'darkred', alpha = 0.4)
ax[0].plot(process_d, d, color = 'darkred', alpha = 0.4)

ax[0].fill_between(process_a, 0, a, where = (process_a < 2.5),
                color = 'darkgreen', alpha = 0.5)
ax[0].fill_between(process_b, 0, b, where = (process_b > 2.5), 
                color = 'darkgreen', alpha = 0.5)
ax[0].fill_between(process_c, 0, c, where = (process_c > 3.0), 
                color = 'darkgreen', alpha = 0.5)
ax[0].fill_between(process_d, 0, d, where = (process_d > 3.75), 
                color = 'darkgreen', alpha = 0.5)

ax[0].scatter(x_vals, y_vals, color = 'darkred', alpha = 0.5)
ax[0].text(1.9, 2.1, "K")
ax[0].text(5.1, 4.1, "Y")

ax[0].text(1.9, 2.5, "Process_A", fontsize = 8)
ax[0].text(2.45, 3.35, "Process_B", fontsize = 8)
ax[0].text(3.0, 3.75, "Process_C", fontsize = 8)
ax[0].text(4.25, 4.1, "Process_D", fontsize = 8)

ax[0].arrow(2.75, 3.25, -0.04, -0.04, shape = 'full', lw = 0.5, 
         length_includes_head = True, head_width = 0.05, color = 'darkred', 
         overhang = 0.3)

ax[0].arrow(4.5, 4.0, -0.04, 0, shape = 'full', lw = 0.5, 
         length_includes_head = True, head_width = 0.05, color = 'darkred', 
         overhang = 0.3)
#ax[0].text(0.05,0.95, total_work, transform=ax[0].transAxes, fontsize=8, 
#           verticalalignment='top', bbox=prop)


ax[1].bar(coe_xvals, coe_Energies, tick_label = coe_Labels, color = 'darkred', 
          width = 0.5, alpha = 0.8)
ax[1].set_xlabel('Energy Category')
ax[1].set_ylabel('Energy Quantity ' + r'$\mathrm{\beta V_{0}P_{0}}$')

#ax[1].set_xticks(coe_xvals, coe_Labels)
ax[1].set_xticks(np.arange(-0.25, 4.25, 0.5), minor = True)

ax[1].set_ylim(-15, 15)
ax[1].set_xlim(-0.3, 3.3)
ax[1].axhline(0, color = 'k', linewidth = 0.5)


ax[1].set_yticks(np.arange(-30,30,5), minor = True)
ax[1].set_yticks(np.arange(-30,30, 10))



ax[1].grid(which = 'major', color = 'k', alpha = 0.1)
ax[1].grid(which = 'minor', color = 'k', alpha = 0.05)

question3b_dof = 3

question3b_slope = (2-4)/(2-5)
question3b_intercept = 2-(2*question3b_slope)
question3b_linearBounds = np.linspace(2, 5, 10)
question3b_linearProcess = (question3b_slope*question3b_linearBounds + 
                            question3b_intercept)

question3b_dU = (question3b_dof/2)*(4-20)
question3b_Q = question3b_dU - work_total
question3b_linearWork = scp.simps(question3b_linearBounds, 
                                  question3b_linearProcess)
question3b_linearQ = question3b_dU - question3b_linearWork

ax[0].plot(question3b_linearBounds, question3b_linearProcess, 
           color = 'darkblue', alpha = 0.5)
print('#####' + '\nQuestion 3b: ')
print('Total change in internal energy: ' + str(round(question3b_dU, 4)) +
      ' Joules')
print('\nEnergy exchange via heating for the original process: ' +
      str(round(question3b_Q, 4)) + ' Joules')
print('\nEnergy exchange via working for the linear process: ' +
      str(round(question3b_linearWork, 4)) + ' Joules')
print('Energy exchange via heating for the linear process: ' + 
      str(round(question3b_linearQ, 4)) + ' Joules')
plt.show()

##### Question 3 #####
fig, ax = plt.subplots()
fig.set_size_inches(4, 4)
fig.suptitle("Exam 01 \nQuestion:3.c Work via Linear Process")
coe_Energies_02 = [20, 7, 4-(20+7), 4]
ax.bar(coe_xvals, coe_Energies, tick_label = coe_Labels, color = 'darkred', 
          width = 0.5, alpha = 0.6, label = 'Process 01')
ax.bar(coe_xvals, coe_Energies_02, tick_label = coe_Labels, color = 'darkblue', 
          width = 0.5, alpha = 0.6, label = 'Process 02')
ax.set_xlabel('Energy Category')
ax.set_ylabel('Energy Quantity ' + r'$\mathrm{\beta V_{0}P_{0}}$')

ax.set_xticks(np.arange(-0.25, 4.25, 0.5), minor = True)

ax.set_ylim(-15, 15)
ax.set_xlim(-0.3, 3.3)
ax.axhline(0, color = 'k', linewidth = 0.5)


ax.set_yticks(np.arange(-30,30,5), minor = True)
ax.set_yticks(np.arange(-30,30, 10))

ax.grid(which = 'major', color = 'k', alpha = 0.1)
ax.grid(which = 'minor', color = 'k', alpha = 0.05)

plt.legend()

plt.show()

##### Question 4 #####
fig, ax = plt.subplots()
fig.set_size_inches(4,4)
fig.suptitle('Exam01 \nQuestion 04')

question4_xVals = [2, 6]
question4_yVals = [4, 2]

question4_moles = 1

ax.scatter(question4_xVals, question4_yVals, color = 'darkred', s = 2)

ax.text(1.5, 4.2, '$P_{1}$')
ax.text(6.5, 1.8, '$P_{2}$')

question4_Bounds = np.linspace(2, 6, 100)
question4_isothermal = 8/question4_Bounds
question4_adiabatic1 = (4*((2)/(question4_Bounds))**(5/3))
question4_adiabatic2 = (4*((2)/(question4_Bounds))**(7/5))
question4_adiabatic3 = (4*((2)/(question4_Bounds))**(9/7))

ax.plot(question4_Bounds, question4_isothermal, color = 'darkred', alpha = 0.5)
ax.plot(question4_Bounds, question4_adiabatic1, color = 'darkblue', alpha = 0.5)
ax.plot(question4_Bounds, question4_adiabatic2, color = 'darkgreen', alpha = 0.5)
ax.plot(question4_Bounds, question4_adiabatic3, color = 'darkorange', alpha = 0.5)

ax.text(4, 2.5, 'Isothermal')
ax.text(2.5, 1, 'Adiabatic')

ax.set_xlim(0, 8)
ax.set_ylim(0, 6)

print('\n*****')
print('Question 4')
print('Clearly cannot be Isobaric or Isochoric')
plt.show()