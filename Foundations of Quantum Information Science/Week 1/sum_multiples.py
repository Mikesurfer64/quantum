#!/usr/bin/env python3
'''sum_multiples.py'''

import numpy as np # DAB: Unused import?

#if divisible by 7 and 11, the number is divisible by 77
# DAB: Correct, because 7 and 11 happen to be coprime (they are both primes)
# But the requirement was to calculate the sum of all those numbers!

def main():
    for n in range(1, 1_900):
        if n % 77 == 0:
            print(f"{n:,} is divisible by 7 and 11")
if __name__ == "__main__":
    main()
