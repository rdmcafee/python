import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 8)
ax.set_ylim(-2, 8)

# Initialize the dot as a point
dot1, = ax.plot([], [], 'ro')
dot2, = ax.plot([], [], 'bo')

# Function to initialize the animation (coordinates are two empty lists)
def init():
    dot1.set_data([], [])
    dot2.set_data([], [])
    return (dot1, dot2)

# Function to update the animation
# Note: should add a statement to handle when the objects interact [perfectly elastic]

def update(frame):

    x1 = 1 + 2*frame  # Update x1-coordinate
    y1 = 4 - 2*frame  # Update y1-coordinate

    x2 = 2 + 1*frame  # update x2-coordinate
    y2 = 1 + 1*frame  # update y2-coordinate

    if x1-x2 == 0 and y2-y1 == 0: 
        print("collision")
      
    else: 
        dot1.set_data(x1, y1)
        dot2.set_data(x2, y2)
        return(dot1, dot2)
    
    #return (dot1, dot2)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 4, 0.05), init_func=init, blit=True)

# Show the animation
plt.show()

