"""hydrogen_spectrum.py"""

#!/usr/bin/env python3

#Code from Dr. Biersach, edited

#According to wiki Pfund has k=5 and Humphfrey's has k=6
#Will print Pfund then Humphfrey's high energy spectral series of hydrogen for Rydberg's Forumula

e_charge = 1.602e-19
e_mass = 9.109e-31
permittivity = 8.854e-12
h_plank = 6.626e-34
speed_light = 2.998e8

print("Rydberg Formula for Hydrogen Spectral Lines")

rydberg_constant = 1.0967757e7 #spectral lines for Hydrogen

for k in range(5, 7): #final orbit (lower), range not inclusive
    for j in range(k + 1, k + 6): #initial orbit (higher)
        # Formula for waveLength in nanometers
        wave_length = 1 / (rydberg_constant * (1 / pow(k, 2) - 1 / pow(j, 2))) * 1e9
        print(f"\t{j:>2} -> {k:>2}{wave_length:8.0f} nm") #backslash t
    print()

print("Bohr's formula for ground state energy")

e_0 = pow(e_charge, 4) * e_mass / (8 * pow(permittivity, 2) * pow(h_plank, 2))

for final_orbit in range(5, 7):
    for init_orbit in range(final_orbit + 1, final_orbit + 6):
        # Initial energy level
        e_i = -e_0 / pow(init_orbit, 2)
        # Final energy level
        e_f = -e_0 / pow(final_orbit, 2)
        # Formula for waveLength in nanometers
        wave_length = h_plank * speed_light / (e_i - e_f) * 1e9
        print(f"\t{init_orbit:>2} -> {final_orbit:>2}{wave_length:8.0f} nm")
    print()