#!/usr/bin/env python3
"""plot_unknown_wave.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

alpha = 7
beta = 13

t = np.linspace(0, 2 * np.pi, 1000)
y = 2*np.sin(7*t)*np.cos(13*t)

plt.figure(Path(__file__).name)
plt.title("QIS101 Task 14-01: Unknown Wave")
plt.plot(t, y, lw=2)
plt.grid("on")
plt.show()
