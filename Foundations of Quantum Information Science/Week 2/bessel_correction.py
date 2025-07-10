#!/usr/bin/env python3
"""bessel_correction.py"""

import pickle  #pickle is a file format, huffman encoded, quickly save lists, arrays to a binary file, serializing data structure 
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from numba import njit
from numpy.random import choice, randint


@njit
def get_bsv(arr): #biased sample variance calculation
    mean = np.mean(arr)
    bsv = float(np.sum((arr - mean) ** 2) / len(arr))
    return bsv


@njit #decorator to rund fast in C code
def get_sample_bsv(population, sample_size): # helper function 
    num_trials = 20_000
    total_bsv = 0.0
    for _ in range(num_trials):
        samples = choice(population, sample_size, replace=False) #numpy choice function called
        total_bsv += get_bsv(samples)
    mean_bsv = total_bsv / num_trials
    return mean_bsv


def run_trials():
    population = randint(0, 1000, 7000)
    pop_var = get_bsv(population)

    max_sample_size = 20

    print(f"{'Sample Size':^11}{'Sample Var':^21}{'Pop Var':^18}{'Ratio':^8}")

    results = []
    for sample_size in range(2, max_sample_size + 1):
        sample_bsv = get_sample_bsv(population, sample_size)
        ratio = sample_bsv / pop_var
        results.append((sample_size, sample_bsv, pop_var, ratio))
        print(
            f"{sample_size:^11}{sample_bsv:>16,.4f}{pop_var:>18,.4f}", f"{ratio:^15.4f}"
        )
    return results


def plot_ratio(ax, results):
    x1 = [r[0] for r in results]  # 1st column in results table
    y1 = [r[3] for r in results]  # 4th column in results table
    ax.plot(x1, y1, label="BSV/PV")

    x2 = np.linspace(2, 20)
    y2 = (x2 - 1) / x2
    ax.plot(x2, y2, label=r"$\frac{n-1}{n}$")

    ax.set_title(r"$\frac{BSV}{PV}$ compared to Hyperbola $\frac{(n-1)}{n}$")
    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Biased Sample Var / Population Var")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(0.05))
    ax.legend(loc="center right")


def plot_ubsv(ax, results):
    x = [r[0] for r in results]  # 1st column in results table
    y = [r[2] for r in results]  # 3rd column in results table
    ax.plot(x, y, label="Pop Var")

    y = [r[1] for r in results]
    ax.plot(x, y, label="BSV")

    for i, _ in enumerate(y):
        y[i] = y[i] * x[i] / (x[i] - 1)
    ax.plot(x, y, label="UBSV")

    ax.set_title("Variance: Population v. Biased Sample v. Unbiased Sample")
    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Variance")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.legend(loc="center right")


def main():
    plt.figure(Path(__file__).name) #graph
    file_name = "bessel.pickle"  #calc and save results
    data_file = Path(__file__).parent / file_name
    if not data_file.exists():
        results = run_trials() #sample sizes from 2, 20 
        with open(data_file, "wb") as file_out: #wb is an array saved to pickle file 
            pickle.dump(results, file_out, pickle.HIGHEST_PROTOCOL) #pick highest one
        plot_ratio(plt.gca(), results) # number of samples, bsv and superimpose hyperbola
    else: # jumpo here on run2, same data
        with open(data_file, "rb") as file_in:
            results = pickle.load(file_in)
        print(f"{'Sample Size':^11}{'Sample Var':^21}{'Pop Var':^16}{'UBSV':^12}")
        for r in results: #unpack this row
            sample_size, sample_bsv, pop_var, _ = r
            ubsv = sample_bsv * sample_size / (sample_size - 1)
            print(
                f"{sample_size:^11}{sample_bsv:>16,.4f}{pop_var:>18,.4f}",
                f"{ubsv:^18,.4f}",
            )
        plot_ubsv(plt.gca(), results)

    plt.show()


if __name__ == "__main__":
    main()
#small sample sizes the results of variance are far off