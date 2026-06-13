import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Hénon parameters
a = 1.4
b = 0.3

# Initial point
x = 0.1
y = 0.1

# Store trajectory points
xs = []
ys = []

# Hénon map equations
def henon(x, y):

    x_next = 1 - a * x**2 + y
    y_next = b * x

    return x_next, y_next


# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Dark theme
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Title
ax.set_title(
    "Hénon Strange Attractor",
    color="gold",
    fontsize=16
)

# Axis labels
ax.set_xlabel("x", color="white")
ax.set_ylabel("y", color="white")

# Tick colors
ax.tick_params(colors="white")

# Grid
ax.grid(color="gray", alpha=0.2)

# Border colors
for spine in ax.spines.values():
    spine.set_color("gold")

# Fixed limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 0.5)

# Empty plot
line, = ax.plot(
    [],
    [],
    ".",
    markersize=1,
    color="cyan"
)

# Animation function
def update(frame):

    global x, y

    # Generate multiple points each frame
    for _ in range(50):

        x, y = henon(x, y)

        xs.append(x)
        ys.append(y)

    # Update plot
    line.set_data(xs, ys)

    return line,


# Create animation
ani = FuncAnimation(
    fig,
    update,
    frames=2000,
    interval=10,
    blit=True
)

# Show attractor
plt.show()
