"""custom_cf.py"""

import numpy as np
import math # DAB: Unused import?

def encode_cf(x):
    cf: list[int] = []
    while len(cf) < 7:  # MAX TERMS
        cf.append(int(x))
        x = x - int(x)
        if x < 1e-11:
            break
        x = 1 / x
    # "Normalize" the continued fraction
    if cf[-1] == 1 and cf[-2] != 1:
        cf[int(-2)] += 1
        cf.pop(-1)
    return cf

def x(n):
    return ((1+np.sqrt(4 * n * n - 4 * n+5))/2)

# Correct output!
# But I would much rather use a for loop than hardcoded prints
print(encode_cf(x(1)))
print(encode_cf(x(2)))
print(encode_cf(x(3)))
print(encode_cf(x(4)))
print(encode_cf(x(5)))
print(encode_cf(x(6)))
print(encode_cf(x(7)))
print(encode_cf(x(8)))
print(encode_cf(x(9)))