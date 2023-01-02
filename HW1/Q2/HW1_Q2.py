"""
Abhinav Sinha
SR. No. - 18750

Answer to question Q2 (b) and Q2 (c) are in comments after the code.
"""

import numpy as np
from astropy.constants import G, M_earth, R_earth
G = G.value
M = M_earth.value
R = R_earth.value

""" Q2 (a) ------------------------------------------------------------------"""
T = float(input("Enter desired time period of the satellite (in seconds): "))
h = np.cbrt(G*M/4/np.pi**2*T**2) - R
if h > 0:
    print("Altitude of the satellite above the Earth\'s surface is %.5f m" % h)
else:
    print("Not possible")


""" Q2 (b) ------------------------------------------------------------------

1 day       : Altitude of the satellite above the Earth's surface is 35862994.19769 m
90 minutes  : Altitude of the satellite above the Earth's surface is 274455.46878 m
45 minutes  : Not possible

We conclude that satellites with small time periods are at lesser height. And since the height above the earth's surface
must be positive, there is lower bound to the time period. Thus a satellite with 45 minutes time period is impossible.

--  Q2 (c) ------------------------------------------------------------------

A sidereal day is the time taken by the earth to rotate 360 deg around its axis with respect to the background, for
example a fixed star. This is equal to 23.94 hours. However a solar day is the time taken by the earth to rotate 360 deg
around its axis with respect to the sun. This is equal to 24 hours. A solar day is not a measure of true time period of
rotation of earth as it incorporates the revolution of earth around the sun as well. A sidereal day is the true time
period of rotation of earth.

    time        :   height
1 sidereal day  : 35780818.75795 m
1 solar day     : 35862994.19769 m

Height difference: 82175.43974 m

Satellite must be placed this much lower in height for geo sync.

"""





