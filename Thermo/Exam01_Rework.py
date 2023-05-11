'''
Created on Feb 16, 2022

@author: Mcrye

Reworking Exam 01 and importing Process module to help

'''
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
#import Thermo.Processes as th
import Processes as th

#####Question 1a #####
print('***** \nQuestion 1a: ')
print('Thermal conductivity*')

#####Question 1b #####
print('\n***** \nQuestion 1b: ')
print('Temperature is a state variable, whereas melting point is' + 
      ' a property of a material')

#####Question 1c #####
print('\n***** \nQuestion 1c: ')
print('Yada yada yada, *greater mass*')

#####Question 2a #####
## we are dealing with 4 moles of a monoatomic gas; n = 4, DOF = 3
## The gas occupies a volume of 1.4 m^3 with a pressure 1.8E5 Pa
## How much energy will the gas exchange with env in an isochoric process
## to three times it's initial pressure. 

fig, ax = plt.subplots()
fig.set_size_inches(6, 5)
fig.suptitle('Thermo: Exam 1 \nQuestion 2a')

q2a_V1 = 1.4
q2a_V2 = 1.4

q2a_P1 = 1.8E5
q2a_P2 = 3*q2a_P1

q2a_n = 4
q2a_dof = 3

q2a_Volumes = [q2a_V1, q2a_V2]
q2a_Pressures = [q2a_P1, q2a_P2]

print('\n***** \nQuestion 2a: ')
print('\n' + str(q2a_Volumes) + str(q2a_Pressures))
th.isochoric_plot(ax, q2a_Volumes, q2a_Pressures)
th.isochoric_heating(q2a_Volumes, q2a_Pressures, q2a_dof)
th.isochoric_working(q2a_Volumes, q2a_Pressures)
th.dU(q2a_Volumes, q2a_Pressures, q2a_dof, q2a_n)

print('\n***** \nQuestion 2b: ')

q2b_V1 = 1.4
q2b_V2 = q2b_V1/3

q2b_P1 = 3*1.8E5

q2b_Volumes = [q2b_V1, q2b_V2]
q2b_Pressures = [q2b_P1]

q2a_dof = 3
q2a_n = 4

th.isothermal_plot(ax, q2b_Volumes, q2b_Pressures)
th.isothermal_working(q2b_Volumes, q2b_Pressures)

plt.show()

##### Question 3a #####
## Five moles of a polyatomic gas goes from state Y to state K 
## this occurs via an isothermal process. n = 5; dof = 7

fig, ax = plt.subplots()
fig.set_size_inches(6, 5)
fig.suptitle('Thermo: Exam 1 \nQuestion 3a')

q3a_n = 5
q3a_dof = 7

q3a_Volumes = [4, 1]
q3a_Pressures = [1]

th.isothermal_plot(ax, q3a_Volumes, q3a_Pressures, clr = 'darkorange')

print('\n***** \nQuestion 3b: ')
th.isothermal_working(q3a_Volumes, q3a_Pressures)

q3b_isobaric_Volumes = [4, 1]
q3b_isobaric_Pressures = [1, 1]

q3b_isochoric_Volumes = [1, 1]
q3b_isochoric_Pressures = [1, 4]

th.isobaric_plot(ax, q3b_isobaric_Volumes, q3b_isobaric_Pressures, 
                 clr = 'darkred')
th.isochoric_plot(ax, q3b_isochoric_Volumes, q3b_isochoric_Pressures, 
                  clr = 'darkred')

th.isobaric_working(q3b_isobaric_Volumes, q3b_isobaric_Pressures)


##### Question 3c #####

## Now compare heating from the isothermal process to the heating
## of a linear process from Y to K

print('\n***** \nQuestion 3c: ')
q3c_linear_Volumes = [4, 1]
q3c_linear_Pressures = [1, 4]

th.linear_plot(ax, q3c_linear_Volumes, q3c_linear_Pressures, clr = 'darkgreen')

th.isothermal_working(q3a_Volumes, q3a_Pressures)
th.linear_working(q3c_linear_Volumes, q3c_linear_Pressures)

plt.show()

##### Question 4a #####

## Given a PVT bar graph of an initial and final state, determine if the 
## process described is one of the simple processes we've studied

fig, ax = plt.subplots()
fig.set_size_inches(6, 5)
fig.suptitle('Thermo: Exam 1 \nQuestion 4a')

dof_01 = 3
dof_02 = 5
dof_03 = 7

def adiabatic_constant(xval, yval, dof):
    gamma = (dof+2)/dof
    K = []
    K.append(round(yval[0] * (xval[0]**gamma), 2))
    K.append(round(yval[1] * (xval[1]**gamma), 2))
    print('\nAdiabatic constant figured for: ' + str(dof) + ' DOF')
    print('\nP_1 = ' + str(yval[0]) + '\nV_1 = ' + 
          str(xval[0]) + '\nK = ' + str(K[0]))
    print('\nP_2 = ' + str(yval[1]) + '\nV_2 = ' + 
          str(xval[1]) + '\nK = ' + str(K[1]))

q4a_V1 = [2]
q4a_V2 = [3*q4a_V1[0]]

q4a_P1 = [4]
q4a_P2 = [q4a_P1[0]/2]

q4a_T1 = 3
q4a_T2 = q4a_T1 * (3/2)

q4a_Volumes = [q4a_V1[0], q4a_V2[0]]
q4a_Pressures = [q4a_P1[0], q4a_P2[0]]
q4a_Temps = [q4a_T1, q4a_T2]

th.isothermal_plot(ax, q4a_Volumes, q4a_P1)
th.adiabatic_plot(ax, xvals = q4a_Volumes, yvals = q4a_Pressures, dof = 3)
th.adiabatic_plot(ax, q4a_Volumes, q4a_Pressures, 5, 1)
th.adiabatic_plot(ax, q4a_Volumes, q4a_Pressures, 7, 1)

ax.scatter((2, q4a_V2[0]), (4, q4a_P2[0]), color = 'darkgreen', s = 4)

print('\n***** \nQuestion 4a: ')
print('No, this process does not represent any of the simple processes' + 
      ' which we have studied...')
print('It could only be adiabatic. Lets explore this: ')

adiabatic_constant(q4a_Volumes, q4a_Pressures, 3)
adiabatic_constant(q4a_Volumes, q4a_Pressures, 5)
adiabatic_constant(q4a_Volumes, q4a_Pressures, 7)

plt.show()

##### Question 4b #####
## Could this process in the PVT chart have occured in a container with a 
## free moving pistion. 

print('\n***** \nQuestion 4b ')
print('For this to have occured in a container with a free moving piston' + 
      ' it must obey the ideal gas law.')
print('Which is to say that the change in PV must be proportional to the ' +
      'change in T, which is also proportional to change in U')

q3b_dPV = (q4a_V2[0]*q4a_P2[0])/(q4a_V1[0]*q4a_P1[0])

print('Proportion of initial PV: ' + str(q3b_dPV) + ' * ' 
      + 'PV_initial = PV_final')
print('\nThis should be proportional to change in energy, since energy is ' +
      'proportional to temperature.')
th.dU(q4a_Volumes, q4a_Pressures, 3, 1)

##### Question 5a #####
## Given a PV graph, compare the energy exchange via heating during 
## process B and D (process D is on the left,  process B is on the right)
fig, ax = plt.subplots()
fig.set_size_inches(6, 5)
fig.suptitle('Thermo: Exam 1 \nQuestion 5')

q5a_isobaric_Volumes01 = [2, 4]
q5a_isobaric_Pressures01 = [7/2, 7/2]
th.isobaric_plot(ax, q5a_isobaric_Volumes01, q5a_isobaric_Pressures01)

q5a_isobaric_Volumes02 = [9/2, 3/2]
q5a_isobaric_Pressures02 = [3/2, 3/2]
th.isobaric_plot(ax, q5a_isobaric_Volumes02, q5a_isobaric_Pressures02)

q5a_linear_Volumes01 = [4, 9/2]
q5a_linear_Pressures01 = [7/2, 3/2]
th.linear_plot(ax, q5a_linear_Volumes01, q5a_linear_Pressures01, 
               clr = 'darkblue')

q5a_linear_Volumes02 = [3/2, 2]
q5a_linear_Pressures02 = [3/2, 7/2]
th.linear_plot(ax, q5a_linear_Volumes02, q5a_linear_Pressures02, 
               clr = 'darkblue')

ax.set_ylim(0, 5)
ax.set_xlim(0, 6)

print('Process B: ')
th.linear_heating(q5a_linear_Volumes01, q5a_linear_Pressures01, 5, 4)
print('Process D: ')
th.linear_heating(q5a_linear_Volumes02, q5a_linear_Pressures02, 5, 4)

plt.show()