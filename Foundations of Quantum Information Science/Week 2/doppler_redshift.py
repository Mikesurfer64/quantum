"""doppler_redshift.py"""
import matplotlib.pyplot as plt
import numpy as np

# Use Ryberg's Formula for k=2, adapted code from Dr. Biersach and modified/prompted code from Gemini AI, needed to account for the doppler shift
#as the light moved away from the fixed observer, adjusted plotting 
# we observe that as c increases, R decreases, hence wavelength decreases (higher energy state)
#conversely, as c decreses, R increases, hence wavelength increases (lower energy state)
import numpy as np
import matplotlib.pyplot as plt # Corrected import for plotting

# Define the fundamental physical constants with precise approximate values
# These are needed for the Rydberg constant formula
e_mass = 9.1093837015e-31  # kg (electron mass)
e_charge = 1.602176634e-19 # C (elementary charge)
permittivity = 8.8541878128e-12 # F/m (permittivity of free space, epsilon_0)
h_plank = 6.62607015e-34   # J s (Planck's constant)
c_light = 2.99792458e8     # m/s (speed of light in vacuum)

# --- Helper function to map wavelength to spectral color ---
def get_spectral_color(wavelength_nm):
    """
    Returns an approximate hexadecimal color code for a given wavelength in nm.
    Includes visible light and extends into the infrared spectrum.
    """
    # Visible spectrum
    if 380 <= wavelength_nm < 450:
        return '#8A2BE2'  # Violet (BlueViolet)
    elif 450 <= wavelength_nm < 495:
        return '#0000FF'  # Blue
    elif 495 <= wavelength_nm < 570:
        return '#00FF00'  # Green
    elif 570 <= wavelength_nm < 590:
        return '#FFFF00'  # Yellow
    elif 590 <= wavelength_nm < 620:
        return '#FFA500'  # Orange
    elif 620 <= wavelength_nm <= 750:
        return '#FF0000'  # Red
    # Infrared spectrum (extended range up to 2000 nm)
    elif 750 < wavelength_nm <= 2000: # Extended to include wavelengths up to 2000 nm
        return '#8B0000' # Dark Red / Maroon
    # Beyond visible and defined IR, or UV
    else:
        return '#808080'  # Gray for UV/Far-IR or out of defined range

# --- Function to calculate Rydberg Constant ---
def calculate_rydberg_constant(speed_of_light_override=None):
    """
    Calculates the Rydberg constant (R_infinity) using fundamental physical constants.

    The formula for the Rydberg constant R_infinity is:
    R_infinity = (m_e * e^4) / (8 * epsilon_0^2 * h^3 * c)

    Args:
        speed_of_light_override (float, optional): An optional value to use for
            the speed of light instead of the default c_light.

    Returns:
        float: The calculated value of the Rydberg constant in m^-1.
               Returns None if any required constant is not defined or denominator is zero.
    """
    # Use the provided speed_of_light_override if given, otherwise use the global c_light
    current_c = speed_of_light_override if speed_of_light_override is not None else c_light

    try:
        # Calculate the numerator: (electron_mass * elementary_charge^4)
        numerator = e_mass * (e_charge**4)

        # Calculate the denominator: (8 * permittivity**2 * planck_constant**3 * speed_of_light)
        denominator = 8 * (permittivity**2) * (h_plank**3) * current_c

        # Ensure denominator is not zero to prevent division by zero error
        if denominator == 0:
            print("Error: Denominator is zero, cannot calculate Rydberg constant.")
            return None

        rydberg_inf = numerator / denominator
        return rydberg_inf
    except NameError as e:
        print(f"Error: A required constant is not defined. {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during calculation: {e}")
        return None

# --- Function to calculate Doppler Shift ---
def calculate_doppler_shift(emitted_wavelength, relative_velocity_of_source, speed_of_light=c_light):
    """
    Calculates the observed wavelength due to the relativistic Doppler effect.

    Formula: lambda_observed = lambda_emitted * sqrt((1 + v/c) / (1 - v/c))

    Args:
        emitted_wavelength (float): The wavelength of light emitted by the source (in nm).
        relative_velocity_of_source (float): The velocity of the source relative to the observer (in m/s).
                                             Positive for recession (moving away), negative for approach (moving towards).
        speed_of_light (float): The speed of light in vacuum (in m/s).

    Returns:
        float: The observed wavelength (in nm).
    """
    beta = relative_velocity_of_source / speed_of_light
    if abs(beta) >= 1:
        print("Error: Relative velocity cannot be equal to or greater than the speed of light.")
        return emitted_wavelength # Return original wavelength or handle as error

    # Relativistic Doppler shift formula
    observed_wavelength = emitted_wavelength * np.sqrt((1 + beta) / (1 - beta))
    return observed_wavelength


# --- Main Program Execution ---

# List to store all spectral data for the combined plot
all_spectral_data = []

print("Rydberg Formula for Hydrogen Spectral Lines (Balmer Series, k=2)")

# Constants for wavelength calculation (Balmer series, fixed final orbit k=2)
K_BALMER_FINAL_ORBIT = 2
# J_INITIAL_ORBITS for Balmer series: 3, 4, 5, 6
J_INITIAL_ORBITS_BALMER = range(K_BALMER_FINAL_ORBIT + 1, K_BALMER_FINAL_ORBIT + 5)

# Using the standard Rydberg constant for hydrogen (from your original code)
# Note: This is an empirical value, not derived from fundamental constants in this section.
rydberg_constant_empirical = 1.0967757e7 # spectral lines for Hydrogen (in m^-1)

for k_val in range(K_BALMER_FINAL_ORBIT, K_BALMER_FINAL_ORBIT + 1): # loop for k=2
    for j_val in J_INITIAL_ORBITS_BALMER: #initial orbit (higher)
        try:
            # Formula for waveLength in nanometers
            wave_length = 1 / (rydberg_constant_empirical * (1 / pow(k_val, 2) - 1 / pow(j_val, 2))) * 1e9
            print(f"\t{j_val:>2} -> {k_val:>2}{wave_length:8.0f} nm")
            all_spectral_data.append({
                'wavelength': wave_length,
                'transition': f"{j_val} -> {k_val}",
                'rydberg_source': 'Empirical R',
                'series_type': 'empirical_k2',
                'c_factor': 1.0 # Represents standard c_light for this (for plotting purposes)
            })
        except ZeroDivisionError:
            print(f"\tError: Division by zero when calculating wavelength for j={j_val}, k={k_val}.")
        except Exception as e:
            print(f"\tAn error occurred calculating wavelength for j={j_val}, k={k_val}: {e}")
print()


print("\n--- Calculating Rydberg Constant using fundamental constants (Standard Speed of Light) ---")

# Calculate Rydberg Constant using the defined fundamental constants and standard c_light
R_value_fundamental = calculate_rydberg_constant()
if R_value_fundamental is not None:
    print(f"Calculated Rydberg Constant (R_infinity from fundamentals): {R_value_fundamental:.10e} m^-1")
    # You can compare this to the CODATA recommended value: 1.0973731568160e7 m^-1
    # The difference might be due to the precision of the fundamental constants used.


# Removed the "Rydberg Formula for Hydrogen Spectral Lines for 10%, 30%, 50%, 80%, 100% the speed of light, k=2 (Balmer series)" section
# As requested, the calculations and plots for 'Scaled c' are removed.


# --- Adding Doppler Shift Calculations and Plotting ---
print("\n--- Calculating Doppler Shifted Spectral Lines (applied to original Empirical R wavelengths) ---")

# Define example relative velocities (in fractions of c_light) for recession (moving away)
# These are the requested values: 10%, 30%, 50%, 80% the speed of light
relative_velocities_c_fractions = [0.10, 0.30, 0.50, 0.80]

# Filter for the original empirical R data to apply Doppler shift
empirical_r_data = [data for data in all_spectral_data if data['series_type'] == 'empirical_k2']

# Loop through each relative velocity
for v_fraction in relative_velocities_c_fractions:
    relative_v = v_fraction * c_light
    print(f"Applying Doppler Shift for relative velocity: {relative_v:.2e} m/s ({v_fraction*100:.0f}% of c_light):")
    for original_line in empirical_r_data:
        emitted_wavelenth = original_line['wavelength']
        shifted_wavelength = calculate_doppler_shift(emitted_wavelenth, relative_v)

        if shifted_wavelength is not None:
            print(f"\tOriginal: {emitted_wavelenth:.0f} nm -> Shifted: {shifted_wavelength:.0f} nm")
            all_spectral_data.append({
                'wavelength': shifted_wavelength,
                'transition': original_line['transition'],
                'rydberg_source': f'Doppler Shifted (v={v_fraction:.0%})',
                'series_type': 'doppler_shifted',
                'c_factor': v_fraction # Using c_factor to store v/c for labeling
            })
    print()


# --- Combined Plotting of All Spectral Lines ---
if all_spectral_data:
    plt.figure(figsize=(18, 9)) # Wider figure for better label spacing
    ax = plt.gca() # Get current axes for annotations

    # *** Plotting all data (no filter for visible wavelengths) as requested ***

    # Sort all data by wavelength to ensure labels are placed neatly (optional but good practice)
    all_spectral_data.sort(key=lambda x: x['wavelength'])

    # Adjusted y-levels for better spacing
    y_level_empirical = 1.0  # Height for empirical (k=2) lines
    # Removed y_level_scaled_start as scaled_c_k2 series is removed
    y_level_doppler_start = 0.7 # Adjusted starting height for Doppler shifted lines

    # Removed y_offset_per_scaled_series
    y_offset_per_doppler_series = 0.15 # Offset for each Doppler series

    text_vertical_offset = 0.07

    plotted_labels = set()
    # Removed c_factors_plotted
    doppler_v_factors_plotted = [] # For doppler_shifted

    # Determine dynamic x-axis limits based on ALL wavelengths in all_spectral_data
    min_wavelength = min(d['wavelength'] for d in all_spectral_data)
    max_wavelength = max(d['wavelength'] for d in all_spectral_data)
    x_buffer = (max_wavelength - min_wavelength) * 0.1 # Increased buffer to 10%
    plot_xlim_min = min_wavelength - x_buffer
    plot_xlim_max = max_wavelength + x_buffer

    horizontal_text_offset_amount = (plot_xlim_max - plot_xlim_min) * 0.005 # Small offset in nm relative to plot range

    # Iterate over all_spectral_data directly
    for i, line_data in enumerate(all_spectral_data):
        wavelength = line_data['wavelength']
        transition = line_data['transition']
        series_type = line_data['series_type']
        # c_factor = line_data.get('c_factor', 1.0) # c_factor might not be present for all now

        color = get_spectral_color(wavelength) # This function will assign a color (gray for non-visible)

        x_text_pos = wavelength
        ha_align = 'center'
        # Apply alternating horizontal offset for text labels
        if i % 2 == 0:
            x_text_pos += horizontal_text_offset_amount
            ha_align = 'left'
        else:
            x_text_pos -= horizontal_text_offset_amount
            ha_align = 'right'

        if series_type == 'empirical_k2':
            label_text = "Empirical R (k=2)"
            if label_text not in plotted_labels:
                plt.vlines(wavelength, 0, y_level_empirical, color=color, linewidth=2, linestyle='-', label=label_text)
                plotted_labels.add(label_text)
            else:
                plt.vlines(wavelength, 0, y_level_empirical, color=color, linewidth=2, linestyle='-')

            ax.text(x_text_pos, y_level_empirical + text_vertical_offset,
                    f"{transition}\n{wavelength:.0f}nm",
                    rotation=90, va='bottom', ha=ha_align, fontsize=8, color=color)

        # Removed 'elif series_type == 'scaled_c_k2':` block as requested

        elif series_type == 'doppler_shifted':
            # Use c_factor here to represent v/c fraction for Doppler shift
            v_frac = line_data['c_factor']
            if v_frac not in doppler_v_factors_plotted:
                doppler_v_factors_plotted.append(v_frac)
            current_y_level_doppler = y_level_doppler_start - (doppler_v_factors_plotted.index(v_frac) * y_offset_per_doppler_series)

            label_text = f"Doppler v={v_frac*100:.0f}% (k=2)"
            # Use different linestyle for Doppler shifted lines, e.g., ':'
            if label_text not in plotted_labels:
                plt.vlines(wavelength, 0, current_y_level_doppler, color=color, linewidth=2, linestyle=':', label=label_text)
                plotted_labels.add(label_text)
            else:
                plt.vlines(wavelength, 0, current_y_level_doppler, color=color, linewidth=2, linestyle=':')

            ax.text(x_text_pos, current_y_level_doppler + text_vertical_offset,
                    f"v={v_frac:.0%}\n{transition}\n{wavelength:.0f}nm",
                    rotation=90, va='bottom', ha=ha_align, fontsize=8, color=color)


    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Intensity Only") # Changed label here
    plt.title("Hydrogen Spectral Lines (Balmer Series, k=2): Empirical R and Doppler Shift") # Updated title
    plt.xlim(plot_xlim_min, plot_xlim_max) # Dynamically set x-axis limits to include all wavelengths
    # Adjusted y-limits to accommodate new staggered y-levels and text labels for all series
    # Max height is empirical_k2 level + text offset, min height is lowest doppler level - buffer
    max_y_plot = y_level_empirical + text_vertical_offset + 0.05
    min_y_plot = y_level_doppler_start - (len(doppler_v_factors_plotted) * y_offset_per_doppler_series) - 0.05
    plt.ylim(min_y_plot if min_y_plot < 0 else 0, max_y_plot) # Ensure y-axis starts at 0 or below if lines extend there

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.show()
