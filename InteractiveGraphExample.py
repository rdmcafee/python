# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 19:38:26 2021

@author: Mcrye
"""

import numpy as np
import math as ma
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from tkinter import *
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from matplotlib.ticker import MultipleLocator
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

Root = Tk()
Root.title("Wave Analysis")
frame1 = Frame(Root)
frame1.pack(side = tk.BOTTOM)

frame4 = Frame(frame1)
frame4.pack(side = tk.LEFT)

frame2 = Frame(frame4)
frame2.pack(side = tk.LEFT)

frame3 = Frame(frame4)
frame3.pack(side = tk.RIGHT)

a = 1 
t = 0
phi = 0
#x = 0

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

#x = np.linspace(-1, ma.pi*3, 1000)
x = np.arange(-1, np.pi*3, 0.001)

l, = ax.plot(x, np.zeros_like(x), lw=1.5)

#y = a * np.sin(2 * np.pi * x - 2 * np.pi * t + phi)

  # creating the Tkinter canvas
    # containing the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master = Root)  
#canvas.draw()
  
    # placing the canvas on the Tkinter window
#canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
toolbar = NavigationToolbar2Tk(canvas, Root)
toolbar.update()
  
    # placing the toolbar on the Tkinter window
canvas.get_tk_widget().pack(fill = tk.BOTH)

#ax.relim()
#ax.autoscale_view()
#canvas.draw()
    
def Submit():
    """
    Update the plotted function to the new math *expression*.

    *expression* is a string using "t" as its independent variable, e.g.
    "t ** 3".
    """
    a = float(entA.get())
    t = float(entT.get())
    phi = float(entPhi.get())
    y = a * np.sin(2 * np.pi * x - 2 * np.pi * t + phi)
    print(a) # just to be sure a has taken the correct value
    #ydata = a * ma.sin(2 * ma.pi * x - 2 * ma.pi * t + phi)
    print(t)
    l.set_ydata(y)
    ax.relim()
    ax.autoscale_view()
    
    canvas.draw()
    
    #return a, t, phi

def Play(i):
    a = float(entA.get())
    t = float(entT.get())
    phi = float(entPhi.get())
    #y = a * np.sin(2 * np.pi * x - 2 * np.pi * (t+i) + phi)
    l.set_ydata(a * np.sin(2 * np.pi * x - 2 * np.pi * (t + i/50) + phi))
    ax.relim()
    ax.autoscale_view()
    canvas.get_tk_widget().pack(fill = tk.BOTH)
    canvas.draw()
    
    return l,

def playButtonPress():
    canvas.get_tk_widget().pack_forget()
    ani = animation.FuncAnimation(fig, Play, frames = 100, interval = 50, blit = True)
    
    
    
entA = tk.Entry(frame3)
entA.insert(0, "1")

entT = tk.Entry(frame3)
entT.insert(0, "0")

entPhi = tk.Entry(frame3)
entPhi.insert(0, "0")

labelA = tk.Label(frame2, text = "Enter Amplitude")
labelA.pack(fill = tk.Y, padx =  5, pady = 5)

labelT = tk.Label(frame2, text = "Enter Time")
labelT.pack(fill = tk.Y, padx =  5, pady = 5)

labelPhi = tk.Label(frame2, text = "Enter Phase [phi]")
labelPhi.pack(fill = tk.Y,  padx =  5, pady = 5)

entA.pack(fill = tk.Y, padx =  5, pady = 5)
entT.pack(fill = tk.Y, padx =  5, pady = 5)
entPhi.pack(fill = tk.Y, padx =  5, pady = 5)


process = tk.Button(master = frame1, height = 2, width = 5, text = "Execute", 
                    command = Submit)

animate =tk.Button(master = frame1, height = 2, width = 5, text = "Animate", 
                   command = playButtonPress)

process.pack(side = tk.RIGHT, fill = tk.Y, padx =  5, pady = 5)
animate.pack(side = tk.RIGHT)
#anim = FuncAnimation(fig, Play, interval = 50, blit = True)

   
"""
axboxA = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_boxa = TextBox(axboxA, "Amplitude")
text_boxa.set_val("1") 
text_boxa.on_submit(Submit)
 # Trigger `submit` with the initial string.

axboxT = fig.add_axes([0.2, 0.005, 0.8, 0.075])
text_boxt = TextBox(axboxT, "Time")
text_boxt.set_val("0")
text_boxt.on_submit(Submit) 

axboxPhi = fig.add_axes([0.5, -0.005, 0.8, 0.075])
text_boxphi = TextBox(axboxPhi, "Phi")
text_boxphi.set_val("0")
text_boxphi.on_submit(Submit)
"""

minorSpacing = ma.pi/4
majorSpacing = ma.pi
minorMarkings = MultipleLocator(minorSpacing)
majorMarkings = MultipleLocator(majorSpacing)
ax.xaxis.set_minor_locator(minorMarkings)
ax.yaxis.set_minor_locator(MultipleLocator(base = 0.5))

ax.xaxis.set_major_locator(majorMarkings)
ax.yaxis.set_major_locator(MultipleLocator(base = 1.0))
ax.grid(which = 'minor', alpha = 0.2)
ax.grid(which = 'major', alpha = 1)
#plt.show()

h = plt.ylabel('Y')
h.set_rotation(0)
plt.xlabel('X')

Root.mainloop()