#!/usr/bin/env python3
"""plot_ellipse.py"""

from pathlib import Path

import numpy as np 
import matplotlib.pyplot as plt

# equation of ellipse at (0,0) with major axis length 100 (hor.) and minor axis length vertical 50
# is x^2/50^2+y^2/25^2=1 converted into polar form is r=1250/sqrt((50cos(theta))^2+(25sin(theta))^2)

def plot(ax):
    theta = np.linspace(0, 2 * np.pi, 1000)
    radius = 1250/np.sqrt((50*np.cos(theta))**2+(25*np.sin(theta))**2)
    # A point P on the perimeter of the ellipse has coords (r,theta) or (x,y) where
    x1 = radius * np.cos(theta)
    y1 = radius * np.sin(theta)
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")
    ax.set_title(f"$x^2/a^2 + y^2/b^2 = 1; a=50, b=25$")
    ax.set_xlim(-60, 60)
    ax.set_ylim(-30, 30)
    ax.set_aspect("equal")
    ax.grid("on")
    ax.plot(y1,x1)

def main():
    plt.figure(Path(__file__).name)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
