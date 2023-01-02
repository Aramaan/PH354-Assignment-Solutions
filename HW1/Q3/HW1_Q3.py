"""
Abhinav Sinha
SR. No. - 18750
"""

import numpy as np

x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

r = np.sqrt(x**2 + y**2)
if x==0 and y==0:
    print("r: 0, theta: undefined")
    exit(0)
elif x == 0 and y >= 0:
    theta = 90
elif x == 0 and y <= 0:
    theta = -90
elif x > 0 and y >= 0:
    theta = np.rad2deg(np.arctan(y / x))
elif x > 0 and y <= 0:
    theta = np.rad2deg(2 * np.pi + np.arctan(y / x))
else:
    theta = np.rad2deg(np.pi + np.arctan(y / x))

print("r: %.5f, theta: %.5f" % (r, theta))