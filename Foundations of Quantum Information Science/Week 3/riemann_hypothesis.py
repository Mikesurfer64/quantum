#!/usr/bin/env python3
"""riemann_hypothesis.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

# Some Riemann zeros from the Riemann Zeta function are found in this lab notebook
# While there are some agreement upon the zeros of the eta function and zeta function, there's still investigation needed
# about what makes the two functions equivalent ( not equal)

def eta_term(s, n):
    return complex(1 / np.power(n, s))


def fn_eta(s):
    terms = int(1000)
    vec_eta_term = np.vectorize(eta_term) #vectorize tuple
    eta = (
        complex(1)
        - np.sum(vec_eta_term(s, np.arange(2, terms, 2, dtype=int)))
        + np.sum(vec_eta_term(s, np.arange(3, terms, 2, dtype=int)))
    )
    return eta


def fn_zeta_from_eta(s):
    return fn_eta(s) / (1.0 - np.power(2, 1.0 - s)) # Riemann Zeta Function in terms of eta


def main():
    xa = np.linspace(-1, 31, 800)
    xz = [complex(0.5, i) for i in xa]  #Riemann Hypothesis

    eta = [fn_eta(s) for s in xz]
    zeta = [fn_zeta_from_eta(s) for s in xz]
    zeta_zeros_im = [float(mp.im(mp.zetazero(n))) for n in range(1, 5)]

    plt.figure(Path(__file__).name)
    plt.plot(xa, np.absolute(eta), label=r"$\zeta \left( s \right)$")
    plt.plot(xa, np.absolute(zeta), label=r"$\eta \left( s \right)$", color="red")
    plt.scatter(
        zeta_zeros_im,
        [0] * len(zeta_zeros_im),  # np.zeros_like(zeta_zeros_im) # repitition operator
        marker="o",
        color="green",
        label=r"$\zeta\ root$",
    )
    plt.title(r"Riemann $\zeta(s)$ vs. Dirichlet $\eta(s)$")
    plt.xlabel(r"$\mathrm{Im\left(s\right)}$")
    plt.ylabel(r"$\mathrm{|s|}$")
    ax = plt.gca()
    ax.legend(loc="upper left")
    ax.set_axisbelow(True)                         #matplotlib Zorder 
    ax.grid(color="gray", linestyle="dashed")
    plt.show()


if __name__ == "__main__":
    main()
