#!/usr/bin/env python3
"""plot3d_cylinder_.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

radius, height = 10, 50

u = np.linspace(0, height, 30)  # Vertical location
v = np.linspace(0, radius, 30)  # Horizontal circular slice

x = 10*np.cos(v)
y = 10*np.sin(v)
z = np.outer(u,1)

plt.figure(Path(__file__).name)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, z, color="red")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_xlim(-height, height)
ax.set_ylim(-height, height)
ax.set_zlim(0, height)
plt.show()
