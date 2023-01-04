"""
Abhinav Sinha
SR. No. - 18750
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.constants import h

data = pd.read_csv('millikan.txt', sep=' ', header=None)

x = np.array(data[0])
y = np.array(data[1])

Ex = np.sum(x) / len(x)
Ey = np.sum(y) / len(y)
Exx = np.sum(np.power(x, 2)) / len(x)
Exy = np.sum(x * y) / len(x)

m = (Exy - Ex * Ey) / (Exx - Ex ** 2)
c = (Exx * Ey - Ex * Exy) / (Exx - Ex ** 2)

Y = m * x + c

e = 1.602e-19
h_exp = m * e
print("Planck's constant from data = %.2E \n Standard value = %.2E \n Percentage error = %.2f" % (
h_exp, h, (h - h_exp) / h * 100))
plt.figure()
plt.plot(x, y, 'k.')
plt.plot(x, Y, '--')
plt.text(0.55e15,2, "Planck's constant from data = %.2E \n Standard value = %.2E \n Percentage error = %.2f" % (
h_exp, h, (h - h_exp) / h * 100), fontsize = 10)
plt.title('Milikan')
plt.xlabel("Frequency of light (Hz)")
plt.ylabel("Stopping Voltage (V)")
plt.savefig("HW1_Q18.png")
plt.show()
