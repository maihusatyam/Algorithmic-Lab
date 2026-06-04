import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial parameters
r0 = 3.9
x0 = 0.5

# Generate logistic map values
def logistic_map(r, x0, iterations=100):
    values = []
    x = x0
    for _ in range(iterations):
        x = r * x * (1 - x)
        values.append(x)
    return values

# Create figure
fig, ax = plt.subplots()

# Leave room for sliders
plt.subplots_adjust(bottom=0.25)

# Initial plot
values = logistic_map(r0, x0)
line, = ax.plot(values, color='cyan')

# Dark theme
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_title("Logistic Map Explorer", color='gold')
ax.set_xlabel("Iteration", color='white')
ax.set_ylabel("x", color='white')

ax.tick_params(colors='white')
ax.grid(color='gray')

# Slider positions
ax_r = plt.axes([0.2, 0.12, 0.6, 0.03])
ax_x = plt.axes([0.2, 0.06, 0.6, 0.03])

# Create sliders
r_slider = Slider(
    ax=ax_r,
    label='r',
    valmin=0,
    valmax=4,
    valinit=r0
)

x_slider = Slider(
    ax=ax_x,
    label='x₀',
    valmin=0.01,
    valmax=0.99,
    valinit=x0
)

# Update graph when slider changes
def update(val):

    r = r_slider.val
    x0 = x_slider.val

    values = logistic_map(r, x0)

    line.set_ydata(values)

    fig.canvas.draw_idle()

# Connect sliders
r_slider.on_changed(update)
x_slider.on_changed(update)

plt.show()
