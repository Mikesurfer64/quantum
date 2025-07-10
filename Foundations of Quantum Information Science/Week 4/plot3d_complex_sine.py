import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Reference: Gemini AI, code edited by me

# Define the complex function (e.g., f(z) = abs(sin(z))
def f(z):
    return abs(np.sin(z))

# Create a meshgrid for the complex input z = x + iy
# Define the range for x (real part) and y (imaginary part)
x = np.linspace(-2.5, 2.5, 50)
y = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x, y)

# Create the complex variable Z
Z_complex = X + 1j * Y

# Calculate the function output
W = f(Z_complex)

# Plot the magnitude (|W|) as the Z-axis for the 3D surface
Z_magnitude = np.abs(W)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z_magnitude, cmap='plasma', edgecolor='none')

ax.set_xlabel('Re(z)')
ax.set_ylabel('Im(z)')
ax.set_zlabel('|f(z)|')
ax.set_title(r'Magnitude Plot of $f(z) = z^2$')
fig.colorbar(surf, shrink=0.5, aspect=5, label='|f(z)|')
plt.show()