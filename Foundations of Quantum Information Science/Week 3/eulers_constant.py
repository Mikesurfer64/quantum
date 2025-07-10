"""eulers_constant.py"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from typing import Union
from numba import njit

# Reference: https://en.wikipedia.org/wiki/Euler%27s_constant

# Reference: https://en.wikipedia.org/wiki/Harmonic_number

# compute Euler's constant using numpy and scipy, referenced Gemini AI for some of code error corrections

# Do note my code does not specifically calculate upto 15 sig figs since the number of terms to reach 15 sig figs is quite large and exponential computational time
# as mentioned in class there's a different integral one could take to speed this up

@njit

def integrand(x):
    return -1*np.log(np.log(1/x))
                  
I = gamma = quad(integrand,0,1)

print(I)

euler_gamma = 0.57721566490153286060651209008240243104215933593992

#computation complete

def h(x):
    return np.log(x)+euler_gamma

# Begin plot of sum(1/n)=g(n) Harmonic Number function for n in N and gamma+ln(x) on the same 

def harmonic_numbers(n: Union[int, float]) -> float:
   """
    Calculates the value of the harmonic function sum(g(n)) = 1/n from 1 to n=50 

    Args:
        n (int or float): The input value for which to calculate 1/n.

    Returns:
        float: The reciprocal of n.

    Raises:
        TypeError: If n is not a number.
        ValueError: If n is zero, as division by zero is undefined.
        """
   sum=0
   for k in range (1,n+1):
        sum +=1/k
   return sum


print("\n--- Graphing Harmonic Numbers ---")

def plot_functions(ax, label_text_harmonic="\sum(1/n) (Harmonic Numbers)", label_text_approx="ln(x) + Gamma Approximation"):
    """
    Plots the harmonic Number Function and its approximation (ln(x) + gamma).

    Args:
        ax (matplotlib.axes.Axes): The axes object to plot on.
        label_text_harmonic (str): Label for the harmonic function curve.
        label_text_approx (str): Label for the approximation curve.
    """
    # For 1/n, we should ideally plot for integer n
    n_values_discrete = np.arange(1, 50, 1) # n from 1 to 50 for harmonic series
    harmonic_values = [harmonic_numbers(val) for val in n_values_discrete]

    # For the continuous approximation, use a denser linspace
    x_values_continuous = np.linspace(0.1, 50, 500) # Start from > 0 for log(x)

    ax.step(n_values_discrete, harmonic_values, color='blue', linestyle='-', label='Data Changes (Step Plot)')

    ax.plot(x_values_continuous, h(x_values_continuous), lw=2, color="red", label=label_text_approx)

    ax.set_title("Harmonic Numbers $sum(1/n)$ and Approximation $\ln(x) + \gamma$")
    ax.set_xlabel("n / x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid(True) # Use True for boolean grid instead of "on"

def main():
    fig_name = "Harmonic Numbers sum(1/n) and gamma+ln(x)"

    plt.figure(fig_name, figsize=(9, 6))

    ax = plt.axes() # Get the axes object once

    plot_functions(ax) # Call the plotting function with the axes object

    plt.show()

if __name__ == "__main__":
    main()