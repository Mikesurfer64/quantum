
"""catalans_constant.py"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from typing import Union
import math
from numba import njit
from scipy.integrate import cumulative_simpson


#Reference: https://en.wikipedia.org/wiki/Catalan%27s_constant

# be patient for the script to run as n is large, thank you.

#used prior pyfiles from the course and my files from other assignments


def catalans(n: Union[int, float]) -> float:
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
   for k in range (0,n+1):
        sum +=np.power(-1,k)/np.power((2*k+1),2)
   return sum

print(catalans(100_000)) # must take large n for a precise estimation of Catalan's constant, larger n's may crash the console

def round_to_sig_figs(num, sig_figs):
    """
    Rounds a number to a specified number of significant figures.

    Args:
        num (float or int): The number to round.
        sig_figs (int): The desired number of significant figures.

    Returns:
        float: The rounded number.
    """
    if num == 0:
        return 0.0 # Zero has infinite precision in some contexts, but usually handled as 0.0
    
    # Handle negative numbers
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)

    # Calculate the exponent of the most significant digit
    # log10(num) gives the power of 10 for the number
    # floor() gets rid of the decimal part, giving the exponent of the first digit
    # E.g., log10(123) is ~2.08, floor is 2. So 10^2 is the magnitude.
    # log10(0.0123) is ~-1.9, floor is -2. So 10^-2 is the magnitude.
    exponent = math.floor(math.log10(num))

    # Determine the number of decimal places to round to
    # This is (sig_figs - 1) because the first significant digit is at 'exponent'
    # and we need (sig_figs - 1) more digits after that relative to its position.
    # So, total digits after decimal = (sig_figs - 1) - exponent
    decimal_places = sig_figs - 1 - exponent

    # Use Python's built-in round() function (which rounds to decimal places)
    rounded_num = round(num, decimal_places)

    # Convert back to original sign
    if is_negative:
        rounded_num = -rounded_num
        
    return rounded_num

print(f"\nRounding catalans(100_000) to 15 sig figs: {round_to_sig_figs(catalans(100_000), 15)}") 

G = catalans(100_000)

E = error = .915965594177219 - G

print("Error")
print(E)

print("Best we can do for now though there's propagated error in this calculation when compared to wiki source beginning around the 13th sig fig")

T = G - (np.pi*np.log(2))/4

print(f"\nT=G-$\pi*log(2)/4$: {T}")

print(f"\nRounding T to 15 sig figs: {round_to_sig_figs(T, 15)}") 

def f(t):
    return np.log(np.sin(t)+np.cos(t))

print("Let's compute the integral [0,pi/2] of ln(sin(x))+cos(x))")
def main():
    a, b, n = 0, np.pi/2, 50  # n = Number of samples

    # Generate 'n' sorted random values
    np.random.seed(2019)
    t_samples = np.sort((b - a) * np.random.rand(n))
    # Samples the curve at those angles
    f_samples = f(t_samples)

    # Compute the integral of the curve using the random
    # sample values and the *cumulative* Simpson's rule
    area_discrete = cumulative_simpson(f_samples, x=t_samples)

    # The discrete value
    print(f"Discrete Integral: {area_discrete[-1]:0.4f}")

    # Plot discrete (sampled) data
    plt.figure(Path(__file__).name)
    t = np.linspace(0, np.pi/2, 1000)
    plt.plot(t, f(t), label=r"$\int$")
    plt.scatter(t_samples, f_samples, c="r", label=f"samples ({n})")
    plt.title("Integration over Irregularly Spaced Points")
    plt.xlabel(r"$t$")
    plt.ylabel("y")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
print(r"We see that $T$ is approximately equal to the integral of $\ln(\sin(x)+\cos(x))$ on the interval $[0, \frac{\pi}{2}]$")