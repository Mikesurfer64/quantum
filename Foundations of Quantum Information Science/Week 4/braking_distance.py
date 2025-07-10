#!/usr/bin/env python3
"""braking_distance.py"""

#Reference: Some code from Gemini AI
#Reference: Wikipedia for braking distance

# d=v^2/(2mu*g) braking distance from wikipedia thus mu=v^2/(2gd) 

mu_1=float((10**5)**2/(2*9.81*76.99)) #convert km/h to m/h 100 kmh=10^2*10^3 = 10^5 m/h
mu_2=float((10**5)**2/(2*9.81*126.2))
ratio = mu_2/mu_1
print(mu_1)
print(mu_2)
print(f"Average Ratio in Coefficient of Friction {ratio}")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams['text.usetex'] = True # Enables LaTeX rendering
plt.rcParams['font.family'] = 'serif' # Optional: set font to serif for LaTeX
plt.rcParams['font.serif'] = ['Computer Modern Roman']

file_name1 = "road1.csv"
data1 = np.genfromtxt(file_name1, delimiter=",")
pd.DataFrame(data1[:10], columns=["Speed (km/h)", "Braking Distance (m)"]).style.hide(axis="index")

file_name2 = "road2.csv"
data2 = np.genfromtxt(file_name2, delimiter=",")
pd.DataFrame(data2[:10], columns=["Speed (km/h)", "Braking Distance (m)"]).style.hide(axis="index")

t1 = data1[:, 0]
h1 = data1[0:, 1]

t2 = data2[:, 0]
h2 = data2[0:, 1]

p1 = np.polyfit(t1,h1,3)
p2 = np.polyfit(t2,h2,3)

poly1 = np.poly1d(p1)
poly2 = np.poly1d(p2)

x = np.linspace(0,110,1000)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, poly1(x), color="blue", label='Road 1 Fit')
ax.plot(x, poly2(x), color="green", label='Road 2 Fit')
ax.scatter(t1, h1, color="blue", alpha=0.6, label='Road 1 Data') 
ax.scatter(t2, h2, color="green", alpha=0.6, label='Road 2 Data')

plt.title(
    "Braking Distance vs Speed\n"
    r'Average Ratio in Coefficient of Friction $\frac{{\mu_2}}{{\mu_1}}=.61$', # Removed the f-string for now, it was empty
    fontsize=14
)
ax.set_xlabel("Speed (km/h)", fontsize=12)
ax.set_ylabel("Braking Distance (m)", fontsize=12)
ax.legend(loc="lower right", fontsize=10) # Use the labels defined in plot/scatter calls
ax.grid(True) # Replaced "on" with True for clarity
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()
