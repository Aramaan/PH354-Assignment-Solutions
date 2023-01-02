"""
Abhinav Sinha
SR. No. - 18750

For tower height 100m: Time taken by the ball to hit the ground: 4.5160 seconds.
"""

import numpy as np
from scipy.constants import g

h = float(input("Enter the height of the tower: "))

print("Time taken by the ball to hit the ground: %.4f seconds" % np.sqrt(2*h/g))
