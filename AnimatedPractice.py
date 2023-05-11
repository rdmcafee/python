# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 00:03:38 2021

@author: Mcrye
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
FPS = 30
plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x+i/50))  # update the data.
    #return line,
    return()


ani = FuncAnimation(fig, animate, interval=1000/FPS, 
                    blit=True)

# To save the animation, use e.g.
#
#ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()