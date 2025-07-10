"""lead_attenuation.py"""

# Given N(x; E) = N_0*np.power(e,-mu(E)x) mu(E) varies ---> E varies (inputs).

# Given the text file contains E, mu(E) I'll need to interpolate these values using curve fitting methods based on this data.

# Graph E, mu(E) then finally compute mu(4.65) based on the interpolation then calculate N for specific x = 2 cm.

# reference photon python file we performed in class

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline # cubic spline interpolation

file_name = "lead_attenuation.csv"
file_path = Path(__file__).parent / file_name
energy, laf = np.genfromtxt(file_path, delimiter=",", unpack=True) #laf= Lead Attenuation Factor

min_energy, max_energy = np.min(energy), np.max(energy)
energy_est = np.linspace(min_energy, max_energy, 30)

laf_f = CubicSpline(energy, laf) 
laf_est = laf_f(energy_est)

min_window, max_window = 0, 10  # MeV. region of interest
window_energy = quad(laf_f, min_window, max_window)[0] #high order adaptive simpson , returns array
total_energy = quad(laf_f, min_energy, max_energy)[0]

plt.figure(Path(__file__).name)
plt.scatter(energy, laf, zorder=3) #higher the z order the more things that on top black curve on top of other curves perceived height

plt.plot(energy_est,laf_est)

plt.semilogy()

plt.xlabel("Energy [MeV]")
plt.ylabel(r"Lead Attenuation Factor ($\;\mu(cm^-1$)") #label axes latex \; spacing easier to read 
plt.title("Lead Attenuation Factor vs. Energy")
plt.axhline(0, c="k") #horizntal line 
plt.show()

# End plot

# Calculate mu(4.65) based on interpolation 

u = print(laf_f(4.65))

# assume x is in cm (not converted to meters)

# This value times the initial N_0 would be the number of photons emerging from a lead shield of 2 cm thickness
N = print(np.power(np.e, -2*laf_f(4.65)))

#Thus the percent of photons passing through the lead shield would be N/u=P

P = print(np.power(np.e, -2*laf_f(4.65))/laf_f(4.65))

# approximately 80.83% of photons passed through lead that's 2cm thick when energy is 4.65 and x = 2 cm (thickness)