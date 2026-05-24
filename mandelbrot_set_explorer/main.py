
import numpy as np
import matplotlib.pyplot as plt

# Image size
width = 800
height = 800

# Create empty image
image = np.zeros((height, width))

# Mandelbrot function
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        z = z**2 + c
        # Escape condition
        if abs(z) > 2:
            return n
    return max_iter

# Loop through every pixel
for x in range(width):
    for y in range(height):
        # Convert pixel -> complex number
        real = (x - width/2) * 4 / width
        imag = (y - height/2) * 4 / width
        c = complex(real, imag)
        # Store iteration count
        image[y, x] = mandelbrot(c, 100)

# Display fractal
plt.imshow(image, cmap='inferno')
plt.axis('off')
plt.show()
