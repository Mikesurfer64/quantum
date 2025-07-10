#!/usr/bin/env python3
"""sphere_sampling.py"""

#Reference: tutorial via gemini ai, edited code too from Dr. Biersach;s file. 

#Fix code so that the points on the spehere are uniformly distributed

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Create random samples within the sphere
n = 15000
u = np.random.uniform(-1,1, n)   # poloidal angle
v = np.random.uniform(0,2 * np.pi, n)  # toroidal angle
phi = np.arccos(u)
phi2 = v

# Spherical to Cartesian coordinate conversion, periodicity of sin/cos causes clustering at antipodal of the sphere
x = np.sin(phi) * np.cos(phi2)
y = np.sin(phi) * np.sin(phi2)
z = np.cos(phi)

plt.figure(Path(__file__).name, figsize=(10, 8))
ax = plt.axes(projection="3d")
ax.view_init(azim=-72, elev=48)
ax.scatter(x, y, -1 * z, s=0.5)
ax.set_title("Uniform Sphere Surface Sampling")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_aspect("equal")
plt.tight_layout()
plt.show()
