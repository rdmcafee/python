# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 12:10:52 2021

@author: Mcrye
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
t0 = 0
s = a0 * np.sin(2 * np.pi * f0 * t - t0)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
l, = plt.plot(t, s, lw=2)

slider_bkd_color = 'lightgoldenrodyellow'
ax_freq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=slider_bkd_color)
ax_amp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=slider_bkd_color)
ax_time = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=slider_bkd_color)

# define the values to use for snapping
allowed_amplitudes = np.concatenate([np.linspace(.1, 5, 100), [6, 7, 8, 9]])

# create the sliders
samp = Slider(
    ax_amp, "Amp", 0.1, 9.0,
    valinit=a0, valstep=allowed_amplitudes.any(),
    color="green"
)

sfreq = Slider(
    ax_freq, "Freq", 0, 10*np.pi,
    valinit=2*np.pi, valstep=np.pi,
    color="green"  # Remove the line marking the valinit position.
)

stime = Slider(
    ax_time, "Time", 0, 20, 
    valinit = t0, valstep = 0.2,
    color="green"
)


def update(val):
    amp = samp.val
    freq = sfreq.val
    time = stime.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t-time))
    fig.canvas.draw_idle()


sfreq.on_changed(update)
samp.on_changed(update)
stime.on_changed(update)

ax_reset = plt.axes([0.8, 0.0008, 0.1, 0.04])
button = Button(ax_reset, 'Reset', color=slider_bkd_color, hovercolor='0.975')


def reset(event):
    sfreq.reset()
    samp.reset()
    stime.reset()
button.on_clicked(reset)


plt.show()