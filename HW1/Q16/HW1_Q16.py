"""
Abhinav Sinha
SR. No. - 18750

(a) for 1<r<3 Feigenbaum plot is a fixed point. After 3 it bifurcates and settles into a limit cycle. At around r = 3.4
it further bifurcates (period doubling). The amount of r that is needed for next bifurcation becomes smaller and smaller
and at critical value the system falls into infinite period cycle. This is chaotic behaviour.

(b) Edge of Chaos: r ~= 3.6
"""

import numpy as np
import matplotlib.pyplot as plt

prs = 0.01
r = np.arange(1,4,prs)


def fp(r):
    x = 0.5
    for i in range(1000):
        x = r*x*(1-x)
    out = np.zeros(1000)
    for i in range(1000):
        out[i] = x
        x = r*x*(1-x)
    return out


result = [fp(k) for k in r]
fig, ax = plt.subplots()
for i in range(len(r)):
    ax.scatter([r[i]]*1000, result[i], c='k', s=1)
plt.title('Feigenbaum plot')
plt.xlabel('r')
plt.ylabel('x')
plt.grid()
plt.savefig("HW1_Q16.png")
plt.show()