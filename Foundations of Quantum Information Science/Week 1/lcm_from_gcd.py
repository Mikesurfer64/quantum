#!/usr/bin/env python3
"""lcm_gcd.py"""

import numpy as np
# want to find the lcm of two integers
a, b = 447618, 200
a, b = 447618, 2011835 # DAB: The b value was not 200??
lcm = (a * b) // np.gcd(a,b)
print(f"LCM of {a:,} and {b:,} is {lcm:,}")