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
plt.plot(t, num_sunspots)
plt.xlabel("Time (months)")
plt.ylabel("Number of sunspots")
plt.title("Number of sunspots vs Time (first 1000 entries)")
plt.savefig("HW1_Q13_b.png")
plt.show()
