import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Grid size
rows = 50
cols = 50

# Random initial grid
grid = np.random.randint(0, 2, (rows, cols))

# Create figure
fig, ax = plt.subplots()

# Dark theme
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Remove axis labels
ax.set_xticks([])
ax.set_yticks([])

# Display grid
img = ax.imshow(grid, cmap='viridis')

# Update function
def update(frame):
    global grid
    # Create next generation
    new_grid = grid.copy()
    # Check each cell (excluding borders)
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            # Get 3x3 neighborhood
            neighbors = grid[row-1:row+2, col-1:col+2]
            # Count living neighbors
            count = np.sum(neighbors) - grid[row, col]
            # Alive cell rules
            if grid[row, col] == 1:
                # Underpopulation
                if count < 2:
                    new_grid[row, col] = 0
                # Overpopulation
                elif count > 3:
                    new_grid[row, col] = 0
            # Dead cell rules
            else:
                # Reproduction
                if count == 3:
                    new_grid[row, col] = 1

    # Update grid
    grid = new_grid
    # Update image
    img.set_array(grid)
    return [img]

# Create animation
ani = FuncAnimation(
    fig,
    update,
    interval=100
)

# Show simulation
plt.show()
