import matplotlib.pyplot as plt
import numpy as np
import os # Import os module to handle directory creation

# Data extracted from the user query
x_coords = [-0.120, 0.100, -0.200, -1.500, 0.150]
y_coords = [-0.240, -0.200, -0.080, 0.060, 0.030]
weights = [50, 50, 50, 50, 50] # All points have a weight of 50

# Coordinates of the "main task" point (the first one)
main_task_x = x_coords[0]
main_task_y = y_coords[0]

# Determine the range for the plot for appropriate binning
x_min, x_max = min(x_coords) - 0.1, max(x_coords) + 0.1
y_min, y_max = min(y_coords) - 0.1, max(y_coords) + 0.1

# --- Plotting ---
plt.figure(figsize=(8, 6))

# 1. Create the heatmap using all points
# The heatmap shows the density/weight in bins. The color intensity in the bin
# containing the main_task point will reflect its weight (50).
h = plt.hist2d(x_coords, y_coords, bins=50, weights=weights, cmap='viridis', range=[[x_min, x_max], [y_min, y_max]])

# 2. Add the color bar for the heatmap
plt.colorbar(label='Weight')

# 3. Overlay the "main task" point using scatter
# Choose a distinct color (e.g., red), marker, and size. Add a label.
plt.scatter(main_task_x, main_task_y,
            color='red',        # A distinct color
            marker='*',         # A different marker shape
            s=150,              # Size of the marker
            edgecolor='black',  # Edge color for better visibility
            label='main task',  # Label for the legend
            zorder=3            # Ensure it's plotted on top
           )

# --- Labels and Appearance ---
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Distribution Heatmap')

# Set axis limits
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# Add grid
plt.grid(True, linestyle='--', alpha=0.6)

# 4. Add the legend to display the "main task" label
plt.legend()

# --- Saving the Plot ---
save_path = 'LIBERO/scripts/heatmap.png'
# Ensure the directory exists before saving
save_dir = os.path.dirname(save_path)
if save_dir: # Check if save_dir is not empty (i.e., not saving in CWD)
  os.makedirs(save_dir, exist_ok=True) # Create directory if it doesn't exist

# Save the figure
plt.savefig(save_path)

# Optionally, show the plot interactively as well
# plt.show()

print(f"Plot saved to: {os.path.abspath(save_path)}") # Print the absolute path where it was saved