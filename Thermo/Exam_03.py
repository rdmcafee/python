'''
Created on Apr 25, 2022

@author: Mcrye
'''
import numpy as np
import Processes as pr
import MacroMicro_States as st
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(12,6)
plt.style.use('Solarize_Light2')

##Question 01
## a, b, c, d

##Question 02

##Construct a table of energy values

A_x = [1.0E-3, 1.0E-3]
A_y = [1.0E5, 5.0E5]

B_x = [1.0E-3, 5.0E-3]
B_y = [5.0E5]

C_x = [5.0E-3, 1.0E-3]
C_y = [1.0E5, 1.0E5]

print('\nProcess A\n')

pr.isochoric_plot(ax, A_x, A_y)
working_A = pr.isochoric_working(A_x, A_y)
heating_A = pr.isochoric_heating(A_x, A_y, 3)
U_A = print('Total change in energy = ' + str(working_A + heating_A))

print('\nProcess B\n')

pr.isothermal_plot(ax, B_x, B_y)
working_B = pr.isothermal_working(B_x, B_y)
heating_B = pr.isothermal_heating(B_x, B_y, 0.4, 3)

print('\nProcess C\n')
pr.isobaric_plot(ax, C_x, C_y)
working_C = pr.isobaric_working(C_x, C_y)
heating_C = pr.isobaric_heating(C_x, C_y, 3)
U_C = print('Total change in energy = ' + str(working_C + heating_C))

fig.suptitle('Thermo Exam03 \nQuestion 02')
ax.text(9.11E-4, 9.93E4, '1')
ax.text(9.11E-4, 2.80E5, 'A')
ax.text(9.11E-4, 5.11E5, '2')
ax.text(2.50E-3, 2.20E5, 'C')
ax.text(5.05E-3, 9.93E4, '3')
ax.text(3.00E-3, 8.52E4, 'D')

plt.show()

##Question 03
##Complete the table

fig, ax = plt.subplots()
fig.set_size_inches(12, 6)

n_3 = 2.34                      #moles
dof_3 = 3                       #degrees of freedom
R = 8.314                       #J/mol*K

def unitConversion(cm3 = 1E3):
    m3 = cm3*(1.0E-2)**3
    return m3

temp_3A = (1.4E6 * unitConversion(10E3))/(n_3 * R)
print('\n' + str(temp_3A) + ' K')

pr.isothermal_plot(ax, [10E-3, 16E-3], [1.4E6], )
pr.adiabatic_plot(ax, [16E-3, 24E-3], [8.75E5, 4.45E5], 3)
pr.isothermal_plot(ax, [15E-3, 24E-3], [7.12E5])
pr.adiabatic_plot(ax, [10E-3, 15E-3], [1.4E6, 7.12E5], 3)

fig.suptitle('Thermo Exam03 \n Question 03')

ax.text(9.80E-3, 1.41E6, 'A')
ax.text(1.60E-2, 8.95E5, 'B')
ax.text(2.40E-2, 4.60E5, 'C')
ax.text(1.47E-2, 6.90E5, 'D')

plt.show()