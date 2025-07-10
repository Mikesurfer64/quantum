#!/usr/bin/env python3
"""make_samples.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

# We are genreally not privy to the underlying formula that generated 

# fmt: off
def f(x):
    return np.array(29 * np.cos(3 * x) + 7 * np.cos(19 * x)
                    + 17 * np.sin(11 * x) + 2 * np.sin(31 * x))
# fmt: on


def main():
    sample_duration = 2 * np.pi
    num_samples = 1000

    ts = np.linspace(0, sample_duration, num_samples, endpoint=False) # current time of the experiment
    fs = f(ts) #f at each time step

    file_name = "samples.csv"
    file_path = Path(__file__).parent / file_name
    np.savetxt(file_path, np.column_stack((ts, fs)), fmt="%1.13f", delimiter=", ") # 2 rows x 1000 columns, create file
    #numpy take vectors and make matrix out of them, two vectors (columns stack), save then plot

    plt.figure(Path(__file__).name)
    # fmt: off
    plt.plot(ts, fs, color="lightgray",
        marker="o", markerfacecolor="none",
        markersize=1, markeredgecolor="black")
    # fmt: on
    plt.title(f"Sampled Wave ({num_samples} samples)")
    plt.xlabel("time")
    plt.ylabel("amplitude")
    plt.axhline(y=0.0, color="lightgray", linewidth=1)
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    plt.show()


if __name__ == "__main__":
    main()
