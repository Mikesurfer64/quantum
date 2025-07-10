"""mc_exp_dist.py"""

#Reference: Dr. Biersach file on Monte Carlo Simulation
# https://en.wikipedia.org/wiki/Exponential_distribution

from numba import float64, int64, vectorize
from matplotlib.patches import Rectangle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@vectorize([float64(int64, int64)], nopython=True)
def halton(n, p):
    h, f = 0, 1
    while n > 0:
        f = f / p
        h += (n % p) * f
        n = int(n / p)
    return h

print(halton(10_000, 2))

# ((x, y) anchor point, width, height)
bbox = Rectangle((0, 0), 1, 1.5).get_bbox() #adjusted viewing rectangle
print(bbox)
total_dots = 40_600
print(f"{total_dots = :,}")

x = (1 - halton(np.arange(total_dots), 2)) * bbox.width + bbox.x0
y = (1 - halton(np.arange(total_dots), 3)) * bbox.height + bbox.y0

pd.DataFrame({"x": x[:5], "y": y[:5]})

d = y - np.power(np.e,(1/1.5) * x * (-1/1.5)) # 90 minutes = 1.5 hours

pd.DataFrame({"x": x[:5], "y": y[:5], "d": d[:5]})


x_in = x[d <= 0.0]
y_in = y[d <= 0.0]
x_out = x[d > 0.0]
y_out = y[d > 0.0]

pd.DataFrame(
    {"x_in": x_in[:5], "y_in": y_in[:5], "x_out": x_out[:5], "y_out": y_out[:5]})


plt.figure(figsize=(8, 6))
plt.scatter(x_in, y_in, color="red", marker=".", s=0.5)
plt.scatter(x_out, y_out, color="blue", marker=".", s=0.5)
plt.title("$y=(1/1.5)e^{-x/1.5}$")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

act = .48658
est = (bbox.width * bbox.height) * np.count_nonzero(d <= 0) / total_dots
err = np.abs((est - act) / act)

print(f"dots = {total_dots:,}")
print(f"act = {act:.6f}")
print(f"est = {est:.6f}")
print(f"err = {err:.5%}")

