
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# reference: https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution

#used gemini to assist in editing my code

# MBD (PDF):

def y(x,a):
    return np.sqrt((2/np.pi))*((np.power(x,2))/np.power(a,3))*np.power(np.e,(-x**2/(2*a**2)))


def plot(ax,a,curve_color,label_text):
    x = np.linspace(0, 20, 100)
    ax.plot(x, y(x,a), lw=2,color=curve_color,label=label_text)
    ax.set_title("Maxwell_Boltzmann Distribution")
    ax.set_xlabel("x")
    ax.set_ylabel("P(x)")
    ax.legend()
    ax.grid("on")


def main():
    fig_name = "Maxwell_Boltzmann_Comparison" # A more appropriate name for the figure
    
    plt.figure(fig_name, figsize=(9, 6))
    ax = plt.axes() # Get the axes object once

    # Plot for a = 1
    plot(ax, a=1, curve_color="springgreen", label_text="a = 1")

    # Plot for a = 2
    plot(ax, a=2, curve_color="cornflowerblue", label_text="a = 2")

    # Plot for a = 5
    plot(ax, a=5, curve_color="red", label_text="a = 5")

    plt.show()

if __name__ == "__main__":
    main()