"""
Abhinav Sinha
SR. No. - 18750
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sunspots.txt", sep="\t", header=None)
t = data[0][0:1000]
num_sunspots = data[1][0:1000]
num_sunspots2 = np.convolve(num_sunspots, np.ones(10)/10, mode="same")
plt.plot(t, num_sunspots, linewidth = 1)
plt.plot(t, num_sunspots2, 'r',  linewidth = 1)
plt.xlabel("Time (months)")
plt.ylabel("Number of sunspots")
plt.title("Number of sunspots vs Time (first 1000 entries)")
plt.legend(["original", "running average"])
plt.savefig("HW1_Q13_c.png")
plt.show()
