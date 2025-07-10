"""complex_factorial.py"""


import numpy as np
import scipy as sp
from scipy.integrate import quad

#Reference: Used gamma function code from other notebook from today 
#Reference: https://en.wikipedia.org/wiki/Gamma_function
#Reference: https://mathworld.wolfram.com/GammaFunction.html
#Reference: Gemini AI to fix the code based on my initial (sad) attempt

def f(x, s):
    try:
        return np.power(x, s - 1) * np.exp(-x)
    except ZeroDivisionError:
        return 0
    
#Since gamma(i+1)=i! and gamma(i+1)= int_0^oo t^i*e^-t dt

# since x^i is e^(iln(x))=cos(ln(x))+isin(ln(x)) we can substituate this expression for x^i in the integral

#x = np.linspace(-np.inf,np.inf)
#I=quad((np.cos(np.log(x))+complex(0,1)*np.sin(np.log(x))) * np.exp(-x),0,np.inf)

# --- Define the real and imaginary parts of the integrand ---
def real_part_integrand(x):
    # The term is cos(ln(x)) * exp(-x)
    # Handle potential issues for x <= 0 if the integral limits were different.
    # For 0 to inf, ln(x) is real for x > 0.
    if x == 0: # Handle x=0 explicitly, as ln(0) is undefined
        return 0
    return np.cos(np.log(x)) * np.exp(-x)

def imag_part_integrand(x):
    # The term is sin(ln(x)) * exp(-x)
    if x == 0: # Handle x=0 explicitly
        return 0
    return np.sin(np.log(x)) * np.exp(-x)

# --- Perform the integration ---
# Integrate the real part
integral_real_part, abserr_real = quad(real_part_integrand, 0, np.inf)

# Integrate the imaginary part
integral_imag_part, abserr_imag = quad(imag_part_integrand, 0, np.inf)

# Combine the results
I_complex = integral_real_part + complex(0, 1) * integral_imag_part

print(f"Real part of the integral: {integral_real_part} (Error: {abserr_real})")
print(f"Imaginary part of the integral: {integral_imag_part} (Error: {abserr_imag})")
print(f"Combined complex integral result: {I_complex}")

# If you were aiming to compute the Gamma function, note that Gamma(1+i) is a known value.
# The integral you wrote, int_0^oo t^i*e^-t dt, is Gamma(1+i).
# You can compare your result to scipy.special.gamma(1 + 1j)
from scipy.special import gamma
gamma_1_plus_i = gamma(1 + complex(0, 1))
print(f"\nValue of Gamma(1+i) from scipy.special: {gamma_1_plus_i}")