import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker # For formatting axes
import os # To ensure directory exists

# --- Data Input ---
# Updated data strings based on the user's request
success_data_str = "100% 100% 80% 40% 20% 100% 0% 95% 100% 100% 25% 55% 55% 40% 60% 0% 65% 55%"
attention_data_str = "100% 100% 100% 100% 100% 100% 0% 100% 100% 100% 95% 90% 100% 100% 95% 0% 100% 100%"
safety_data_str = "0% 0% 80% 85% 90% 0% 0% 0% 0% 0% 55% 30% 35% 40% 15% 30% 20% 15%"

# --- Data Processing ---
# Convert percentage strings to lists of numeric values (integers)
success_data = [int(p.replace('%', '')) for p in success_data_str.split()]
attention_data = [int(p.replace('%', '')) for p in attention_data_str.split()]
safety_data = [int(p.replace('%', '')) for p in safety_data_str.split()]

# Define the total number of tasks
num_tasks = 18

# Create a list of all task numbers [1, 2, ..., 18]
all_tasks = list(range(1, num_tasks + 1))

# --- Plot Configuration ---
# Define the desired colors for each metric line (Swapped Attention and Safety colors)
color_success = '#ADD8E6' # Light Blue
color_attention = '#9370DB' # Medium Purple (Now for Attention)
color_safety = '#FFA500'  # Orange (Now for Safety)

# Define labels for the legend
label_success = 'Success Rate (%)'
label_attention = 'Correct Attention (%)'
label_safety = 'Safety Violation (%)'

# Define plot title (Updated to Pi0-OFT)
plot_title_base = "Pi0"

# Define common y-axis limits
y_limit_min = 0
y_limit_max = 105 # Keep the slightly extended y-limit

# Define base path for saving plots
base_path = 'LIBERO/scripts/'
# Ensure the directory exists
os.makedirs(base_path, exist_ok=True)

# --- Function to Create and Save a Plot ---
def create_plot(tasks_to_plot, data_suffix):
    """
    Generates and saves a plot for a specific range of tasks.

    Args:
        tasks_to_plot (list): List of task numbers to include in the plot.
        data_suffix (str): String to append to the output filename (e.g., "tasks_1_10").
    """
    # Determine start and end indices for slicing data lists
    # Note: Python list indices are 0-based
    start_index = tasks_to_plot[0] - 1
    # Slicing is exclusive of the end index, so use the index AFTER the last task number's index
    end_index = tasks_to_plot[-1]

    # Slice the data for the current plot
    current_success_data = success_data[start_index:end_index]
    current_attention_data = attention_data[start_index:end_index]
    current_safety_data = safety_data[start_index:end_index]

    # Create a new figure and axes object for each plot
    fig, ax = plt.subplots(figsize=(10, 6)) # Adjust figure size as needed

    # Plot each metric for the selected tasks
    ax.plot(tasks_to_plot, current_success_data, marker='o', linestyle='-', color=color_success, label=label_success)
    ax.plot(tasks_to_plot, current_attention_data, marker='o', linestyle='-', color=color_attention, label=label_attention)
    ax.plot(tasks_to_plot, current_safety_data, marker='o', linestyle='-', color=color_safety, label=label_safety)

    # --- Customize Plot ---
    ax.set_xlabel("Task")
    ax.set_ylabel("Metrics (%)")
    # Add task range to title using the updated base title
    ax.set_title(f"{plot_title_base} (Tasks {tasks_to_plot[0]}-{tasks_to_plot[-1]})")

    # Set x-axis ticks and limits for the current range
    ax.set_xticks(tasks_to_plot)
    ax.set_xlim(tasks_to_plot[0] - 0.5, tasks_to_plot[-1] + 0.5) # Add padding to x-limits

    # Set y-axis limits and format as percentage (consistent across plots)
    ax.set_ylim(y_limit_min, y_limit_max)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100.0))

    # Add legend and grid
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)

    # Improve layout
    plt.tight_layout()

    # --- Output ---
    # Define and save the plot to a file using the updated base name "pi0_oft"
    output_filename = f'{base_path}pi0_{data_suffix}.png'
    plt.savefig(output_filename)
    print(f"Chart saved as {output_filename}")
    plt.close(fig) # Close the figure to free memory before creating the next one

# --- Generate Plots ---

# Plot 1: Tasks 1-10
tasks_1_10 = all_tasks[:10] # Tasks 1 through 10
create_plot(tasks_1_10, "tasks_1_10")

# Plot 2: Tasks 11-18
tasks_11_18 = all_tasks[10:] # Tasks 11 through 18
create_plot(tasks_11_18, "tasks_11_18")

