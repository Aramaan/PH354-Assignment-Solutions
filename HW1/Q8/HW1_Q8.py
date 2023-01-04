"""
Abhinav Sinha
SR. No. - 18750

Value of Madelung constant is -1.7418198158396654
"""

import numpy as np

L = 100
M = 0.0

for i in range(-L, L + 1):
    for j in range(-L, L + 1):
        for k in range(-L, L + 1):
            if i == 0 and j == 0 and k == 0:
                continue
            M = M + (-1)**((i+j+k) % 2) / np.sqrt(i**2 + j**2 + k**2)

print(f"Value of Madelung constant is {M}")
