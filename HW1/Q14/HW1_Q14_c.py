"""
Abhinav Sinha
SR. No. - 18750
"""

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 24*np.pi, 10000)

r = np.exp(np.cos(theta)) - 2*np.cos(4*theta) + np.power(np.sin(theta/12), 5)
x = r*np.cos(theta)
y = r*np.sin(theta)

plt.plot(x, y)
plt.title("Fey\'s function")
plt.savefig("HW1_Q14_c.png")
plt.show()