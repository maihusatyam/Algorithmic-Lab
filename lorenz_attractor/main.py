import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Lorenz system constants
a = 10
b = 8/3
r = 28

# Initial coordinates
x = 1
y = 1
z = 1

# Small timestep
dt = 0.01

# Lists to store trajectory points
xs = []
ys = []
zs = []

# Lorenz differential equations
def lorenz(x, y, z):

    # Rate of change of x
    dx = a * (y - x)

    # Rate of change of y
    dy = x * (r - z) - y

    # Rate of change of z
    dz = x * y - b * z

    return dx, dy, dz

# Create figure window
fig = plt.figure()

# Create 3D graph
ax = fig.add_subplot(111, projection='3d')

# Set fixed axis limits
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_zlim(0, 60)

# Theme
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.grid(color='gray', linestyle='--')

# Create empty line for trajectory
line, = ax.plot([], [], [], lw=0.5, color='yellow')

# Animation update function
def update(frame):

    global x, y, z

    # Calculate derivatives
    dx, dy, dz = lorenz(x, y, z)

    # Update coordinates
    x += dx * dt
    y += dy * dt
    z += dz * dt

    # Store trajectory points
    xs.append(x)
    ys.append(y)
    zs.append(z)

    # Update x and y data
    line.set_data(xs, ys)

    # Update z data
    line.set_3d_properties(zs)

    return line,

# Create animation
ani = FuncAnimation(
    fig,
    update,
    frames=10000,
    interval=10
)

# Show graph window
plt.show()
