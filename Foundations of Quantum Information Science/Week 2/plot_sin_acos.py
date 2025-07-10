#!/usr/bin/env python3
"""plot_polynomial.py"""

from pathlib import Path

from matplotlib import markers
from matplotlib.pylab import arccos
import matplotlib.pyplot as plt
import numpy as np

def plot(ax):
    x1 = np.linspace(-1,1, 400)
    y1 = -np.sqrt(1-x1**2)

    ax.plot(x1, y1, color='blue', linewidth=2, label=r'$y = -\sqrt{1 - x^2}$')

    # Set the graph title to the polynomial expressed in LaTeX format
    
    y2 = np.sin(arccos(x1))
    
    ax.plot(x1, y2, color='green', linewidth=2, label=r'$y = -\sqrt{1 - x^2}$')
   #circle of radius one
    theta = np.linspace(0,2*np.pi, 36)
    x3 = np.cos(theta)
    y3 = np.sin(theta)
    ax.scatter(x3, y3, color = "black", marker = "o", s = 100, label='Solid Black Circles (c="black")')
    ax.grid("on")

def main():
    plt.figure(Path(__file__).name)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()
