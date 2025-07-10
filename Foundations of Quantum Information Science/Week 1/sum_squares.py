#!/usr/bin/env python3
'''sum_squares.py'''

import numpy as np

k = np.arange(1, 1001)
y1 = np.sum(k * k)
print(f"y1 = {y1:,}")

#Does this match Gauss' equation? 
# Gauss' equation: 1^2+2^2+3^2+...n^2=(n+1)(2n+1)/6
# Let n=1,000
n = 1000
y2 = n * ((n+1) * (2 * n+1))/6
print(f"y2 = {y2:,}")