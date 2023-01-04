"""
Abhinav Sinha
SR. No. - 18750
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("stm.txt", header=None, sep=' ')
X, Y = np.meshgrid(range(data.shape[1]), range(data.shape[0]))

# heat map
plt.figure(1)
plt.pcolormesh(data)
plt.colorbar()
plt.title("STM measurement of (111) Silicon (Heat Map)")
plt.savefig('HW1_Q15_heatmap.png')
plt.show()

# Surface plot
plt.figure(2)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, data ,cmap='viridis', edgecolor='none')
ax.set_title('STM measurement of (111) Silicon (Surface plot)')
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig('HW1_Q15_surfaceplot.png')
plt.show()
