import numpy as np
import matplotlib.pyplot as plt

# Define the function to calculate the Mandelbrot set
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Define the function to generate the Mandelbrot set image
def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

# Set parameters for the Mandelbrot set image
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 800, 600
max_iter = 256

# Generate the Mandelbrot set image
r1, r2, n3 = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)

# Plot the image using matplotlib
plt.figure(dpi=100)
plt.imshow(n3.T, extent=[xmin, xmax, ymin, ymax], cmap='hot', interpolation='bilinear')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
