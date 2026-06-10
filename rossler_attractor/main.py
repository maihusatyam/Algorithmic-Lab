import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Rössler parameters
a = 0.2
b = 0.2
c = 5.7

# Initial point
x = 1
y = 1
z = 1

# Time step
dt = 0.01

# Trajectory points
xs = []
ys = []
zs = []

# Rössler system
def rossler(x, y, z):

    dx = -y - z
    dy = x + a * y
    dz = b + z * (x - c)

    return dx, dy, dz

# Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Dark theme
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Axis colors
ax.tick_params(colors='yellow')

# Grid
ax.grid(color='gray', linestyle='--', alpha=0.3)

# Labels
ax.set_title("Rössler Attractor", color='gold')
ax.set_xlabel("X", color='yellow')
ax.set_ylabel("Y", color='yellow')
ax.set_zlabel("Z", color='yellow')

# Axis limits
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_zlim(0, 30)

# Empty line
line, = ax.plot([], [], [], lw=0.7, color='cyan')

# Animation update
def update(frame):

    global x, y, z

    # Compute derivatives
    dx, dy, dz = rossler(x, y, z)

    # Euler integration
    x += dx * dt
    y += dy * dt
    z += dz * dt

    # Store points
    xs.append(x)
    ys.append(y)
    zs.append(z)

    # Update trajectory
    line.set_data(xs, ys)
    line.set_3d_properties(zs)

    return line,

# Create animation
ani = FuncAnimation(
    fig,
    update,
    frames=10000,
    interval=10,
    blit=False
)

# Show plot
plt.show()
