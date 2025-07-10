import numpy as np
import matplotlib.pyplot

# reference https://en.wikipedia.org/wiki/Benford%27s_law

#Law of Anomalous Numbers to calculate the probabilty each digit of 1 thru 9 appearing as the most sig. digit in 100,000 very large random
#integers

#Integers chosen from a uniform dist. btwn 1 and 1,000,000 inclusive then raise to 100th power

# Most sig digit is the leftmost non-zero digit of a number. e.g. 1234 then 1 is the most sig digit 

# Let 1,000,000 ==>convert to list ==> [1,0,0,0,0,0,0] generally if string a1a2a3a4a5a6a7 where a_1...a_7 is in [1,9] convert to wlog list l=[a1,a2,a3,a4,a5,a6,a7]
# Idea:
# for i in range(7) write l[i] where l[i]=a_i 
# if l[1]=0 return l[2] 
# else l[1]
# if l[2]=0 return l[3] 
# else l[2]
# ...
# print l[i]

#iterate over 100,000  postive integers, raise each to the 100th power, then print count of number of times each digit 1,...,9 represented by each l[i] appears

#I've prompted gemini AI accordingly and took account of any major errors in the code that I've found, here's the result of that output: 

import numpy as np
from collections import defaultdict
import time
import matplotlib.pyplot as plt

# --- Parameters for generating base numbers that favor Benford's Law ---
# Instead of uniform linear, we'll draw exponents uniformly to get a log-uniform distribution
# This will ensure the numbers span many orders of magnitude, making Benford's Law apparent
log_min = 0      # Corresponds to 10^0 = 1
log_max = 6.0    # Corresponds to 10^6 = 1,000,000
# So, the "base numbers" will be approximately from 1 to 1,000,000 but picked to span orders of magnitude.

# Number of random integers to generate
num_samples = 100000

# The power to which each number will be raised (still 100)
exponent = 100

# Initialize a dictionary to store counts for each leftmost non-zero digit
leftmost_non_zero_digit_counts = defaultdict(int)

print(f"Starting process: Generating {num_samples} numbers from a log-uniform distribution (10^{log_min} to 10^{log_max}), then raising to power {exponent}...")
start_time = time.time()

# Generate numbers with a log-uniform distribution
# This ensures that numbers across all orders of magnitude are equally likely (e.g., 1-9, 10-99, 100-999, etc.)
# Then we raise these numbers to the 100th power to amplify the effect
random_log_exponents = np.random.uniform(low=log_min, high=log_max, size=num_samples)
random_base_numbers = [int(10**exp) for exp in random_log_exponents]


# Process each generated number
for i, num in enumerate(random_base_numbers):
    if (i + 1) % 10000 == 0:
        print(f"Processing number {i + 1}/{num_samples}...")

    # Ensure num is at least 1, as 0**100 is 0
    if num == 0:
        num = 1 # Replace 0 with 1 to avoid issues, or skip, depending on desired behavior

    # Raise the chosen integer to the 100th power
    powered_num = num ** exponent

    # Convert the powered number to a string
    s_powered_num = str(powered_num)

    # Find the leftmost non-zero digit
    leftmost_digit = None
    for char_digit in s_powered_num:
        if not char_digit.isdigit():
            continue
        
        digit = int(char_digit)
        if digit != 0:
            leftmost_digit = digit
            break

    if leftmost_digit is not None and 1 <= leftmost_digit <= 9:
        leftmost_non_zero_digit_counts[leftmost_digit] += 1

end_time = time.time()
print(f"Finished processing in {end_time - start_time:.2f} seconds.")

# Print the count of each leftmost non-zero digit (1-9)
print(f"\nCounting leftmost non-zero digits for {num_samples} numbers, each raised to the {exponent}th power:")
print(f"Base numbers drawn from a LOG-UNIFORM Distribution (approx {10**log_min:.0e} to {10**log_max:.0e}):")

# Calculate total count for percentage
total_counted_digits = sum(leftmost_non_zero_digit_counts.values())

for digit in range(1, 10):
    count = leftmost_non_zero_digit_counts[digit]
    percentage = (count / total_counted_digits) * 100 if total_counted_digits > 0 else 0
    print(f"Digit {digit}: {count} times ({percentage:.2f}%)")

# --- Matplotlib Plotting ---

# Create data for the bar chart
digits = list(range(1, 10))
counts = [leftmost_non_zero_digit_counts[d] for d in digits]

plt.figure(figsize=(12, 7))
bars = plt.bar(digits, counts, color='skyblue', label='Observed Frequency')

# Add counts and percentages on top of the bars
for bar, count in zip(bars, counts):
    yval = bar.get_height()
    percentage = (count / total_counted_digits) * 100 if total_counted_digits > 0 else 0
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02 * max(counts),
             f'{count}\n({percentage:.1f}%)', ha='center', va='bottom', fontsize=8)


plt.xlabel("Leftmost Non-Zero Digit")
plt.ylabel("Frequency (Count)")
plt.title(f"Distribution of Leftmost Non-Zero Digits (N={num_samples}, Power={exponent})\n"
          f"Base numbers from LOG-UNIFORM Distribution (10^{log_min:.0f} to 10^{log_max:.0f})")
plt.xticks(digits)
plt.grid(axis='y', linestyle='--', alpha=0.7)


# --- Benford's Law (Theoretical) Calculation and Plotting ---
benford_probabilities = [np.log10(1 + 1/d) for d in digits]
benford_theoretical_counts = [p * total_counted_digits for p in benford_probabilities]

plt.plot(digits, benford_theoretical_counts,
         'r-o', linestyle='--', marker='o', markersize=8, label="Benford's Law (Theoretical)")
plt.legend()


plt.tight_layout()
plt.show()

print("\n--- Summary Statistics of Leftmost Digits ---")
total_sum_of_digits = sum(d * leftmost_non_zero_digit_counts[d] for d in digits)
mean_digit = total_sum_of_digits / total_counted_digits if total_counted_digits > 0 else 0

sum_of_squared_diffs = sum(leftmost_non_zero_digit_counts[d] * ((d - mean_digit)**2) for d in digits)
std_dev_digit = np.sqrt(sum_of_squared_diffs / total_counted_digits) if total_counted_digits > 0 else 0

print(f"Mean of Leftmost Digits: {mean_digit:.4f}")
print(f"Standard Deviation of Leftmost Digits: {std_dev_digit:.4f}")
print("Mean Square Distance (MSE) is typically used for error measurement, not descriptive statistics of a distribution.")