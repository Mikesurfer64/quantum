"""arichmedes_spiral.py"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import pandas as pd

# Reference gemini AI and prior python graphing examples in the QIS course

#We define the base case where r=theta though generally there are many different Archimedes spirals one could create. 

# reference https://en.wikipedia.org/wiki/Archimedean_spiral

def r(theta):
    return theta

theta = np.linspace(0, 8*np.pi, 100)

# (Optional) Data Table for (r,theta) where  r = theta (Archimedes Spiral)

polar_table = np.vstack((r(theta), theta)).T # Transpose to get columns of (r, theta)

print("--- R, Theta Table for a Circle (first 5 rows) ---")
print(polar_table[:5])
print("...")
print(polar_table[-5:])

# (Optional) End Data table for r=theta

# Generally, Archimedes spiral is any spiral in the form r= a + b(theta)^(1/c), let a=0 ,b=1, c=1 

# --- 1. Define the Archimedes Spiral parameters ---
a = 0  # Starting radius (at theta=0)
b = 1 # Controls the spacing between turns (distance = 2*pi*b)

# --- 2. Define the polar equation of the spiral ---
def r_archimedes(theta, a_val, b_val):
    return a_val + b_val * theta

# --- 3. Calculate the derivative dr/d(theta) ---
# For r = a + b*theta, dr/d(theta) is simply b
def dr_dtheta_archimedes(theta, b_val):
    return b_val # This is constant for an Archimedes spiral

# --- 4. Define the integrand for the arc length formula ---
def integrand_arc_length(theta, a_val, b_val):
    r = r_archimedes(theta, a_val, b_val)
    dr_dtheta = dr_dtheta_archimedes(theta, b_val)
    return np.sqrt(r**2 + dr_dtheta**2)

# --- 5. Define the integration limits ---
theta_start = 0.0
theta_end = 8.0 * np.pi # Four full turns
num_table_points = 20 # Number of points to display in the table

# Create an array of theta values for which we want to calculate the arc length
theta_for_table = np.linspace(theta_start, theta_end, num_table_points)

# --- 6. Calculate arc length for each theta in the table ---
arc_lengths = []
for current_theta_end in theta_for_table:
    arc_length, _ = integrate.quad(
        integrand_arc_length,
        theta_start, # Always integrate from the absolute start
        current_theta_end,
        args=(a, b)
    )
    arc_lengths.append(arc_length)

# --- 7. Display the arc length table ---
# Using Pandas DataFrame for a clean, readable table output
arc_length_data = {
    'Theta (radians)': theta_for_table,
    'Theta (degrees)': np.degrees(theta_for_table),
    'Arc Length (L)': arc_lengths
}
df_arc_length = pd.DataFrame(arc_length_data)

print(f"--- Arc Length Table for Archimedes Spiral (a={a}, b={b}) ---")
print(df_arc_length.to_string(index=False, float_format="%.4f")) # .to_string to show all rows, .float_format for readability

# --- 6. Calculate the arc length using scipy.integrate.quad ---
# quad returns (integral_value, absolute_error)
arc_length, abs_error = integrate.quad(
    integrand_arc_length,
    theta_start,
    theta_end,
    args=(a, b) # Pass 'a' and 'b' parameters to the integrand
)

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={'projection': 'polar'})

# Plotting the spiral
ax.plot(theta, r(theta), color='red', lw=2)
ax.set_title('Polar Plot: Archimedes Spiral (r = theta)')
ax.set_rticks([0,4,8,12,16,20,24,28]) # Radial ticks

plt.tight_layout()
plt.show()