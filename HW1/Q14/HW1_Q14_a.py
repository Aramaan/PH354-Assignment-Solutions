"""
Abhinav Sinha
SR. No. - 18750
"""

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 1000)
x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)

plt.plot(x, y)
plt.title("Deltoid curve")
plt.savefig("HW1_Q14_a.png")
plt.show()