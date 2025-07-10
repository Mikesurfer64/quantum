#!/usr/bin/env python3
#used gemini AI to assist me in writing the code and debugging
"""plot_limits.py"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

def plot(ax):
    #Subdivide [-1,1]=[-1,0)U[0,.5]U(.5,1] into three subintervals
    x1 = np.linspace(-1,0)
    x2 = np.linspace(0,.5)
    x3 = np.linspace(.5,1)

    #glue together three subintervals
    
    x=np.concatenate((x1, x2, x3))

    def y1(x):
        return np.where(x == 0, np.nan,(12*((x-np.sin(x))/(np.power(x,3)))))

    def y2(x):
        return np.where(x == 0, np.nan,((np.power(np.e,x)-np.power(np.e,-x)-2)/(x-np.sin(x))))
    
    y_values_1 = y1(x)

    y_values_2 = y2(x)
 
    ax.plot(x, y_values_1, color="green", label=r"$12 \frac{x-\sin(x)}{x^3}$")
    ax.plot(x, y_values_2, color="blue", label=r"$\frac{e^x-e^{-x}-2}{x-\sin(x)}$")

    ax.set_title("Plot of Functions $y_1(x)$ and $y_2(x)$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-100,100 )
    ax.grid(True) # Changed from "on" to True for clarity
    ax.legend() # Show the labels

    # middle 6 x-values are found by sub-dividing [-1,1]. Length =2 divide by 5 to obtain increment of .4. Starting at -1,-.6,.-2,.2,.6,1 yields
    #6 values over 5 subintervals. Lets take the middle of each subinterval -.8,-.4,0 (undefined at 0),.4,.8

    breakpoints = np.linspace(-1, 1, 5)
    print(f"Breakpoints: {breakpoints}")

    # Evaluate y1 and y2 at the breakpoints
    y_values_1_at_breakpoints = y1(breakpoints)
    y_values_2_at_breakpoints = y2(breakpoints)

    print(f"\nEvaluating y1 at breakpoints:")
    for i, bp in enumerate(breakpoints):
        print(f"  y1({bp:.2f}) = {y_values_1_at_breakpoints[i]:.4f}")

    print(f"\nEvaluating y2 at breakpoints:")
    for i, bp in enumerate(breakpoints):
        print(f"  y2({bp:.2f}) = {y_values_2_at_breakpoints[i]:.4f}")




def main():
    fig = plt.figure(Path(__file__).name)
    ax = fig.add_subplot(111) # Add a subplot to the figure
    plot(ax)
    plt.show()

if __name__ == "__main__":
    main()

