#!/usr/bin/env python3
"""plot3d_surface.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator


def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))


def main():
    x = np.linspace(-5, 5, 100) #plot -5,5 100 intervals
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y) #np.meshgrid() zero to hero, convenient (not an outer product), makes copies of x and y 1-1 matching to make a grid
    z = f(x, y) #passed into f, 100x100=10000 x values, 10000 y values

    plt.figure(Path(__file__).name)
    ax = plt.axes(projection="3d")

    surf = ax.plot_surface(x, y, z, cmap="coolwarm", lw=0, antialiased=False)
    plt.colorbar(surf, ax=ax, shrink=0.5)

    ax.zaxis.set_major_locator(LinearLocator(10)) #10 tick marks (only) spaced evenly
    ax.zaxis.set_major_formatter("{x:.02f}") #format the tick marks
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.show()


if __name__ == "__main__":
    main()
