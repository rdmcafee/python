# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 00:11:05 2022

@author: Mcrye

Offloading computational tasks to other programs making it reusable and 
easier to follow
"""
import Thermo.Processes as pr
import matplotlib.pyplot as plt
import numpy as np

def fig(size = (10, 6), title = 'Question #'):
    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.suptitle("Thermo: Exam 1 " + '\n' + title)
    
    major_xticks = np.arange(0, 6, 1)
    minor_xticks = np.arange(0, 6, 1/4)

    major_yticks = np.arange(0, 5, 1)
    minor_yticks = np.arange(0, 5, 1/2)
    
    ax.set_xticks(major_xticks)
    ax.set_xticks(minor_xticks, minor = True)
    ax.set_xticklabels([r'0', r'$1V_{0}$', r'$2V_{0}$', r'$3V_{0}$', 
                    r'$4V_{0}$', r'$5V_{0}$', r'$6V_{0}$'])

    ax.set_yticks(major_yticks)
    ax.set_yticks(minor_yticks, minor = True)
    ax.set_yticklabels([r'0', r'$1P_{0}$', r'$2P_{0}$', r'$3P_{0}$', 
                    r'$4P_{0}$'])

    ax.grid(which = 'major', color = 'k', alpha = 0.2)
    ax.grid(which = 'minor', color = 'k', alpha = 0.05)
    
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 5)
    return ax

ax = fig(size = (10, 6), title = 'Quesetion 3a')


##### Question 3a #####

q3a_Volumes = [4, 1]
q3a_Pressures = [1, 4]

def isothermal_process(xval):
    yval = 4/xval
    return yval

isothermal_Volumes = [3, 2]
isothermal_Pressures = [isothermal_process(isothermal_Volumes[0]), 
                        isothermal_process(isothermal_Volumes[1])]

ax.scatter(q3a_Volumes, q3a_Pressures, color = 'darkblue', 
           s = 20, alpha = 0.8)
ax.scatter(isothermal_Volumes, isothermal_Pressures, color = 'darkred', 
           s = 20, alpha = 0.2)

ax.text(4.1, 1, 'Y')
ax.text(1.1, 4, 'K')

pr.isothermal_plot(ax, q3a_Volumes, [q3a_Pressures[0]], 
                      clr = 'darkred')



plt.show()

##### Question 3b #####
## Graphing the isobaric + isochoric process
## Adding the graph of the isothermal process. 

ax = fig(size = (10, 6), title = 'Question 3b')

q3b_isobaric_Volumes = [4, 1]
q3b_isobaric_Pressures = [1, 1]

q3b_isochoric_Volumes = [1, 1]
q3b_isochoric_Pressures = [1, 4]

pr.isobaric_plot(ax, q3b_isobaric_Volumes, q3b_isobaric_Pressures, 
                 clr = 'darkgreen')
pr.isochoric_plot(ax, q3b_isochoric_Volumes, q3b_isochoric_Pressures, 
                  clr = 'darkgreen')
pr.isothermal_plot(ax, q3a_Volumes, [q3a_Pressures[0]], 
                      clr = 'darkred')
ax.text(4.1, 1, 'Y')
ax.text(1.1, 4, 'K')

plt.show()

##### Question 3c #####
## Graphing the linear process from Y to K
## Adding the graph of the isothermal process

ax = fig(size = (10, 6), title = 'Question 3c')

q3c_Volumes = [4, 1]
q3c_Pressures = [1, 4]

pr.isothermal_plot(ax, q3c_Volumes, [q3c_Pressures[0]], 
                      clr = 'darkred')
pr.linear_plot(ax, q3c_Volumes, q3c_Pressures, clr = 'darkgreen')

ax.text(4.1, 1, 'Y')
ax.text(1.1, 4, 'K')

plt.show()

##### Question 5a #####
## graph and label the process descrbed in the question

ax = fig(size = (10, 6), title = 'Question 5')

q5a_isobaric_Volumes01 = [2, 4]
q5a_isobaric_Pressures01 = [7/2, 7/2]
pr.isobaric_plot(ax, q5a_isobaric_Volumes01, q5a_isobaric_Pressures01)

q5a_isobaric_Volumes02 = [9/2, 3/2]
q5a_isobaric_Pressures02 = [3/2, 3/2]
pr.isobaric_plot(ax, q5a_isobaric_Volumes02, q5a_isobaric_Pressures02)

q5a_linear_Volumes01 = [4, 9/2]
q5a_linear_Pressures01 = [7/2, 3/2]
pr.linear_plot(ax, q5a_linear_Volumes01, q5a_linear_Pressures01, 
               clr = 'darkblue')

q5a_linear_Volumes02 = [3/2, 2]
q5a_linear_Pressures02 = [3/2, 7/2]
pr.linear_plot(ax, q5a_linear_Volumes02, q5a_linear_Pressures02, 
               clr = 'darkblue')

ax.text(1.9, 3.65, 'I')
ax.text(3, 3.6, 'A')
ax.text(4.1, 3.65, 'II')
ax.text(4.30, 2.5, 'B')
ax.text(3, 1.25, 'C')
ax.text(4.6, 1.25, 'III')
ax.text(1.4, 1.25, 'IV')
ax.text(1.6, 2.5, 'D')
plt.show()