#!/usr/bin/env python3
"""euler_curve.py"""

#Reference: gemini AI 

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# 1. Define the derivatives (the integrands)
def derivatives_func(t, state):
    """
    Returns [dx/dt, dy/dt] for the given t and state [x, y].
    For Euler's curve, dx/dt = cos(t^2) and dy/dt = sin(t^2).
    """
    dxdt = np.cos(t**2)
    dydt = np.sin(t**2)
    return [dxdt, dydt]

# 2. Set initial conditions and time span
t_initial = 0
t_final = 12.34
initial_state = [0, 0] # [x(0), y(0)]

# 3. Define the t values at which to evaluate the solution
t_eval = np.linspace(t_initial, t_final, 500) # More points for a smoother curve

# 4. Solve the ODE system
solution = solve_ivp(
    derivatives_func,
    (t_initial, t_final),
    initial_state,
    t_eval=t_eval,
    rtol=1e-6,
    atol=1e-9
)

# 5. Extract x and y values, and the corresponding t values
x_values = solution.y[0]
y_values = solution.y[1]
t_values = solution.t # In this case, t_values directly represents the arc length L(t)

# 6. Plot the Euler's Curve, colored by arc length (t_values)
plt.figure(figsize=(9, 8)) # Slightly larger figure to accommodate colorbar
scatter = plt.scatter(x_values, y_values, c=t_values, cmap='viridis', s=10,
                      label='Euler\'s Curve (Color by Arc Length)')

# Add a color bar
cbar = plt.colorbar(scatter)
cbar.set_label("Arc Length (t)")

plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.title("Euler's Curve with Arc Length Displayed")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box') # Ensures the spiral shape is accurate
plt.legend()
plt.show()

print("The Euler's curve is plotted, with its color varying along the curve to represent the arc length (t value) at each point.")