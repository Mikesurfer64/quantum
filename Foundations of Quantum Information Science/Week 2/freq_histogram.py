#!/usr/bin/env python3
"""freq_histogram.py"""

import collections # creates the statistics to make a histrogram
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# file_name = "gettysburg.txt" # open this file
file_name = "ciphertext1.txt"

# Read the data file into a buffer
file_path = Path(__file__).parent / file_name #path to find file, / concatanter, parent containing folder of script
with open(file_path, "rb") as f_in: #closes, rb=read binary (file object), file input = file name with is a scope
    f_bytes = bytearray(f_in.read()) # read into an array of bytes

# Only set tick marks for characters that occur more than 6%
ticks = []
char_count = np.zeros(256) #track how many times each byte
for char, count in collections.Counter(f_bytes).items(): #return how many times each char appears
    char_count[char] = count 
    if count / len(f_bytes) > 0.06: #only for those ASCII values who occur greater than 6% of the time
        ticks.append(char)

# Create a histogram of each character's ASCII value
plt.figure(Path(__file__).name)
plt.bar(np.arange(256), char_count) #pass in two arrays
plt.xticks(ticks)
plt.tick_params("x", rotation=90)
plt.title(f"Frequency Analysis ({file_name})")
plt.xlabel("ASCII Value")
plt.ylabel("Count")
plt.show()
