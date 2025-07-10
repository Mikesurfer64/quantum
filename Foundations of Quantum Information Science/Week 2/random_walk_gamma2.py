
# The following code was given by Gemini AI, I needed to modify the code slightly
# for the python code to run. Works for any fixed dim [1,25]
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma

def expected_final_distance(dims, num_steps):
    """
    Calculates the expected final distance for a uniform random walk
    based on a theoretical formula.
    """
    return np.sqrt((2 * num_steps)/ dims) * (gamma((dims + 1) / 2) / gamma(dims / 2))**2

def fit_linear(x, y):
    """
    Returns the slope (m) and y-intercept (b) of the line
    that passes through (x, y) data values with least error
    """
    n = len(x)
    # Ensure inputs are float to prevent integer division issues
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    m = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / \
        (n * np.sum(x**2) - np.sum(x)**2)
    b = (np.sum(y) - m * np.sum(x)) / n
    return m, b

def main():

    num_points = 100
    # Values for dimensions to plot against in the second subplot
    dimensions_for_plot = np.linspace(1, 25, num_points)

    # Walks increase in length from 1 to max_steps for the first plot
    max_steps = 20_000

    # Number of times a walk of each length is repeated to find its average
    # NOTE: This parameter is not used in the theoretical `expected_final_distance` function.
    # If you intend to simulate random walks, you would need to implement that logic.
    num_walks = 50_000

    print("This may take up to 30 seconds . . .")

    # --- Plotting Expected Distance vs. Number of Steps (for a fixed dimension) ---
    # Let's choose a single dimension for this plot, e.g., 1 dimension
    fixed_dim = 1
    steps_for_plot = np.arange(1, max_steps + 1) # Steps from 1 to max_steps

    # Calculate expected distances for varying steps at a fixed dimension
    distances_steps_fixed_dim = np.array([expected_final_distance(fixed_dim, s) for s in steps_for_plot])
    distances_squared_steps_fixed_dim = distances_steps_fixed_dim**2

    # Fit a linear line to (steps, distances_squared)
    m, b = fit_linear(steps_for_plot, distances_squared_steps_fixed_dim)
    print(f"Slope of line (for fixed_dim={fixed_dim}) = {m:.4f}")
    print(f"Expected_final_distance(dims, num_steps)

    plt.figure(Path(__file__).name, figsize=(14, 6)) # Increased figure size

    ax1 = plt.subplot(1, 2, 1)
    ax1.plot(steps_for_plot, distances_steps_fixed_dim)
    ax1.set_title(f"Expected Final Distance vs. Steps ({fixed_dim}-D Unit Lattice)")
    ax1.set_xlabel("Number of Steps")
    ax1.set_ylabel("Expected Final Distance")
    ax1.grid(True)

    ax2 = plt.subplot(1, 2, 2)
    ax2.plot(steps_for_plot, distances_squared_steps_fixed_dim, color="green", zorder=3, label="Expected Final Distance Squared")
    ax2.plot(steps_for_plot, m * steps_for_plot + b, color="red", linewidth=3, label=f"Linear Fit (Slope={m:.4f})")
    ax2.set_title(rf"$(Expected\;Final\;Distance)^2$ vs. Steps ({fixed_dim}-D)")
    ax2.set_xlabel("Number of Steps")
    ax2.set_ylabel(r"$(Expected\;Final\;Distance)^2$")
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout() # Adjust layout to prevent overlap
    plt.show()

    # --- Optional: Plotting Expected Distance vs. Dimensions (for a fixed number of steps) ---
    # If you want to see how the expected distance changes with dimensions,
    # you would fix the number of steps and vary the dimensions.
    # For example, let's pick max_steps as the fixed number of steps.
    #
    # distances_dims_fixed_steps = np.array([expected_final_distance(d, max_steps) for d in dimensions_for_plot])
    #
    # plt.figure("Expected Distance vs. Dimensions", figsize=(8, 6))
    # plt.plot(dimensions_for_plot, distances_dims_fixed_steps)
    # plt.set_title(f"Expected Final Distance vs. Dimensions (Steps={max_steps})")
    # plt.set_xlabel("Number of Dimensions")
    # plt.set_ylabel("Expected Final Distance")
    # plt.grid(True)
    # plt.show()


if __name__ == "__main__":
    main()