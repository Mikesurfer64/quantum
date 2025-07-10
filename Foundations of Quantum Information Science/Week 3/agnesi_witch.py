
"""agnesi_witch.py"""

#Reference: https://en.wikipedia.org/wiki/Witch_of_Agnesi
#Reference: Code from Dr. Biersach taylor_series.py ,newton file
#Reference: Gemini AI for modifying some code

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# According to the reference we define the witch of Agnesi where a=1/2 to be

def w(x):
    return 1/(1+np.power(x,2))

#Since d/dx arctan(x) = 1/(1+x^2) we can write the Taylor Series for arctan(x) then take term-by-term differentiation to find the resulting power (Taylor) series:
#Alternatively, since we know that the power series of x^n=1/(1-x) on its interval of convergence, we may write
# 1/(1+x^2) as 1/(1-(-x^2)) then the resulting power series rep. is summation (-1)^n(x)^(2) n=0 to inf.

def main():
    # Plot exact y = cos(x)
    x = np.linspace(-1.5, 1.5, 1000)
    plt.figure(Path(__file__).name)
    plt.plot(x, w(x), label="Exact Witch of Agnesi")

    
    current_sum = np.zeros_like(x)

    # Plot Power Series Expansion for 1/(1+x^2) for first 7 terms
    # fmt: off
    # Accumulate the n=0 and n=1 terms so they are part of the 'current_sum' before plotting starts at n=2
    current_sum += ((-1)**0) * np.power(x, 2 * 0) # n=0 term
    current_sum += ((-1)**1) * np.power(x, 2 * 1) # n=1 term

    # Iterate from 2 to 9 (to get terms from n=2 onwards for plotting partial sums)
    for n in range(2, 9): # <- Changed range here to start from 2
        term = ((-1)**n) * np.power(x, 2 * n)
        current_sum += term
        # Plot the partial sum for the current number of terms
        plt.plot(x, current_sum, label=f"Power Series (n=0 to {n})")

    plt.title("Witch of Agnesi and its Power Series Expansion")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

    # Set the y-axis limits here
    plt.ylim(-2, 2) # <- This line restricts the y-axis range

    plt.show()

if __name__ == "__main__":
    main()

"""We can observe that when x=+-i that w(x)=1/(1+x^2) is undefined (poles of w(x)) and the power series does not exist at these values
Accordingly, we cannot write a power series at x=+-i for w(x). For the divergence at x=+-1 we see that the power series at these values
is either the sums of 1's (infinite) which is divergent by the Divergence Theorem or sums of +1 and -1's which is also Divergent by the the same Divergence Theorem.
We conclude that as x approaches these values the series is unbounded (diverges). Since taking n terms of the partial sums of w(x) yields some Error Function E(x) we can illustrate that the difference
abs(w(x)-s(x))=E(x) is non-zero for large n ( in fact grows to inf for large n near x=+-1). To conclude, if one seeks an great estimate near
x=+-1 then the Taylor series could be centered closer to these poles but the result would be a less accurate overall depiction of w(x) though better
numerical estimates near these poles."""