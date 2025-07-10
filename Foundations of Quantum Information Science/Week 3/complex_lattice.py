"""complex_lattice.py"""

# Reference: https://en.wikipedia.org/wiki/Gaussian_integer

# Reference: Gemini AI, modified some code myself to meet parameters

import matplotlib.pyplot as plt
import numpy as np
from z3 import *

#Gaussian Integers x+yi where x,y are integers

#Since the hint gave us the real and imaginary parts of f(z) we can solve these inequalities to obtain the integers x,y
# thus complex numbers z=x+yi that 
# Need to solve simultanenous inequalities for (x,y) such that x^2-y^2-y+1<=10 and (2xy+x)<=10

# Lets visualize the solution set first to the system of inequalities 

from matplotlib.lines import Line2D # For custom legend

# Define the inequalities
def ineq1_func(x, y):
    return x**2 - y**2 - y + 1 <= 10

def ineq2_func(x, y):
    return 2*x*y + x <= 10

# Create a grid of x and y values
# We choose a range that is likely to show the interesting parts of the feasible region.
# You might need to adjust this based on the specific inequalities.
x = np.linspace(-50, 50, 400) # Increased range for x
y = np.linspace(-50, 50, 400) # Increased range for y
X, Y = np.meshgrid(x, y)

# Evaluate the inequalities on the grid
Z1 = ineq1_func(X, Y)
Z2 = ineq2_func(X, Y)

# Find the feasible region where both inequalities are true
feasible_region = Z1 & Z2

plt.figure(figsize=(10, 8))

# Plot the feasible region (shaded area)
# `imshow` works by coloring cells where `feasible_region` is True
plt.imshow(feasible_region, extent=[x.min(), x.max(), y.min(), y.max()],
           origin='lower', cmap='Greys', alpha=0.3)

# Plot the boundary lines of the inequalities (as contours)
# We plot the equality case for visualization
# For x^2 - y^2 - y + 1 = 10  => x^2 - y^2 - y - 9 = 0
plt.contour(X, Y, X**2 - Y**2 - Y - 9, levels=[0], colors='blue',
            linestyles='--', linewidths=1.5) # Removed label here as it's not used by contour

# For 2xy + x = 10
plt.contour(X, Y, 2*X*Y + X - 10, levels=[0], colors='red',
            linestyles='--', linewidths=1.5) # Removed label here as it's not used by contour

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Feasible Region for Non-Linear Inequalities')
plt.grid(True, linestyle=':', alpha=0.6)

# Create custom legends as `contour` doesn't automatically add them with the `label` argument
custom_lines = [Line2D([0], [0], color='blue', lw=1.5, linestyle='--'),
                Line2D([0], [0], color='red', lw=1.5, linestyle='--'),
                Line2D([0], [0], color='grey', lw=8, alpha=0.3)]
plt.legend(custom_lines, [r'$x^2 - y^2 - y + 1 = 10$', r'$2xy + x = 10$', 'Feasible Region'])

plt.xlim(x.min(), x.max())
plt.ylim(y.min(), y.max())
plt.gca().set_aspect('equal', adjustable='box') # Keep aspect ratio for better visualization

plt.show()


#We can conclude there are infinitely many solutions to these inequalties and the solution set is unbounded.
#It's impossible to enumerate all integers solutions to this set of inequalties 

#------------------------------------------------------------------------------------------------


# Define the complex function
def f(z):
    """
    Complex function: f(z) = z^2 + i*z + 1
    """
    return z**2 + 1j * z + 1

# Define the input domain (a grid of complex numbers for z)
# Let's keep the original input domain for z
x_min, x_max = -2.5, 2.5
y_min, y_max = -2.5, 2.5
num_points = 200 # Number of points along each dimension

x = np.linspace(x_min, x_max, num_points)
y = np.linspace(y_min, y_max, num_points)
X, Y = np.meshgrid(x, y)
Z_complex = X + 1j * Y

# Compute the function values
W = f(Z_complex)

# Apply the restrictions to the OUTPUT of the function (W)
# Real part of f(z) should be less than 4
# Imaginary part of f(z) should be less than 2
mask = (np.abs(W.real) < 4) & (np.abs(W.imag) < 2)

# Apply the mask to W.real and W.imag
W_real_filtered = W.real[mask]
W_imag_filtered = W.imag[mask]

# Flatten the filtered arrays for the scatter plot
W_real_flat = W_real_filtered.flatten()
W_imag_flat = W_imag_filtered.flatten()

# Create the scatter plot
plt.figure(figsize=(10, 10)) # Make the figure square for better aspect ratio
plt.scatter(W_real_flat, W_imag_flat, s=5, alpha=0.3, color='purple') # Reduced size and increased transparency for density

plt.xlabel('Re(f(z))')
plt.ylabel('Im(f(z))')
plt.title(r'Scatter Plot of $f(z) = z^2 + i z + 1$ with Restrictions')
plt.suptitle(r'Re($f(z)$) < 4 and Im($f(z)$) < 2', fontsize=12) # Adding suptitle for the restrictions

plt.axvline(0, color='gray', linestyle='--', alpha=0.6)
plt.axhline(0, color='gray', linestyle='--', alpha=0.6)
plt.grid(True, linestyle=':', alpha=0.4)
plt.axis('equal') # Important: Ensures the real and imaginary axes have the same scale

# Adjust limits to fit the filtered data, or set fixed limits to clearly show the restriction boundaries
plt.xlim(W_real_flat.min() - 0.5, 4.0) # Max limit for real part is 4
plt.ylim(W_imag_flat.min() - 0.5, 2.0) # Max limit for imaginary part is 2

plt.savefig('restricted_complex_function_scatter.png')
print("The plot 'restricted_complex_function_scatter.png' has been generated with the specified restrictions.")

