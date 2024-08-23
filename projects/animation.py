import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots()
xdata = np.linspace(0, 2 * np.pi, 1000)
ydata = np.sin(xdata)
line, = ax.plot(xdata, ydata)

# Function to update the plot
def update(frame):
    line.set_ydata(np.sin(xdata + frame / 10))  # Update the data.
    return line,

# Create the animation object
ani = FuncAnimation(fig, update, frames=range(100), blit=True)

# Display the animation
plt.show()
