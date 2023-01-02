"""
Abhinav Sinha
SR. No. - 18750

Verification with Earth and Halley's comet after the code
"""

import numpy as np
from astropy.constants import G, M_sun

G = G.value
M = M_sun.value

l1 = float(input("Enter the perihelion distance: "))
v1 = float(input("Enter the perihelion velocity: "))

a = 1/(2/l1 - v1**2/G/M)
e = 1 - l1/a
l2 = a*(1+e)
v2 = l1*v1/l2
T = np.sqrt(4*np.pi**2/G/M*a**3)/3.15576e7

print("Aphelion distance: %.5f" % l2)
print("Aphelion velocity: %.5f" % v2)
print("Orbital period: %.5f" % T)
print("Eccentricity: %.5f" % e)

"""
-------------------------------------------------------------

For Earth:

Perihelion distance: 1.4710e11
Perihelion velocity: 3.0287e4
Aphelion distance: 152111350728.59259
Aphelion velocity: 29289.18637
Orbital period: 1.00010
Eccentricity: 0.01675
-------------------------------------------------------------

For Halley's Comet

Perihelion distance: 8.7830e10
Perihelion velocity: 5.4529e4
Aphelion distance: 5371566481143.35352
Aphelion velocity: 891.59877
Orbital period: 77.94568
Eccentricity: 0.96782
"""