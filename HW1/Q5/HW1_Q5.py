"""
Abhinav Sinha
SR. No. - 18750
"""

import numpy as np
from scipy.constants import electron_mass, hbar, elementary_charge


E = 10
V = 9
k1 = np.sqrt(2*electron_mass*E*elementary_charge) / hbar
k2 = np.sqrt(2*electron_mass*(E-V)*elementary_charge) / hbar

R = ((k1-k2)/(k1+k2))**2
T = 1 - R

print(f"Reflection probability: {R} \nTransmission probability: {T}")