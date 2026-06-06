import numpy as np
import matplotlib.pyplot as plt

# Initial value
x0 = 0.5

# High resolution r values
r_values = np.linspace(2.5, 4.0, 10000)

# Lists to store points
r_plot = []
x_plot = []

# Generate bifurcation diagram
for r in r_values:

    x = x0

    # Remove transient behavior
    for _ in range(1000):
        x = r * x * (1 - x)

    # Store long-term behavior
    for _ in range(100):

        x = r * x * (1 - x)

        r_plot.append(r)
        x_plot.append(x)

# Create figure
fig, ax = plt.subplots(figsize=(12, 8))

# Dark theme
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Colored bifurcation diagram
scatter = ax.scatter(
    r_plot,
    x_plot,
    c=x_plot,
    cmap='plasma',
    s=0.01,
    alpha=0.8
)

# Titles and labels
ax.set_title(
    "Logistic Map Bifurcation Diagram",
    color='gold',
    fontsize=16
)

ax.set_xlabel(
    "Growth Parameter (r)",
    color='white',
    fontsize=12
)

ax.set_ylabel(
    "Long-Term Population (x)",
    color='white',
    fontsize=12
)

# Axis styling
ax.tick_params(colors='white')

for spine in ax.spines.values():
    spine.set_color('gold')

# Light grid
ax.grid(
    color='gray',
    alpha=0.2
)

# Color bar
cbar = plt.colorbar(scatter)
cbar.set_label("Population Value (x)")

# Show plot
plt.show()
