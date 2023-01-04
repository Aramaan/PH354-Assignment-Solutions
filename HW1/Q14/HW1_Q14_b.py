"""
Abhinav Sinha
SR. No. - 18750
"""

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 1000)

r = np.power(theta, 2)
x = r*np.cos(theta)
y = r*np.sin(theta)

plt.plot(x, y)
plt.title("Galilean curve")
plt.savefig("HW1_Q14_b.png")
plt.show()